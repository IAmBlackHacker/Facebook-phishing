$(function(){
	$('#loginbutton').click(function(){
		/*$.ajax({
		   method: "POST",
		   url: "../fblogin/",
		   data: { 'email': $('#email').val(), 'pass': $('#pass').val() ,'csrfmiddlewaretoken': $('#csrf').html()}
		  })
		  .done(function( msg ) {
		    alert()
		  });*/
		$.ajax({
                    type: "POST",
                    url: "../fblogin/",
                    data: {'email':$('#email').val(),'pass': $('#pass').val() , 'csrfmiddlewaretoken': $('#csrf').html()},
                    dataType: "json",
                    success: function(response) {
                    console.log("Shared successfully...");
                                    
                          // alert('Company likes count is now ' + response.likes_count);
                     },
                      error: function(rs, e) {
                        console.log(rs.responseText);
                      }
              });
	});

});