from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound

from app.customers.models import Customer
from app.customers.views import CustomerSerializer


def display_customers_data_page(request):
    """Display the customers data page"""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer(queryset, many=True)
    return render(request, 'customers.html', {'data': serializer_class.data})


def display_customer_by_id_page(request):
    """Get the user id to search value input and display the customer's info page if the id matches"""

    if request.method == "POST":
        try:
            id_to_search = request.POST.get('id_to_search', None)
            assert str(id_to_search).isdigit() and id_to_search

            customer_data = Customer.objects.get(id=id_to_search)
            if customer_data:
                return render(
                    request, 'customers_by_id.html', {
                        'id': customer_data.id,
                        'first_name': customer_data.first_name,
                        'last_name': customer_data.last_name,
                        'email': customer_data.email,
                        'gender': customer_data.gender,
                        'company': customer_data.company,
                        'city': customer_data.city,
                        'title': customer_data.title,
                    })

        except AssertionError:
            return HttpResponse(
                "<h1>Error! The customer id must be a digit and the id has to be valid!</h1>"
            )
        except (Customer.DoesNotExist, AttributeError):

            return HttpResponseNotFound(
                "<h1>Sorry! The customer you are looking for does not exist!</h1>"
            )


def display_home_page(request):
    """Display the home page of the application"""
    return render(request, 'index.html', {})
