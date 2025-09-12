from django.test import TestCase
from django import forms
from .models import Booking
from .seats import ALL_SEATS
from films.models import FilmSchedule, Film

class TestBookingForm(TestCase):
    def setup(self):
        self.film = Film.objects.create(title="Test")

