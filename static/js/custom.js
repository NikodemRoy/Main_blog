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

