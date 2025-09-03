from django import forms 
from films.models import Film
from bookings.models import Booking
from django.contrib.auth import get_user_model
User = get_user_model()



class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'poster', 'hero_image', 'cast', 'genre', 'release_date',
                  'duration', 'is_popular', 'is_coming_soon', 'is_family', 'is_hero_image']
        

class StaffBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['film_schedule', 'seat', 'user']
        widgets = {
            'film_schedule': forms.Select(attrs={'class': 'form-select'}),
            'seat': forms.Select(attrs={'class': 'form-select'}),
            'user': forms.Select(attrs={'class': 'form-select'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'is_active',
            'is_staff'
        ]
        help_texts = {
            'is_active': None,
            'is_staff': None,
        }