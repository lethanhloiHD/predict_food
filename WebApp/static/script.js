
$(document).ready(function() {
	
		$('.skillbar').each(function() {
				$(this).find('.skillbar-bar').animate({
					width: $(this).attr('data-percent')
				}, 3000);
		});
	
	
		$("input").change(function(){
	
			var reader = new FileReader();
			var filename = "";
	
			reader.onload = function(){
				$('#output').attr('src', reader.result);
	
				filename = $('input[type=file]').val().replace(/C:\\fakepath\\/i, '');
				$('#name-food').text(filename);
			};
	
			reader.readAsDataURL(event.target.files[0]);
	
			$.ajax({
				url : "https://127.0.0.1:5000/image",
				type : "POST",
				dataType: 'json', // du lieu tra ve dang json
				data : JSON.stringify({'image':filename}),
				success : function (result){
						$('.skillbar1').attr('data-percent', '60%');
						$('.skillbar2').attr('data-percent', '80%');
						$('.skillbar3').attr('data-percent', '50%');
						$('.skillbar4').attr('data-percent', '10%');
						$('.skillbar5').attr('data-percent', '90%');
						$('.skillbar6').attr('data-percent', '20%');
				}
			});
			$('.skillbar').each(function() {
				$(this).find('.skillbar-bar').animate({
					width: $(this).attr('data-percent')
				}, 3000);
			});
			
		})
	
		
		
	});