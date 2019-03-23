if(window.location.pathname.search("post") === -1){
    const menuItems = document.querySelectorAll(".md-sidebar--primary ul.md-nav__list + li.md-nav__item--nested")
    for(i=0; i<menuItems.length; i++){
        menuItems[i].style.display = "none"
    }
} else {
    const items = document.querySelector(".md-sidebar--primary ul.md-nav__list").children
    for(i=0; i < items.length; i++){
        if(items[i].classList.contains("md-nav__item--active") !== true){
            items[i].style.display = "none"
        } else {
            const fas = items[i].querySelectorAll("i.fa")
            for(j=0; j < fas.length; j++){
                fas[j].className = 'fa fa-caret-right' 
            }
        }
    }
}