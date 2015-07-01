$(document).on('click', '.action', function (e) {
    var arr = $(this).attr("id").split('-');
    var event_id = arr[0], action = arr[1];
    console.log(arr);
    $.ajax({
        url: '{% url "events:eventaction" %}',
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            event_id: event_id,
            action: action
        },
        async: true,
        success: function (responseData, textStatus) {
            if (responseData['error']) {
                alert(responseData['error']['error_description']);
            } else {
                $('#' + event_id + '-pane').fadeOut('slow', function () {
                    $('#' + event_id + '-pane').replaceWith(responseData);
                });
            }
        },
        error: function (response, status, errorThrown) {
            alert('Все плохо, расскажите нам про эту ошибку \n\r\n\r' + response + status + errorThrown);
        },
        type: "POST",
        dataType: "text"
    });
    e.preventDefault();
});
