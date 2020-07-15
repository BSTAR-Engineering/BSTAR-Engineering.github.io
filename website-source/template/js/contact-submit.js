
var $form = $('#contact-us-form'),
    url = 'https://script.google.com/macros/s/AKfycbyysD-n_5o2f-DHCr3K47Nzkt_NkALdKdVTubBEt0tYrCmuVYn7/exec'

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
