$(document).ready(function() {
  // Set up the click event handler for the "Translate" button
  $('#btn_translate').click(function() {
    // Get the language code from the input field
    const languageCode = $('#language_code').val();
    
    // Construct the URL for the API request
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
    
    // Make an AJAX GET request to the API
    $.get(url, function(data) {
      // Update the #hello div with the translated "Hello"
      $('#hello').text(data.hello);
    }).fail(function() {
      // Handle the error if the API request fails
      $('#hello').text('Error: Unable to fetch translation');
    });
  });
});
