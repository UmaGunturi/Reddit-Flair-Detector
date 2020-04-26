
$(document).ready(function () {

    $('#sub-post').on('submit', function (event) {
        $.ajax({
            data: {
                post: $("#reddit-post").val(),
            },
            type: "POST",
            url: '/data'
        })
            .done(function (data) {

                document.getElementById('show-flair').innerText = data.flair;

            });

        event.preventDefault();
    });
});

