from django import forms
from .models import Booking
from .seats import ALL_SEATS
from films.models import FilmSchedule, Film

class BookingForm(forms.Form):
    schedule = forms.ModelChoiceField(
        queryset=FilmSchedule.objects.all(),
        label="Select Showtime",
        widget=forms.Select(attrs={'class': 'form-select form-select-md'})
    )
    seat_numbers = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label="Select your seats (max 8)",
    )

    def __init__(self, *args, **kwargs):
        schedule = kwargs.pop('schedule', None)
        super().__init__(*args, **kwargs)

        # Default choices (all seats)
        available_seats = [(seat, seat) for seat in ALL_SEATS]

        if schedule:
            # Remove seats already booked for this schedule
            booked_seats = Booking.objects.filter(film_schedule=schedule).values_list('seat__seat_number', flat=True)
            available_seats = [(seat, seat) for seat in ALL_SEATS if seat not in booked_seats]

        self.fields['seat_numbers'].choices = available_seats

    def clean_seat_numbers(self):
        seats = self.cleaned_data.get('seat_numbers')
        if not seats:
            raise forms.ValidationError("Please select at least one seat.")
        if len(seats) > 8:
            raise forms.ValidationError("You can select a maximum of 8 seats.")
        return seats


class FilmSelectForm(forms.Form):
    film = forms.ModelChoiceField(queryset=Film.objects.all(), label="Choose A Film")




class FilmScheduleForm(forms.ModelForm):
    class Meta:
        model = FilmSchedule
        fields = ['film', 'days_of_week', 'slot', 'specific_date', 'specific_time']
        widgets = {
            'film': forms.Select(attrs={'class': 'form-select'}),
            'days_of_week': forms.Select(attrs={'class': 'form-select'}),
            'slot': forms.Select(attrs={'class': 'form-select'}),
            'specific_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'specific_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
    


class StaffBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['film_schedule', 'seat', 'user']
        widgets = {
            'film_schedule': forms.Select(attrs={'class': 'form-select'}),
            'seat': forms.Select(attrs={'class': 'form-select'}),
            'user': forms.Select(attrs={'class': 'form-select'}),
        }