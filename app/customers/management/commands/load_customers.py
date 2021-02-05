import csv

from django.db import IntegrityError
from django.core.management import BaseCommand

from app.customers.models import Customer, CustomerLocationHandler


class Command(BaseCommand):
    help = "Load the customers CSV file and upload it to the database use --path option to type the file path"
    customer_location_handler = CustomerLocationHandler()

    def add_arguments(self, parser):
        # add the --path option for the command to set the csv file path on the command line
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        """Load the customers CSV file and upload it to the database using the Customer model"""

        path = kwargs['path']

        try:
            with open(path) as customers_csv_file:
                fieldnames = [
                    'id', 'first_name', 'last_name', 'email', 'gender',
                    'company', 'city', 'title'
                ]
                customers_data = csv.DictReader(customers_csv_file,
                                                fieldnames=fieldnames)
                # skip the headers
                next(customers_data, None)

                for row in customers_data:
                    Customer(first_name=row['first_name'],
                             last_name=row['last_name'],
                             email=row['email'],
                             gender=row['gender'],
                             company=row['company'],
                             city=row['city'],
                             title=row['title']).save()

        except IntegrityError:
            return (
                "Customers can't have the same email, please check your data!")
        except FileNotFoundError:
            return "The path to the file is incorrect or does not exist!\nLine 46: load_customers.py"

        first_customer = Customer.objects.get(id=1)

        # If The first customer in the file has not coordinates
        # this means it's the first file load, so we only do it once!
        if first_customer.latitude is None:
            self.set_customers_location_coordinates()
            self.get_customers_images_locations()

    def set_customers_location_coordinates(self):
        """After creating the database we set the latitude and longitude fields"""

        self.customer_location_handler.set_customers_locations()

    def get_customers_images_locations(self):
        """After getting the customers's latitude and longitude we get the customers location images and store it in the static folder"""
        self.customer_location_handler.get_customers_images_locations()
