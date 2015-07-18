$(document).ready(function () {
    $('.notifications .alert').each(function () {
        $(this).fadeIn('slow');
    });
    setTimeout(function(){
        $('.notifications .alert').each(function () {
            $(this).fadeOut('slow');
        });
        //TODO: here we read all the notifications
    }, 6000);
});