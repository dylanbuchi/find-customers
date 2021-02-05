from django.urls import path

from app.pages.views import (
    display_customers_data_page,
    display_customer_by_id_page,
    display_home_page,
)

urlpatterns = [
    path('', display_home_page),
    path('customers/', display_customers_data_page, name="customers"),
    path('customers_by_id/',
         display_customer_by_id_page,
         name="customers_by_id"),
]
