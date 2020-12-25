$(document).ready(function(){
    $('.receive').click(function(){
        $('#receive_box').show();
        $('#send_box').hide();
    });

    $('.send').click(function(){
        $('#receive_box').hide();
        $('#send_box').show();
    });

    $('.send_mail_btn').click(function(){
        $('#receive_box').hide();
        $('#send_box').hide();
        $('#send_mail').show();
    });
    $('.back_btn').click(function(){
        $('#receive_box').show();
        $('#send_box').hide();
        $('#send_mail').hide();
    });
});

