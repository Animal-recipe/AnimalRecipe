$(document).ready(function(){
    $.noConflict();
    $('.image_list').slick({
          dots: true, // 하단 paging버튼 노출 여부
          infinite: true, // 양방향 무한 모션
          speed: 300, // 모션 스피드
          cssEase: 'linear' //css easing 모션 함수
    });
    $('.create_recomment').click(function(){
        $(this).closest("div").next().show();
    });
    $(".change_disable").click(function(){
        $('.user_comment_box').removeAttr('disabled');
    });

});
