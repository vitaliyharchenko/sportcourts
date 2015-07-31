/**
 * Created by vitaliyharchenko on 16.06.15.
 */
var pressed = false;
$(document).ready(function() {
    //inputfunc('email');
    clickfunc('email');
});

//function inputfunc (item) {
//    $(document).on('input','#'+item, function(){
//        if($(this).val() != '') {
//            var pattern = /^([a-z0-9_\.-])+@[a-z0-9-]+\.([a-z]{2,4}\.)?[a-z]{2,4}$/i;
//            if(pattern.test($(this).val())){
//                $(this).css({'border' : '1px solid #569b44'});
//                $('#'+item+'button').removeAttr('disabled');
//            } else {
//                $(this).css({'border' : '1px solid #ff0000'});
//                $('#'+item+'button').attr('disabled', 'disabled');
//            }
//        } else {
//            $(this).css({'border' : '1px solid #ff0000'});
//            $('#'+item+'button').attr('disabled', 'disabled');
//        };
//    });
//};

function clickfunc (item) {
    $(document).on('click','#'+item+'button', function(){
        var email = $('#'+item).val();
        var user_client = emailclient(email);
        console.log(email);
        console.log(user_client);
        if (!pressed) {
            $.ajax({
                url: "{% url 'add_email_activation' %}",
                data: {
                    csrfmiddlewaretoken:'{{ csrf_token }}',
                    email: email
                },
                async: true,
                beforeSend: function() {
                    pressed = true;
                    $('#'+item+'button').attr('disabled', 'disabled');
                    $('#'+item+'button').html('Отправка...');
                    $('#'+item).attr('disabled', 'disabled');
                },
                success: function (data, textStatus) {
                    if ('response' in data) {
                        $('#'+item+'button').html('Отправлено');
                        if (user_client[0]) {
                            $('#userclient').html('<p>Мы отправили вам письмо.</p><p>Пожалуйста, проверьте вашу почту</p><p><a href="'+user_client[1]+'" target="_blank">'+user_client[0]+'</a></p>');
                            console.log('Определили');
                        } else {
                            $('#userclient').html('<p class="lead">Сейчас на указанный Вами адрес <span class="text-primary">'+email+'</span> придет сообщение, содержащее ссылку для подтверждения email.<br><br>Пожалуйста, проверьте вашу почту.</p>');
                            console.log('Не');
                        };
                        $('#regModal').modal('hide');
                        $('#activateModal').modal('show');
                    } else {
                        var error = data['error'];
                        console.log(error);
                        var error_code = error['error_code'];
                        if (error_code == 1){
                            alert('Ошибка, пользовтель с таким email уже зарегестрирован!')
                            pressed = false;
                            $('#'+item+'button').removeAttr('disabled');
                            $('#'+item+'button').html('Присоединиться');
                            $('#'+item).removeAttr('disabled');
                        }
                        if (error_code == 2){
                            alert('Пользовтель с таким email уже активирован!')
                            pressed = false;
                            $('#'+item+'button').removeAttr('disabled');
                            $('#'+item+'button').html('Присоединиться');
                            $('#'+item).removeAttr('disabled');
                        }
                        if (error_code == 3){
                            alert('Ошибка, неверный email')
                            pressed = false;
                            $('#'+item+'button').removeAttr('disabled');
                            $('#'+item+'button').html('Присоединиться');
                            $('#'+item).removeAttr('disabled');
                        }
                    }
                },
                error: function (response, status, errorThrown) {
                    alert('Все плохо, расскажите нам про эту ошибку \n\r\n\r' + response + status + errorThrown);
                    $('#'+item+'button').html('Ошибка');
                },
                type: "POST",
                dataType: "json"
            });
        }
    });
};

function emailclient(item) {
    var arr = item.split('@');
    var client = arr[1];
    var result = [];
    switch (client) {
        case 'gmail.com':
            result[0] = 'Открыть Gmail';
            result[1] = 'https://mail.google.com/';
            break
        // case 'sportcourts.ru':
        //   result[0] = 'Открыть Gmail';
        //   result[1] = 'https://mail.google.com/';
        //   break
        case 'mail.ru':
            result[0] = 'Открыть Почту Mail.Ru';
            result[1] = 'https://e.mail.ru/';
            break
        case 'list.ru':
            result[0] = 'Открыть Почту Mail.Ru (list.ru)';
            result[1] = 'https://e.mail.ru/';
            break
        case 'inbox.ru':
            result[0] = 'Открыть Почту Mail.Ru (inbox.ru)';
            result[1] = 'https://e.mail.ru/';
            break
        case 'bk.ru':
            result[0] = 'Открыть Почту Mail.Ru (bk.ru)';
            result[1] = 'https://e.mail.ru/';
            break
        case 'yandex.ru':
            result[0] = 'Открыть Почту Yandex';
            result[1] = 'https://mail.yandex.ru/';
            break
        case 'ya.ru':
            result[0] = 'Открыть Почту Yandex';
            result[1] = 'https://mail.yandex.ru/';
            break
        case 'rambler.ru':
            result[0] = 'Открыть Почту Rambler';
            result[1] = 'https://mail.rambler.ru/';
            break
        case 'e1.ru':
            result[0] = 'Открыть Почту E1.ru';
            result[1] = 'https://mail.e1.ru/';
            break
        case 'icloud.com':
            result[0] = 'Открыть iCloud Mail';
            result[1] = 'https://www.icloud.com/';
            break
        case 'me.com':
            result[0] = 'Открыть iCloud Mail';
            result[1] = 'https://www.icloud.com/';
            break
        case 'yahoo.com':
            result[0] = 'Открыть Yahoo! Mail';
            result[1] = 'https://mail.yahoo.com/';
            break
        case 'live.ru':
            result[0] = 'Открыть Outlook.com (live.ru)';
            result[1] = 'https://mail.live.com/';
            break
        case 'live.com':
            result[0] = 'Открыть Outlook.com (live.com)';
            result[1] = 'https://mail.live.com/';
            break
        default:
    };
    return result;
}