let newsTab = document.querySelectorAll('.news-category li');
let newsDetail = document.querySelectorAll('.news-detail')

// 탭 초기화
function initNews(){
    for(i=0;i<newsDetail.length;i++){
        newsDetail[i].style.display = 'none';
    };
    newsDetail[0].style.display = 'flex';
}
initNews()


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
    // 클릭한 탭은 active클래스 추가
    this.classList.add('active');
}

// 콜백 : 뉴스 카테고리 클릭시 newsTapClick함수 호출
for(i=0;i<newsTab.length;i++){
    newsTab[i].addEventListener('click', newsTapClick)
}

let appCategory = document.querySelectorAll('.search-category h4');
let appDetail = document.querySelectorAll('.list_wrapper ul');

// 탭 초기화
function initApp(){
    for(i=0;i<appDetail.length;i++){
        appDetail[i].style.display = 'none';
    };
    appDetail[0].style.display = 'flex';
}
initApp()

function appClick(e){
    //reset all tabs
    for(i=0;i<appDetail.length;i++){
        appDetail[i].style.display = 'none';
    };
    //클릭한 탭의 index 산출해서 같은 index값을 가진 탭 display flex적용
    for(i=0;i<appCategory.length;i++){
        if(appCategory[i] === this){
            if(i === 0){
                appDetail[i].style.display = 'flex';
            }else{
                appDetail[i].style.display = 'grid';
            }
        };
        console.log(i)
    };
    // Add .active on clicked category
    for(i=0;i<appCategory.length;i++){
        appCategory[i].classList.remove('active');
    };
    // 클릭한 탭은 active클래스 추가
    this.classList.add('active');
}
for(i=0;i<appCategory.length;i++){
    appCategory[i].addEventListener('click', appClick)
}