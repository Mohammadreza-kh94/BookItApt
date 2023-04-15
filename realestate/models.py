from django.contrib.auth.models import User
from django.db import models


class Estate(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    sqft = models.IntegerField()
    price = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    photo = models.ImageField(upload_to="img/")
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    # total_price = models.FloatField()
    # guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.estate.name}"
