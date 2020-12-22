$(document).ready(function(){
    $('.animal .radio_box').click(function(){
        $('.animal .radio_box').css("background-color", "#FFFFFF");
        $('.animal .radio_box').css("color", "#575757");
        $(this).css("background-color", "#FF6B00");
        $(this).css("color","#FFFFFF");
    })

    $('#star1').click(function(){
        $('#img1').attr("src", "{% static 'img/review/review_create/fill_star.png' %}");
        $('#img2').attr("src", "{% static 'img/review/review_create/empty_star.png' %}");
        $('#img3').attr("src", "{% static 'img/review/review_create/empty_star.png' %}");
        $('#img4').attr("src", "{% static 'img/review/review_create/empty_star.png' %}");
        $('#img5').attr("src", "{% static 'img/review/review_create/empty_star.png' %}");
    })

    $('.cook .radio_box').click(function(){
        $('.cook .radio_box').css("background-color", "#FFFFFF");
        $('.cook .radio_box').css("color", "#575757");
        $(this).css("background-color", "#FF6B00");
        $(this).css("color","#FFFFFF");
    })

    $('.level .radio_box').click(function(){
        $('.level .radio_box').css("background-color", "#FFFFFF");
        $('.level .radio_box').css("color", "#575757");
        $(this).css("background-color", "#FF6B00");
        $(this).css("color","#FFFFFF");
    })

    $('.input_box2').hide();
    $('.input_box3').hide();
    $('.input_box2').first().show();
    $('.input_box3').first().show();

    var number = 1;
    $('#click_box').click(function(){
        $('.input_box2').eq(number).show();
        $('.input_box3').eq(number).show();
        number += 1;
    })
});
