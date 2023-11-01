$(document).ready(function() {
    console.log("working ok$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$x`")
    const monthNames = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ];
    

    $("#commentForm").submit(function(e) {
        e.preventDefault();

        let dt = new Date();
        let time = dt.getDay() + " "+ monthNames[dt.getUTCMonth()] + "," + dt.getUTCFullYear()

        $.ajax({
            data: $(this).serialize(),
            method: $(this).attr("method"),
            url: $(this).attr("action"),
            dataType: "json",
            success: function(response) {
                console.log("111111111222222222233333333333");
                if (response.bool === true) {
                    // Build the HTML structure as a string
                    let _html = '<li>' +
                        '<div class="people-box">' +
                        '<div>' +
                        '<div class="people-image">' +
                        '<img src="https://media.istockphoto.com/vectors/default-profile-picture-avatar-photo-placeholder-vector-illustration-vector-id1223671392?k=20&m=1223671392&s=170667a&w=0&h=kEAA35Eaz8k8A3qAGkuY8OZxpfvn9653gDjQwDHZGPE=" class="img-fluid blur-up lazyload" alt="">' +
                        '</div>' +
                        '</div>' +
                        '<div class="people-comment">' +
                        '<a class="name" href="javascript:void(0)">' + response.context.user + '</a>' +
                        '<div class="date-time">' +
                        '<h6 class="text-content">' + time + '</h6>' +
                        '<div class="product-rating">';

                    // Build the rating stars based on response.context.rating
                    // for (var i = 1; i <= response.context.rating; i++) {
                    //     _html += '<i class="fas fa-star text-warning"></i>';
                    // }

                    // Assuming response.context.rating is a number between 1 and 5
                    for (var i = 1; i <= 5; i++) {
                    // Use a ternary operator to add either a filled or empty star
                    _html += '<i class="fas fa-star ' + (i <= response.context.rating ? 'text-warning' : '') + '"></i>';
                    }

                    // Close the rating stars div and continue with HTML structure
                    _html += '</div>' +
                        '</div>' +
                        '<div class="reply">' +
                        '<p>' + response.context.review + ' <a href="javascript:void(0)">Reply</a></p>' +
                        '</div>' +
                        '</div>' +
                        '</div>' +
                        '</li>';

                    // Prepend the _html to an element with the id "review-list"
                    $("#review-list").prepend(_html);

                    // Optionally, hide the form
                    $("#hide-comment-form").hide();
                }
            },
            error: function(xhr, status, error) {
                console.error("AJAX Error:", status, error);
            }
        });
    });
});
