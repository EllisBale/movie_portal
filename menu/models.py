from django.db import models
from cloudinary.models import CloudinaryField


class Menu(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('drink', 'Drink'),
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES
    )

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name
