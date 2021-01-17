$(document).ready(function(){
    $.noConflict();
    $('.image_list').slick({
          dots: true, // 하단 paging버튼 노출 여부
          infinite: true, // 양방향 무한 모션
          speed: 300, // 모션 스피드
          cssEase: 'linear', //css easing 모션 함수
          autoplay: true,
          autoplaySpeed: 5000,
          prevArrow: null,
          nextArrow: null,
    });
    $(".page-link").on('click', function () {
        $("#page").val($(this).data("page"));
        $(".searchBarBox").submit();
    });
    $("#searchBtn").on('click', function () {
        $("#q").val($(".q").val());
        $("#page").val(1);
        $(".searchBarBox").submit();
    });
    $(".petkind").on('change', function() {
        $("#petkind").val($(this).val());
        $("#cooking_time").val($(".cooking_time").val());
        $("#order").val($(".order").val());
        $("#page").val(1);
        $(".searchBarBox").submit();
    });
    $(".cooking_time").on('change', function() {
        $("#petkind").val($(".petkind").val());
        $("#cooking_time").val($(this).val());
        $("#order").val($(".order").val());
        $("#page").val(1);
        $(".searchBarBox").submit();
    });
    $(".order").on('change', function() {
        $("#petkind").val($(".petkind").val());
        $("#cooking_time").val($(".cooking_time").val());
        $("#order").val($(this).val());
        $("#page").val(1);
        $(".searchBarBox").submit();
    });
});
