var selected = new Array();

$(document).ready(function() {
	$(document).on('submit','form.question-form',function(){
	  $("input:radio:checked").each(function() {
	       selected.push($(this).val());
	  });
	});
});