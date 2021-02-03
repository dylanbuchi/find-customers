import os

from django.db import models

from mapbox import Geocoder

# Create your models here.


class Customer(models.Model):
    """Database model for the customers"""

    # fields
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    email = models.EmailField(max_length=255)
    gender = models.CharField(max_length=255)

    company = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    latitude = models.DecimalField(max_digits=22,
                                   decimal_places=16,
                                   blank=True,
                                   null=True)
    longitude = models.DecimalField(max_digits=22,
                                    decimal_places=16,
                                    blank=True,
                                    null=True)

    # getters methods
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender

    def get_company(self):
        return self.company

    def get_city(self):
        return self.city

    def get_title(self):
        return self.title

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    # magic methods
    def __repr__(self) -> str:
        return f"\
        Name: {self.first_name}, \
        LastName: {self.last_name}, \
        Email: {self.email}, \
        Gender: {self.gender}, \
        Company: {self.company}, \
        City: {self.city}, \
        Title: {self.title}, \
        Latitude: {self.latitude}, \
        Longitude: {self.longitude}"


class CustomerLocation():
    """Customer Location model to get the customers longitude and latitude coordinates from the Map Box API"""

    customers = Customer.objects.all()
    # loads the secret TOKEN API from the .env file, to get access to the API
    geocoder = Geocoder(access_token=os.environ['MAP_BOX_TOKEN'])

    def set_customers_locations(self):
        """Set the customer latitude and longitude by his city name"""
        if not self.customers:
            raise ValueError("There is no customer!")

        for customer in self.customers:
            city = customer.get_city()
            if city:
                response = self.geocoder.forward(city)
                collection = response.json()
                coordinates = collection['features'][0]['geometry'][
                    'coordinates']

                longitude, latitude = coordinates
                customer.longitude = longitude
                customer.latitude = latitude
                customer.save()
