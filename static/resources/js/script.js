// For Client-Details
$(document).ready(function(){
    $('.client-profile').click(function(){
        $('.client-panels').toggle();
    });
;})


// For Sticky Navigation 

$(document).ready(function() {

    $('.js--section-steps').waypoint(function(direction) {
        if(direction == "down")  {
            $('nav').addClass('sticky');
        } else {
            $('nav').removeClass('sticky')
        }
    } , {
        offset: '50px'
    }) ;

    /*
    var waypoints = $('#handler-first').waypoint(function(direction) {
        notify(this.element.id + ' hit 25% from top of window') 
      }, {
        offset: '25%'
      })
    */
});

/* -- mobile-nav -- */

$('.js--nav-icon').click(function() {
    var nav = $('.js--main-nav');
    var icon = $('js--nav-icon');

    
    nav.slideToggle(200)     /* 200mili second  */
    if(icon.hasClass('menu-icon')) {
        icon.addClass('cross-icon')
        icon.removeClass('ion-class-icon')
    } else {
        icon.addClass('menu-icon')
        icon.removeClass('cross-icon')
    }

})


// Select Price Category

function chooseGentleman(){
    var priceCategory = document.querySelector('.category');
    priceCategory.innerHTML = "GENTLEMAN"

    document.querySelector('.Gentleman').style.display = 'block' 
    document.querySelector('.Ladies').style.display = 'none' 
    document.querySelector('.Ladies').style.display = 'none' 
    document.querySelector('.Ladies').style.display = 'none' 
    document.querySelector('.Home').style.display = 'none' 
}

function chooseLadies(){
    var priceCategory = document.querySelector('.category');
    priceCategory.innerHTML = "LADIES"

    document.querySelector('.Gentleman').style.display = 'none' 
    document.querySelector('.Ladies').style.display = 'block' 
    document.querySelector('.Babies').style.display = 'none' 
    document.querySelector('.Unisex').style.display = 'none' 
    document.querySelector('.Home').style.display = 'none' 
}
function chooseBabies(){
    var priceCategory = document.querySelector('.category');
    priceCategory.innerHTML = "BABIES"

    document.querySelector('.Gentleman').style.display = 'none' 
    document.querySelector('.Ladies').style.display = 'none' 
    document.querySelector('.Babies').style.display = 'block' 
    document.querySelector('.Unisex').style.display = 'none' 
    document.querySelector('.Home').style.display = 'none' 
}
function chooseUnisex(){
    var priceCategory = document.querySelector('.category');
    priceCategory.innerHTML = "UNISEX"

    document.querySelector('.Gentleman').style.display = 'none' 
    document.querySelector('.Ladies').style.display = 'none' 
    document.querySelector('.Babies').style.display = 'none' 
    document.querySelector('.Unisex').style.display = 'block' 
    document.querySelector('.Home').style.display = 'none' 

}
function choosehome(){
    var priceCategory = document.querySelector('.category');
    priceCategory.innerHTML = "HOME APPLIANCE"

    document.querySelector('.Gentleman').style.display = 'none' 
    document.querySelector('.Ladies').style.display = 'none' 
    document.querySelector('.Babies').style.display = 'none' 
    document.querySelector('.Unisex').style.display = 'none' 
    document.querySelector('.Home').style.display = 'block' 
}

// For hide and show of sign in and sign up

$(document).ready(function(){
    
    $('.signin').click(function(){
        $('.section-signin').show()
        $('.section-signup').hide()
    });

    $('.signup').click(function(){
        $('.section-signup').show()
        $('.section-signin').hide()
    });
})

document.querySelector('#signin').addEventListener('click',function(){
    var username = document.querySelector('#username')
    var password = document.querySelector('#password')
    if (username.value === ' ' || username.value == null){
        document.getElementById('usernameError').innerHTML = ' Username is required '
    }
    if (password.value === ' ' || password.value == null){
        document.getElementById('passwordError').innerHTML = ' Password is required '
    }
    document.querySelector('.loginError').style.display = "block";
})

document.querySelector('#signupButton').addEventListener('click',function(){
    const success = document.querySelector('');
})