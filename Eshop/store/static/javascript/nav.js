const toggleButton = document.getElementsByClassName('toggle')[0];

const navItems = document.getElementsByClassName('nav_items')[0];

toggleButton.addEventListener('click', () => {
    navItems.classList.toggle('active')
})