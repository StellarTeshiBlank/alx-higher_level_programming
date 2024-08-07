// Wait for the document to be fully loaded
$(document).ready(function() {
  // Set up a click event handler for the div with id 'toggle_header'
  $('#toggle_header').on('click', function() {
    // Check the current class of the header element
    if ($('header').hasClass('red')) {
      // If the header has class 'red', remove 'red' and add 'green'
      $('header').removeClass('red').addClass('green');
    } else {
      // Otherwise, remove 'green' and add 'red'
      $('header').removeClass('green').addClass('red');
    }
  });
});
