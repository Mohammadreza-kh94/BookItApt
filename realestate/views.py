from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import ReservationForm
from .models import Estate, Reservation


def index(request):
    return render(request, "index.html")


def remove_estate(request, pk):
    estate = get_object_or_404(Estate, pk=pk)
    estate.delete()
    return HttpResponse("Estate removed successfully")


def add_reservation(request, estate_id):
    estate = get_object_or_404(Estate, pk=estate_id)

    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.estate = estate
            reservation.save()
            return redirect("/realestate/reservation_detail/{}".format(reservation.pk))
    else:
        form = ReservationForm()
    return render(request, "add_reservation.html", {"form": form, "estate": estate})


def remove_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    return HttpResponse("Reservation removed successfully")


def estate_detail(request, pk):
    estate = get_object_or_404(Estate, pk=pk)
    reservations = Reservation.objects.filter(estate=estate, check_out_date__gt=timezone.now())
    return render(request, "estate_detail.html", {"estate": estate, "reservations": reservations})


def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, "reservation_detail.html", {"reservation": reservation})


def estate_list(request):
    estates = Estate.objects.all()
    return render(request, "estate_list.html", {"estates": estates})


def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, "reservation_list.html", {"reservations": reservations})


def about(request):
    return render(request, "about.html")


from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Estate


def add_estate(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        city = request.POST["city"]
        state = request.POST["state"]
        sqft = request.POST["sqft"]
        price = request.POST["price"]
        bedrooms = request.POST["bedrooms"]
        bathrooms = request.POST["bathrooms"]
        photo = request.FILES.get("photo")

        new_estate = Estate(
            name=name,
            description=description,
            city=city,
            state=state,
            sqft=sqft,
            price=price,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            photo=photo,
        )
        new_estate.save()

        messages.success(request, "Estate created successfully!")
        return redirect("/realestate/estate_list")

    return render(request, "add_estate.html")
