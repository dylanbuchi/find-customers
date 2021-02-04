from django.urls import path, include
from rest_framework import routers
from app.customers.views import CustomerView

router = routers.DefaultRouter()
customer_list = CustomerView.as_view({'get': 'list'})

router.register(r'', CustomerView, basename='customer')
urlpatterns = [
    path('', include(router.urls)),
    path('', customer_list, name='api')
]
