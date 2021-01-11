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
    });

    $('.nontext').hide();
    $('.input_box4').hide();
    $('p label').hide();

    for(var i=0; i<1; i++){
        var temp = i+1;
        $('.nontext').eq(i).val('step '+temp);
        $('.nontext').eq(i).show();
        $('.input_box4').eq(i).show();
        $('.img_show2').eq(i).show();
    }

    var j = 1;
    $('#add_block_btn').click(function(){
        if(j < 11){
            var temp = j+1;
            $('.nontext').eq(j).val('step '+temp);
            $('.nontext').eq(j).show();
            $('.input_box4').eq(j).show();
            $('.img_show2').eq(j).show();
            j += 1;
        }
    });
    if($('ul').hasClass("errorlist")){
        $('.errorlist').hide();
        alert("조리방법 내용은 "+$('.errorlist').text());
        $('.input_box4').focus();
    }
});
