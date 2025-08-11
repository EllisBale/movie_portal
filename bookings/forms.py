from django import forms
from .models import Booking, FilmSchedule
from .seats import ALL_SEATS

class BookingForm(forms.ModelForm):
    seat_number = forms.ChoiceField(choices=[(seat, seat) for seat in ALL_SEATS], label="Seat")

    class Meta:
        model = Booking
        fields = ['film_schedule', 'guests', 'seat_number']
        widgets = {
            'film_schedule': forms.Select(attrs={'class': 'form-control'}),
            'guests': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['film_schedule'].queryset = FilmSchedule.objects.order_by('show_date', 'slot')

