// side navigation bar
function toggleSidebar(){
    document.getElementById("side-nav").classList.toggle('toggle-active');
    document.getElementById("main").classList.toggle('toggle-active');
    document.getElementById("top-navbar").classList.toggle('toggle-active');
}

// popup for messages or student grade
var g = 0;
function pop(){
    if(g == 0){
        document.getElementById("grade-box").style.display = "none";
        g = 1;
    }else{
        document.getElementById("grade-box").style.display = "block";
        g = 0;
    }
}

var a = 0;
function assesment_pop(){
    if(a == 0){
        document.getElementById("assesment-box").style.display = "none";
        a = 1;
    }else if(a == 1){
        document.getElementById("assesment-box").style.display = "block";
        a = 0;
    }
}

// extend and collapse
function showCourses(btn) {
    var btn = $(btn);

    if (collapsed) {
        btn.html("Collapse <i class=\"fas fa-angle-up\"></i>");
        $(".hide").css("max-height", "unset");
        $(".white-shadow").css({"background": "unset", "z-index": "0"});
    } else {
        btn.html("Expand <i class=\"fas fa-angle-down\"></i>");
        $(".hide").css("max-height", "150");
        $(".white-shadow").css({"background": "linear-gradient(transparent 50%, rgba(255,255,255,.8) 80%)", "z-index": "2"});
    }
    collapsed = !collapsed;
}

// img darken
const productItems = document.querySelectorAll('.img-wrapper')

productItems.forEach(product => {
    product.addEventListener('mouseover', () => {
        product.childNodes[1].classList.add('img-darken')
    })
    product.addEventListener('mouseout', () => {
        product.childNodes[1].classList.remove('img-darken')
    })
});
