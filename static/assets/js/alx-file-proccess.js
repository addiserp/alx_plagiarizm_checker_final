
$(document).ready(function () {

  
  $('#checker').click(function () {
 
    $.get(`http://0.0.0.0:5002/api/v1/process/`, data => {
console.log(data.status);
      if (data.status == "OK") {
          
        $('.card-body-status .progress').disabled = false;
        $('div#maincontent main#main.main div h2.card-tit').append(data.result);
 


      } else {
        $('#result_status .graph').append(data.map(d => {
          return `<div class="progress mt-3">
          <div class="progress-bar progress-bar-striped bg-danger" role="progressbar" style="width: 10%" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
        </div>`

        }));
        $('#result_status h5').append(data.length);
       
        for (let i = 0; i < data.length; i++) {
          $('#my_list').append('<li>'+ data[i] + '</li>');
        }

      }
    });
      });

});
