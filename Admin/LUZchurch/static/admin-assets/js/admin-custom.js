
/* ADD CHURCH MOTO API CALL  */
function add_church_moto(church_moto_json) {
    $.ajax({
        url: "/luz-admin/church-moto/", 
        type: "POST",
        dataType: "json",
        headers: {"X-CSRFToken": getCookie('csrftoken')},
        data: church_moto_json,
        success: function (result) {
           var message = result['message'];
           $('#success-alert').text(result['message']);
           $('.success_alert_show').show("slow").delay(5000).hide("slow"); 
         },
         error: function (err) {

           $('.error_alert_show').show("slow").delay(5000).hide("slow"); 
           console.log("error");
         }
      });
    }



/* ADD CHURCH OFFICE DETAILS AND HISTORY API  */

function add_office_history_moto(church_office_history_json) {
  $.ajax({
      url: "/luz-admin/church-office-history/", 
      type: "POST",
      dataType: "json",
      headers: {"X-CSRFToken": getCookie('csrftoken')},
      // contentType: "application/json; charset=utf-8",
      data: church_office_history_json,
      success: function (result) {
         var message = result['message'];
         $('#success-alert').text(result['message']);
         $('.success_alert_show').show("slow").delay(5000).hide("slow"); 
       },
       error: function (err) {

         $('.error_alert_show').show("slow").delay(5000).hide("slow"); 
         console.log("error");
       }
    });
  }