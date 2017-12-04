
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
		$('#upload-file-btn').click(function() {
			var form_data = new FormData($('#upload-file')[0]);
			$.ajax({
				type: 'POST',
				url: '/image',
				data: form_data,
				contentType: false,
				cache: false,
				processData: false,
				async: false,
				success: function(data) {
					console.log('Success!');
				},
			});
		});
			$('.skillbar').each(function() {
				$(this).find('.skillbar-bar').animate({
					width: $(this).attr('data-percent')
				}, 3000);
			});
			
		})
	
		
		
	});