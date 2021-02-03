import csv

from django.core.management import BaseCommand

from app.customers.models import Customer, CustomerLocation


class Command(BaseCommand):
    help = "Load the customers CSV file and upload it to the database use --path option to type the file path"

    def add_arguments(self, parser):
        # add the --path option for the command to set the csv file path on the command line
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        """Load the customers CSV file and upload it to the database using the Customer model"""

        path = kwargs['path']

        with open(path) as customers_csv_file:
            fieldnames = [
                'id', 'first_name', 'last_name', 'email', 'gender', 'company',
                'city', 'title'
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
        self.set_customers_location_coordinates()

    def set_customers_location_coordinates(self):
        """After creating the database we set the latitude and longitude fields"""
        customer_location = CustomerLocation()
        customer_location.set_customers_locations()
