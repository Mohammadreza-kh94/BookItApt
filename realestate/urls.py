from django.urls import path

from . import views

app_name = "realestate"
urlpatterns = [
    path("add_estate/", views.add_estate, name="add_estate"),
    path("remove_estate/<int:pk>/", views.remove_estate, name="remove_estate"),
    path("add-reservation/<int:estate_id>/", views.add_reservation, name="add_reservation"),
    path("remove_reservation/<int:pk>/", views.remove_reservation, name="remove_reservation"),
    path("estate_detail/<int:pk>/", views.estate_detail, name="estate_detail"),
    path("reservation_detail/<int:pk>/", views.reservation_detail, name="reservation_detail"),
    path("estate_list", views.estate_list, name="estate_list"),
    path("reservation_list", views.reservation_list, name="reservation_list"),
    path("about", views.about, name="about"),
]
