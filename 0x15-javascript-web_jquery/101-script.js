// Ensure the script runs after the DOM is fully loaded
$(document).ready(function() {
  // Add a new <li> item when the "Add item" div is clicked
  $('#add_item').click(function() {
    $('.my_list').append('<li>Item</li>');
  });

  // Remove the last <li> item when the "Remove item" div is clicked
  $('#remove_item').click(function() {
    $('.my_list li').last().remove();
  });

  // Clear all <li> items when the "Clear list" div is clicked
  $('#clear_list').click(function() {
    $('.my_list').empty();
  });
});
