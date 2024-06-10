#!/usr/bin/python3
""" Index """
from models.biddoc import Biddoc
from models import storage
from models.user import User
from models.utype import Utype
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import re

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Biddoc, User, Utype]
    names = ["biddocs", "users", "utype"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)


@app_views.route('/process', methods=['GET'],
                 strict_slashes=False)
def get_process():
    """ Retrieves an biddoc data"""
    """
    Retrieves a list of top biddocs
    """
    all_biddocs = storage.all(Biddoc).values()
    list_biddocs = []
    for biddoc in all_biddocs:
        list_biddocs.append(biddoc.to_dict())
    
    if biddoc.codetext == 'fromurl':
        url = biddoc.url
        resp = requests.get(url)
        datas = resp.text
        print("getdatas=" + datas)
        datas = re.sub('\W+','', datas )
        datas = datas.replace("'"," ")
        datas = datas.replace("\""," ")
        datas = datas.replace("{"," ")
        datas = datas.replace("}"," ")
        biddoc.codetext = datas
        storage.save()
       
    searchKeyWord = biddoc.codetext

    result = remove_top_lines(searchKeyWord, num_lines=2)
 
    print(result)


    urls = "https://api.github.com/search/code?q=" + result + " +in:file +language:python"

    headers = {
    'Authorization': '',
    'Accept' : 'application/vnd.github.text-match+json'
    }

    response = requests.request("GET", urls, headers=headers)
    if response.status_code == 200:
        """getresult =json.dumps(response.text)"""
        response = response.json()
        x = json.dumps(response["items"][0]["text_matches"])

        with open("gitresult-text.json", mode="+w", encoding="utf-8") as myfile:
            count = myfile.write(x)
        new_dict = {}
        jj = 0
        for i in response["items"]:
            """ for j in i["items"]: """

            subset_dict = {key: value for key, value in i.items() if key in {'name', 'html_url'}}
            new_dict.update({jj:subset_dict['html_url']})
            jj += 1

        """print(new_dict)"""
        for i, j in new_dict.items():
            print("{}:{}".format(i, j))
 
        datas = [new_d for new_d in new_dict.items()]

        return jsonify(datas)
    
    elif response.status_code == 404:
        print(response)
        return jsonify({"status": "404"})
    else:
        print(response.text)
        return jsonify({"status": "error"})


def remove_top_lines(input_string, num_lines=1):
    lines = input_string.splitlines()
    return "\n".join(lines[num_lines:])

def is_valid_github_url(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False
