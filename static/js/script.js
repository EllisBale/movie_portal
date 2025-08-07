
// DOM Elements

const buttonToTop = document.getElementById(
    "btn-to-top" // Back to top button
); 



// Back to top function
buttonToTop.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth"  }) 
})