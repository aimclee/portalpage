let newsTab = document.querySelectorAll('.news-category li');
let newsDetail = document.querySelectorAll('.news-detail')
console.log(newsDetail)
console.log(newsDetail[0])
console.log(newsDetail[1])
console.log(newsDetail.length)

// 탭 초기화
function inintializing(){
    for(i=0;i<newsDetail.length;i++){
        newsDetail[i].style.display = 'none';
    };
    newsDetail[0].style.display = 'flex';
}
inintializing()


function newsTapClick(e){
    //reset all tabs
    for(i=0;i<newsDetail.length;i++){
        newsDetail[i].style.display = 'none';
    };
    
    //클릭한 탭의 index 산출해서 같은 index값을 가진 탭 display flex적용
    for(i=0;i<newsTab.length;i++){
        if(newsTab[i] === this){
            console.log(this)
            newsDetail[i].style.display = 'flex';
        };
        console.log(i)
    };
    
    // Add .active on clicked category
    for(i=0;i<newsTab.length;i++){
        newsTab[i].classList.remove('active');
    };

    this.classList.add('active');
    
}

for(i=0;i<newsTab.length;i++){
    newsTab[i].addEventListener('click', newsTapClick)
}
