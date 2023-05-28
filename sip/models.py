from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return self.username
    

class Product(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Event(models.Model):
    event_date = models.DateField(null=False)
    user = models.ForeignKey(to=get_user_model(),  null=True, on_delete=models.SET_NULL, related_name='event')
    product = models.ForeignKey(to=Product, null=True, on_delete=models.SET_NULL, related_name='event')
    amount = models.IntegerField(null=False)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    direction = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.direction

    @property
    def weekdaynumber_and_year(self):
        return f'{self.event_date.weekday} | {self.event_date.year}'
    
    def save(self, *args, **kwargs):
        is_received_from_peterfruit = self.product  in ['Kit', 'filme', 'Fertilizante']
        if is_received_from_peterfruit:
            self.direction = "Received from Peterfruit"
        else:
            self.direction = "Sent to Peterfruit"

        self.total = self.amount * self.unit_price
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("event-detail", kwargs={"pk": self.pk})


class Invetory(models.Model):
    user = models.ForeignKey(to=get_user_model(),  null=True, on_delete=models.SET_NULL, related_name='inventory')
    nobre_amount = models.IntegerField(null=False)
    special_amount = models.IntegerField(null=False)
    top10_amount = models.IntegerField(null=False)
    moranguito_amount = models.IntegerField(null=False)
