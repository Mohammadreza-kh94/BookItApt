from django import forms

from .models import Estate, Reservation


class EstateForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields = ["name", "description", "city", "state", "sqft", "price", "bedrooms", "bathrooms", "photo"]


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["name", "phone", "email", "message", "check_in_date", "check_out_date"]
