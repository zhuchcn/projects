// The sidebar menu of mkdocs is a little crazy. Instead of create each separate sidebar menu for each top navbar item, it renders a whole sidebar menu, and sets the list items that do not belong to the current top navbar item as "visibility: hidden". So I have to change the format according to the router url
if(window.innerWidth > 1341){
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
} else {
    const items = document.querySelectorAll(".md-sidebar--primary li.md-nav__item--nested .fa")
    for(i=0; i<items.length; i++){
        items[i].className = 'fa fa-caret-right'
    }
}

// get year for footer
const date = new Date()
const year = date.getFullYear()
const footer = document.querySelector(".md-footer-copyright__highlight")
console.log(footer.innerText)
footer.innerText = footer.innerText.replace('$YEAR', year)