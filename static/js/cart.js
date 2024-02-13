// cart.js

$(document).ready(function() {
    // Listen for the "Add to Cart" link click event
    $('a.add-to-cart-link').on('click', function(event) {
        event.preventDefault();
        var link = $(this);
        var productId = link.data('dishes-id');

        // Get the CSRF token from the hidden input field
        var csrfToken = $('input[name=csrfmiddlewaretoken]').val();

        // Send an AJAX request to add the dishes to the cart
        $.ajax({
            type: 'POST',
            url: link.attr('href'),
            data: {
                product_id: productId,
            },
            headers: {
                "X-CSRFToken": csrfToken
            },
            success: function(response) {
                // Update the cart count in the <sup> tag
                $('#cart-count').text(response.cart_count);
            },
            error: function() {
                alert('An error occurred. Please try again.');
            }
        });
    });
});
