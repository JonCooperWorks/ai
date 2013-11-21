$(document).ready(function() {

	$( "input.next" ).click(function() {
	  if (curSlide < slideEls.length - 1) {
	    curSlide++;

	    updateSlides();
	  }
	});

});