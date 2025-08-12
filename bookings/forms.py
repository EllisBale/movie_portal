from django import forms
from .models import Booking
from .seats import ALL_SEATS
from films.models import FilmSchedule, Film

class BookingForm(forms.Form):
    schedule = forms.ModelChoiceField(queryset=FilmSchedule.objects.all(), label="Select Showtime")
    seat_numbers = forms.MultipleChoiceField(
        choices=[(seat, seat) for seat in ALL_SEATS],
        widget=forms.CheckboxSelectMultiple,
        label="Select your seats (max 8)",
    )
    
    def clean_seat_numbers(self):
        seats = self.cleaned_data.get('seat_numbers')
        if not seats:
            raise forms.ValidationError("Please select at least one seat.")
        if len(seats) > 8:
            raise forms.ValidationError("You can select a maximum of 8 seats.")
        return seats
    
class FilmSelectForm(forms.Form):
    film = forms.ModelChoiceField(queryset=Film.objects.all(), label="Select a Film")