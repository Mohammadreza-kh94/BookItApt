from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Estate, Reservation


class EstateReservationViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.image = SimpleUploadedFile(
            name="home.jpg",
            content=open(settings.BASE_DIR / "static/img/home.jpg", "rb").read(),
            content_type="image/jpeg",
        )

        # Create some estates and reservations
        self.estate1 = Estate.objects.create(
            name="Luxury Penthouse",
            description="Lavish 4-bedroom penthouse with stunning city views",
            city="San Francisco",
            state="CA",
            sqft=5000,
            price=10000000,
            bedrooms=4,
            bathrooms=5,
            photo="static/img/Luxury_Penthouse.webp",
        )

        self.estate2 = Estate.objects.create(
            name="Urban Townhouse",
            description="Stylish 3-bedroom townhouse in a trendy urban area",
            city="Portland",
            state="OR",
            sqft=2000,
            price=600000,
            bedrooms=3,
            bathrooms=3,
            photo="static/img/Urban_Townhouse.jpg",
        )

        self.estate3 = Estate.objects.create(
            name="Coastal Cottage",
            description="Adorable 2-bedroom cottage just steps from the beach",
            city="Charleston",
            state="SC",
            sqft=800,
            price=250000,
            bedrooms=2,
            bathrooms=1,
            photo="static/img/Coastal_Cottage.jpg",
        )

        self.reservation1 = Reservation.objects.create(
            name="farzad",
            email="farzad@example.com",
            phone="+989121234567",
            message="I would like to formally reserve the estate for 5 days",
            check_in_date=timezone.now().date() - timezone.timedelta(days=10),
            check_out_date=timezone.now().date() - timezone.timedelta(days=5),
            estate_id=self.estate1.id,
        )

        self.reservation2 = Reservation.objects.create(
            name="Shima",
            email="shima@example.com",
            phone="+989127539510",
            message="Please reserve the estate for me and let me know what steps are necessary to secure the reservation.",
            check_in_date=timezone.now().date() + timezone.timedelta(days=3),
            check_out_date=timezone.now().date() + timezone.timedelta(days=7),
            estate_id=self.estate2.id,
        )

    def test_add_estate_view(self):
        url = reverse("realestate:add_estate")

        data = {
            "name": "Lakeview Mansion",
            "description": "Stunning 6-bedroom mansion with breathtaking lake views",
            "city": "Seattle",
            "state": "WA",
            "sqft": 10000,
            "price": 5000000,
            "bedrooms": 6,
            "bathrooms": 7,
            "photo": self.image,
        }

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("realestate:estate_list"))
        self.assertEqual(Estate.objects.count(), 4)

    def test_remove_estate_view(self):
        url = reverse("realestate:remove_estate", args=[self.estate1.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Estate.objects.count(), 2)
        self.assertContains(response, "Estate removed successfully")

    def test_add_reservation_view(self):
        url = reverse("realestate:add_reservation", args=[self.estate1.id])

        data = {
            "name": "Hamid",
            "email": "hamid@example.com",
            "phone": "+989302343001",
            "message": "I would like to make a reservation for the estate.",
            "check_in_date": timezone.now().date() + timezone.timedelta(days=8),
            "check_out_date": timezone.now().date() + timezone.timedelta(days=12),
            "estate_id": self.estate3,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(), 3)
