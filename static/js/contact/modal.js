$(document).ready(function(){
    $('.receive').click(function(){
        $('#receive_box').show();
        $('#send_box').hide();
    });

    $('.send').click(function(){
        $('#receive_box').hide();
        $('#send_box').show();
    });

    $('.back_btn').click(function(){
        $('#receive_box').show();
        $('#send_box').hide();
        $('#send_mail').hide();
    });

    $('.summary_list2').click(function(){
        var temp = $(this).children('.content_list');
        if(temp.css("display")=="none"){
            temp.show();
        }else{
            temp.hide();
        }
    });
});
