
// DOM Elements

const buttonToTop = document.getElementById(
    "btn-to-top" // Back to top button
); 

const posterHover = document.querySelectorAll(
    '.card-poster-hover' // Poster hover
);


// Book_seats.html

const bookSeatForm = document.getElementById(
    "book_seats_form" // Book seats form
);

const seatCheckBox = document.querySelectorAll(
    ".seat-checkbox" // Book seats checkbox
);


// Delete button warning

const deleteBtns = document.querySelectorAll(
    ".delete-button" // Delete button
);


// Back to top function
buttonToTop?.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth"  }) 
});


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


// Checks if seat has been selected before booking

bookSeatForm?.addEventListener("submit", (event) => {
    
    const seatCheckBox = document.querySelectorAll(".seat-checkbox:checked");

    if (seatCheckBox.length === 0) {
        event.preventDefault();
        alert(" Select at least one seat to book.")
    }
})

deleteBtns.forEach(deleteBtn => {
    deleteBtn.addEventListener("click", event => {
        if (!confirm("Are you sure you want to delete this?")) {
            event.preventDefault(); 
        }
    });
});

