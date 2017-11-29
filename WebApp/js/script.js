
$(document).ready(function() {

	$('.skillbar').each(function() {
	        $(this).find('.skillbar-bar').animate({
	            width: $(this).attr('data-percent')
	        }, 3000);
	});


	$("input").change(function(){

		var reader = new FileReader();
		reader.onload = function(){
			$('#output').attr('src', reader.result);

			var filename = $('input[type=file]').val().replace(/C:\\fakepath\\/i, '')
		};
		reader.readAsDataURL(event.target.files[0]);


		$('.skillbar1').attr('data-percent', '60%');
		$('.skillbar2').attr('data-percent', '80%');
		$('.skillbar3').attr('data-percent', '50%');
		$('.skillbar4').attr('data-percent', '10%');
		$('.skillbar5').attr('data-percent', '90%');
		$('.skillbar6').attr('data-percent', '20%');

		$('.skillbar').each(function() {
	        $(this).find('.skillbar-bar').animate({
	            width: $(this).attr('data-percent')
	        }, 3000);
		});
		
	})

	
	
});
