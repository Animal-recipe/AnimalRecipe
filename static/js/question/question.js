$(document).ready(function(){

    const item = document.getElementById('trigger');
    const content = document.getElementById('triggerContentBox');
    function openClose() {
        if(content.style.display === 'block') {
            content.style.display = 'none';
            document.getElementById(this.id).textContent = '상세보기';
        } else {
            content.style.display = 'block';
            document.getElementById(this.id).textContent = '접기';
        }
    }
    item.addEventListener('click', openClose);
});
