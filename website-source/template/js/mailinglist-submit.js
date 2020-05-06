
var $form = $('#mailinglist-form'),
    url = 'https://script.google.com/macros/s/AKfycbzxl87awQS8UvzVuPMWGzXdWnFa4pRqh5vY7m05kDSHgKDH1Svf/exec'

$('#submit-form').on('click', function(e) {
  e.preventDefault();
  var jqxhr = $.ajax({
    url: url,
    method: "GET",
    dataType: "json",
    data: $form.serialize(),
    success: function(data){
      if (data['result']=='success'){
        $("#submit-form").css("background-color","#444");
        $("#submit-form").val("✓");
      }
     }

  });
})
