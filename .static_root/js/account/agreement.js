$(document).ready(function(){

    const items = document.querySelectorAll('.trigger');
    function openClose() {
        const contentID = this.id.replace('trigger', 'content');

        if(document.getElementById(contentID).style.display === 'block') {
            document.getElementById(contentID).style.display = 'none';
            document.getElementById(this.id).textContent = '상세보기';
        } else {
            document.getElementById(contentID).style.display = 'block';
            document.getElementById(this.id).textContent = '접기';
        }
    }
    items.forEach(item => item.addEventListener('click', openClose));

    $('#customCheckAll').click(function(){
        if($("#customCheckAll").prop("checked")){
            $("input[type=checkbox]").prop("checked", true);
            $('#nextButton').prop('disabled', false);
            $('#nextButton').css('background-color', '#FF5C00');
        } else {
            $("input[type=checkbox]").prop("checked", false);
            $('#nextButton').prop('disabled', true);
            $('#nextButton').css('background-color', '#5f5f5f');
        }
    })

    var allCnt = $(".checkItem").length;
    $(".checkItem").click(function(){
        var checkedCnt = $(".checkItem").filter(":checked").length;
        if( allCnt==checkedCnt ){
            $("#customCheckAll").prop("checked", true);
            $('#nextButton').prop('disabled', false);
            $('#nextButton').css('background-color', '#FF5C00');
        }
        else{
            $("#customCheckAll").prop("checked", false);
            $('#nextButton').prop('disabled', true);
            $('#nextButton').css('background-color', '#5f5f5f');
        }
    })
});
