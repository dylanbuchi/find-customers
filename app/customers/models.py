import os
from django.db import models

from mapbox import Geocoder, Static

# Create your models here.


class Customer(models.Model):
    """Database model for the customers"""

    # fields
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    email = models.EmailField(max_length=255, unique=True)
    gender = models.CharField(max_length=255)

    company = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    latitude = models.DecimalField(max_digits=22,
                                   decimal_places=4,
                                   blank=True,
                                   null=True)
    longitude = models.DecimalField(max_digits=22,
                                    decimal_places=4,
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


class CustomerLocationHandler():
    """Customer Location model to get the customers longitude and latitude coordinates from the Map Box API"""
    # IF API KEY: Load the secret TOKEN API from the .env file, to get access to the API
    # secret = os.environ['MAP_BOX_TOKEN']
    # geocoder = Geocoder(secret)
    # TOKEN = secret
    # geocoder = Geocoder(access_token=TOKEN)

    geocoder = Geocoder()
    customers = Customer.objects.all()

    def set_customers_locations(self):
        """Set the customer latitude and longitude by his city name"""

        if not self.customers:
            raise ValueError("There is no customer!")

        for customer in self.customers:
            self.update_customer_location(customer)

    def get_customer_location_from_API(self, customer: Customer) -> tuple:
        """Return the customer's city location longitude and latitude coordinates from the Map Box API"""

        city = customer.get_city()
        coordinates = None

        if city:
            response = self.geocoder.forward(city)
            collection = response.json()

            # The format from the API is (longitude, latitude)
            coordinates = collection['features'][0]['geometry']['coordinates']
        return coordinates

    def update_customer_location(self, customer: Customer):
        """Update a customer's location based on his city"""

        longitude = latitude = 0
        coordinates = self.get_customer_location_from_API(customer)

        if coordinates:
            longitude, latitude = coordinates

        customer.longitude = longitude
        customer.latitude = latitude
        customer.save()

    def get_customers_images_locations(self):
        """Get every image location from the MapBox API based on his city longitude and latitude coordinates"""
        # add api token key here to get all the images
        # service = Static(self.TOKEN)
        service = Static()

        for customer in self.customers:
            city = {
                'type': 'Feature',
                'properties': {
                    'name': customer.get_city()
                },
                'geometry': {
                    'type':
                    'Point',
                    'coordinates':
                    [customer.get_longitude(),
                     customer.get_latitude()]
                }
            }
            response = service.image('mapbox.satellite', features=[city])
            image_path = rf"C:\Users\crypt\Desktop\customers-rest-api\customers-rest-api\app\pages\static\images\{customer.id}.png"
            self.save_customer_image_location(image_path, response)

    def save_customer_image_location(self, filepath, response):
        """Save the customer's image location to the static folder, files format name are: {customer_id}.png"""

        if not os.path.isfile(filepath):
            # create and write something to the file for it to exist before saving the image on it
            with open(filepath, 'w') as output:
                output.write('something')

        with open(filepath, 'wb') as output:
            output.write(response.content)
