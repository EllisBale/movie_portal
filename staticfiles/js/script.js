
// DOM Elements

const buttonToTop = document.getElementById(
    "btn-to-top" // Back to top button
); 

const posterHover = document.querySelectorAll(
    '.card-poster-hover' // Poster hover
);


// Back to top function
buttonToTop.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth"  }) 
})


// Hover effect for poster
posterHover.forEach(poster => {
    poster.addEventListener('mouseenter', () => {
        posterHover.forEach(other => {
            if (other !== poster) {
                other.classList.add('inactive');
            }
        });
    });

    poster.addEventListener('mouseleave', () => {
        posterHover.forEach(other => {
            other.classList.remove('inactive');
        });
    });

});