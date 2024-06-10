
$(document).ready(function () {

  const HOST = '0.0.0.0';
//  const HOST = '196.189.23.236';

 // Get api status
 $.get(`http://${HOST}:5002/api/v1/status/`, data => {
  if (data.status == "OK") {
    $('DIV#api_status').addClass("available");
  } else {
    $('DIV#api_status').removeClass("available");
    $('DIV#api_status').addClass("notavailable");
  }
});

 
  // submit file
  $('#submitfile').click(function () {
 
  readFile();
  });
  $('#submiturl').click(function () {
 
    readurl();
    });

 });



function readurl() {
const fileUrl = document.getElementById('formUrl');

const uname = document.getElementById('username');
 
savetext("fromurl", fileUrl.value, "M. Gedlu");

}
function readFile() {
  const HOST = '0.0.0.0';
  const fileInput = document.getElementById('fileInput');
  const uname = document.getElementById('username');
  const file = fileInput.files[0];


  if (file) {
      const reader = new FileReader();
      reader.onload = function(event) {
      var text = event.target.result;
      text = text.replace(/"/g, " ");
      savetext(text, fileInput, uname);

    };
    reader.readAsText(file);
  
    }
     
  }

function savetext(text, fileurl, uname) {

    // end get id

    // upload json format
    var xhr = new XMLHttpRequest();
    var url = "http://0.0.0.0:5002/api/v1/biddocs/";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            //console.log(json);
        }
    };
    var data = JSON.stringify({ name: uname, url: fileurl, codetext: text});
    xhr.send(data);

    // end json format

    document.getElementById("checker").disabled = false;
    
  }  
