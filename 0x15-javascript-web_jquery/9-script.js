// Use jQuery to ensure the DOM is fully loaded
$(document).ready(function() {
  // Define the URL to fetch data from
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  
  // Perform an AJAX GET request to the specified URL
  $.get(url, function(data) {
    // Extract the 'hello' value from the response
    const helloText = data.hello;
    
    // Set the text of the div with id 'hello' to the fetched 'hello' value
    $('#hello').text(helloText);
  });
});
