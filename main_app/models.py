from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

ROAST = (
    ('L', 'Light'),
    ('M', 'Medium'),
    ('D', 'Dark'),
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    origin = models.CharField(max_length=100)
    flavour = models.CharField(max_length=100)
    roast = models.CharField(
        max_length=1,
        choices=ROAST,
        default=ROAST[0][0]
    )
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'product_id': self.id})
    
