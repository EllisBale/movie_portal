from django import forms
from .models import Booking, FilmSchedule
from .seats import ALL_SEATS

class BookingForm(forms.ModelForm):
    seat_number = forms.MultipleChoiceField(
        choices=[],
        label="Seat(s)", 
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Booking
        fields = ['film_schedule', 'guests',]
        widgets = {
            'film_schedule': forms.Select(attrs={'class': 'form-control'}),
            'guests': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['film_schedule'].queryset = FilmSchedule.objects.order_by('show_date', 'slot')



    def clean_seat_number(self):
        seats = self.cleaned_data.get('seat_number', [])
        if len(seats) > 8:
            raise forms.ValidationError(" You can only select a maximum of 8 seats.")
        
        if len(seats) != self.cleaned_data.get('guests'):
            raise forms.ValidationError("The number of seats must match number of guests.")

        return seats

    