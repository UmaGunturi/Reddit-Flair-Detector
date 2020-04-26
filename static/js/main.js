// 

$(document).ready(function () {

    $('#sub-post').on('submit', function (event) {
        $('#prl').show();
        $('#show-flair').hide();
        $.ajax({
            data: {
                post: $("#reddit-post").val(),
            },
            type: "POST",
            url: '/data'
        })
            .done(function (data) {
                if (data.error) {
                    $('#prl').hide();
                    $('#show-flair').text(data.error);
                    $('#show-flair').show();
                }
                else {
                    $('#prl').hide();
                    $('#show-flair').text(data.flair);
                    $('#show-flair').show();
                }

            });

        event.preventDefault();
    });
});
