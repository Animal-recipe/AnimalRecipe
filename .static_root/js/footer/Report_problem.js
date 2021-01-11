$(document).ready(function(){
    $('.list').click(function(){
        $('.noncheck_box').show();
        $('.check_box').hide();
        $(this).children('.noncheck_box').hide();
        $(this).children('.check_box').show();
    })
});
