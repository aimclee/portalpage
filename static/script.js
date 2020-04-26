let newsTab = document.querySelectorAll('.news-category li');
let newsDetail = document.querySelectorAll('.news-detail')
let newsLine = document.querySelectorAll('.news-line')
let newsItem = document.querySelectorAll('.news-imageNews')
let shoppingCategory = document.querySelectorAll('.shopping-category li')
let shoppingItems = document.querySelectorAll('.shopping-item ul')

// 탭 초기화
function initNews(){
    for(i=0;i<newsDetail.length;i++){
        newsDetail[i].style.display = 'none';
    };
    newsDetail[0].style.display = 'flex';
    //랜덤 수 2개 생성 (1~12)
    rand = Math.floor(Math.random() * 12);
    rand2 = Math.floor(Math.random() * 12);
    //시작페이지 2개 클래스 변경
    childNode = newsLine[0].children;
    childNode[rand].classList.add('desc');
    childNode[rand2].classList.add('desc');
}
initNews()

function newsTapClick(e){
    //reset all tabs
    for(i=0;i<newsDetail.length;i++){
        newsDetail[i].style.display = 'none';
    };
    //reset all class
    for(i=0;i<newsItem.length;i++){
        newsItem[i].classList.remove('desc');
    }
    //랜덤 수 생성 (1~12)
    rand = Math.floor(Math.random() * 12);
    rand2 = Math.floor(Math.random() * 12);
    
    //클릭한 탭의 index 산출해서 같은 index값을 가진 탭 display flex적용
    for(i=0;i<newsTab.length;i++){
        if(newsTab[i] === this){
            newsDetail[i].style.display = 'flex';
            childNode = newsLine[i].children;
            childNode[rand].classList.add('desc');
            childNode[rand2].classList.add('desc');
        };
    };
    // Add .active on clicked category
    for(i=0;i<newsTab.length;i++){
        newsTab[i].classList.remove('active');
    };
    // 클릭한 탭은 active클래스 추가
    this.classList.add('active');
}


function shoppingTabClick(e){
    //reset all tabs
    for(i=0;i<shoppingItems.length;i++){
        shoppingItems[i].style.display = 'none';
    };
    //클릭한 탭의 index 산출해서 같은 index값을 가진 탭 display flex적용
    for(i=0;i<shoppingCategory.length;i++){
        if(shoppingCategory[i] === this){
            shoppingItems[i].style.display = 'grid';
        };
    };
    // Add .active on clicked category
    for(i=0;i<shoppingCategory.length;i++){
        shoppingCategory[i].classList.remove('active');
    };
    // 클릭한 탭은 active클래스 추가
    this.classList.add('active');
}

// 콜백 : 뉴스 카테고리 클릭시 newsTapClick함수 호출
for(i=0;i<newsTab.length;i++){
    newsTab[i].addEventListener('click', newsTapClick)
}
for(i=0;i<newsTab.length;i++){
    shoppingCategory[i].addEventListener('click', shoppingTabClick)
}