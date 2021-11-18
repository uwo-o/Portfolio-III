let square = document.getElementById('hero-square');
let image = document.getElementById('hero-image');
let menu_icon = document.getElementById('menu-icon');
let menu = document.getElementById('menu-options');
let flash = document.getElementById('flash-message');

//parallax effect with square with mouse movement
window.addEventListener('mousemove', moveImage);

function moveImage(e) {
    let x = e.clientX;
    let y = e.clientY;
    square.style.transform = `rotate(${x/75}deg)`;
    image.style.transform = `translateX(${y/100}px)`;
}

function toggleMenu(){
    menu.classList.toggle('open');
    menu_icon.classList.toggle('open');
}

function closeMessage(){
    flash.style.display = 'none';
}
