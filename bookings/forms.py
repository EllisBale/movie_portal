from django import forms
from django.utils import timezone
from .models import Booking, BookingSeat

class BookingForm(forms.ModelForm):
    seats = forms.MultipleChoiceField(
        # Choices are from rows A-F and seat 1-8
        choices=[(f"{row}{num}", f"{row}{num}")
                 for row, _ in BookingSeat.ROW_CHOICES
                 for num in range(1, 9)],
        widget= forms.CheckboxSelectMultiple(attrs={
            'class': 'seat-checkbox',}),
        required =True,
        label="Select seats (max 8)"
    )


    class Meta:
        model = Booking
        fields = ['film', 'date', 'time', 'guests']
        widgets = {
            'film': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            
            'time': forms.Select(attrs={'class': 'form-select'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Limit date picker to today or in future
        self.fields['date'].widget.attrs['min'] = timezone.localdate().strftime('%Y-%m-%d')

    def clean_date(self):
        # Validation to check if date is not in the past
        date = self.cleaned_data.get('date')
        if date < timezone.localdate():
            raise forms.ValidationError("You can't book a date in the past!")
        return date
    
    def clean_seats(self):
        # Validation to check if at least 1 seat is selected and no more than 8 seats is selected
        seats = self.cleaned_data.get('seats')
        if not seats:
            raise forms.ValidationError("Please select at least one seat.")
        if len(seats) > 8:
            raise forms.ValidationError("You can't select more than 8 seats!")
        return seats
    
    def clean_guests(self):
        # Validation to check if guests is between 1 and 8
        guests = self.cleaned_data.get('guests')
        if guests < 1 or guests > 8:
            raise forms.ValidationError("Number of guests must be between 1 and 8.")
        return guests
            
    

