from django.core.exceptions import ValidationError


ROWS = ['A', 'B', 'C', 'D', 'E', 'F']
SEATS_PER_ROW = 8


ALL_SEATS = [
    f"{row}{num}"
    for row in ROWS for num in range(
        1, SEATS_PER_ROW + 1
        )]


def validate_seat(value):
    """
    Validate that the given seat is valid (A1-F8) or raise ValidationError.
    """

    value = value.strip().upper()
    if value not in ALL_SEATS:
        raise ValidationError(
            f"Seat '{value}' is invalid. Choose a seat between A1 and F8.")
