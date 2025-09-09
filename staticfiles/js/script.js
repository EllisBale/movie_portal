

/* ===== DOM Elements ===== */
const buttonToTop = document.getElementById("btn-to-top"); // Back to top button
const posterHover = document.querySelectorAll(".card-poster-hover"); // Poster hover
const bookSeatForm = document.getElementById("book_seats_form"); // Book seats form
const deleteBtns = document.querySelectorAll(".delete-button"); // Delete button
const customModal = document.getElementById("customModal"); // Modal
const customModalBody = document.getElementById("customModalBody"); // Modal body
const customModalClose = document.getElementById("customModalClose"); // Modal close


/* ===== Back to Top ===== */
buttonToTop?.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
});


/* ===== Poster Hover Effect ===== */
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


/* ===== Seat Booking Validation ===== */
bookSeatForm?.addEventListener("submit", (event) => {

    const selectedSeats = document.querySelectorAll(".seat-checkbox:checked");
    event.preventDefault();

    if (selectedSeats.length === 0) {
        customModalBody.textContent = "Select at least one seat to book.";
        customModal.style.display = "flex";
    
    } else if (selectedSeats.length > 8) {
        customModalBody.textContent = "You can only select a maximum of 8 seats.";
        customModal.style.display = "flex";
    } else {
        bookSeatForm.submit();
    }

});


customModalClose?.addEventListener("click", () => {
    customModal.style.display = "none";
});


/* ===== Delete Confirmation ===== */
deleteBtns.forEach(deleteBtn => {
    deleteBtn.addEventListener("click", event => {
        if (!confirm("Are you sure you want to delete this?")) {
            event.preventDefault(); 
        }
    });
});