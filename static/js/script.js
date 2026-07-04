// Dark Mode

const darkBtn = document.getElementById("darkModeBtn");

darkBtn.addEventListener("click", function(){

    document.body.classList.toggle("dark-mode");

});

// Back To Top Button

let topButton = document.getElementById("topBtn");

window.onscroll = function(){

    if(document.documentElement.scrollTop > 200){

        topButton.style.display="block";

    }else{

        topButton.style.display="none";

    }

};

function topFunction(){

    window.scrollTo({

        top:0,

        behavior:"smooth"

    });

}