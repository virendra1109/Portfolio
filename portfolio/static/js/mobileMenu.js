// Mobile menu functionality
document.addEventListener('DOMContentLoaded', function() {
    // Add the menu icon to the header
    const header = document.querySelector('.header');
    const navbar = document.querySelector('.navbar');
    
    // Create the menu icon element
    const menuIcon = document.createElement('div');
    menuIcon.classList.add('menu-icon');
    menuIcon.innerHTML = '<i class="bx bx-menu"></i>';
    
    // Insert the menu icon before the navbar
    header.insertBefore(menuIcon, navbar);
    
    // Toggle the navigation menu on click
    menuIcon.addEventListener('click', function() {
        navbar.classList.toggle('active');
        
        // Change the icon when menu is open/closed
        const icon = menuIcon.querySelector('i');
        if(navbar.classList.contains('active')) {
            icon.classList.remove('bx-menu');
            icon.classList.add('bx-x');
        } else {
            icon.classList.remove('bx-x');
            icon.classList.add('bx-menu');
        }
    });
    
    // Close menu when clicking on a menu item
    const navLinks = document.querySelectorAll('.navbar a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navbar.classList.remove('active');
            const icon = menuIcon.querySelector('i');
            icon.classList.remove('bx-x');
            icon.classList.add('bx-menu');
        });
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!event.target.closest('.navbar') && !event.target.closest('.menu-icon')) {
            navbar.classList.remove('active');
            const icon = menuIcon.querySelector('i');
            icon.classList.remove('bx-x');
            icon.classList.add('bx-menu');
        }
    });
});
