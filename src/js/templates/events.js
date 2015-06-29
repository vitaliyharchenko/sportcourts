$(document).on('click', '.action', function () {
    var arr = $(this).attr("id").split('-');
    var game_id = arr[0], action = arr[1];
    $.ajax({
        url: 'events/actions/games/' + action + '/' + game_id,
        data: {
            tab_name: pane
        },
        async: true,
        success: function (responseData, textStatus) {
            $('#gamepane-' + game_id + '-' + pane).fadeOut('slow', function () {
                $('#gamepane-' + game_id + '-all').replaceWith(responseData);
                $('#gamepane-' + game_id + '-my').replaceWith(responseData);
            });
        },
        error: function (response, status, errorThrown) {
            alert('Все плохо, расскажите нам про эту ошибку \n\r\n\r' + response + status + errorThrown);
        },
        type: "GET",
        dataType: "text"
    });
});