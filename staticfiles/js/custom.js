let responsiveBarParent = document.getElementById("responsive-bar-parent");
let navbarBarParent = document.getElementById("navbar-parent");

document.querySelector('.adds').addEventListener('click', function () {
    responsiveBarParent.classList.add("active")
    navbarBarParent.classList.add("active")
})
document.querySelector('.close').addEventListener('click', function () {
    responsiveBarParent.classList.remove("active")
    navbarBarParent.classList.remove("active")
})

var linkToggle = document.querySelectorAll('.dropdown-toggle');

for (i = 0; i < linkToggle.length; i++) {

    linkToggle[i].addEventListener('click', function (event) {

        event.preventDefault();

        var container = document.getElementById('dropdown-menu');
        container.classList.toggle("active");
        document.getElementById('category-nav-heading').classList.toggle('bb-0')
        this.classList.toggle('rotate_span')



    });

}


function getScrollMaxY() {
    "use strict";
    var innerh = window.innerHeight || ebody.clientHeight,
      yWithScroll = 0;
  
    if (window.innerHeight && window.scrollMaxY) {
      // Firefox 
      yWithScroll = window.innerHeight + window.scrollMaxY;
    } else if (document.body.scrollHeight > document.body.offsetHeight) {
      // all but Explorer Mac 
      yWithScroll = document.body.scrollHeight;
    } else {
      // works in Explorer 6 Strict, Mozilla (not FF) and Safari 
      yWithScroll = document.body.offsetHeight;
    }
    return yWithScroll - innerh;
  }
  
  function setEqualHeight() {
    let scrollAblepx = getScrollMaxY();
    // var maxscroll = window.scrollMaxY
    let innerWidth = window.innerWidth
    if(innerWidth<768){
      if (scrollAblepx < 105) {
        document.querySelector(".footer").classList.add("no_scroll");
      } else {
        document.querySelector(".footer").classList.remove("no_scroll");
      }
  
    }else{
      if (scrollAblepx < 5) {
        document.querySelector(".footer").classList.add("no_scroll");
      } else {
        document.querySelector(".footer").classList.remove("no_scroll");
      }
  
    }
    
  }
  setEqualHeight();
  window.onresize = setEqualHeight;



// var button = document.getElementById('save_btn');

// button.onclick = function () {

//     // this adds the 'active' class to the classes that the element already has
//     var maptab = document.getElementById('save_btn');

//     maptab.className = maptab.className + ' active';
// };

// var search = document.getElementById('searchbar');

// search.addEventListener('keyup', function (event) {
//     if (event.code === 'Enter') {
//         event.preventDefault();
//         document.querySelector('form').submit();
//     }
// });