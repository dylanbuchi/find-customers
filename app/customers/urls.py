from django.urls import path, include
from rest_framework import routers
from app.customers.views import CustomerView

router = routers.DefaultRouter()
router.register('', CustomerView, basename='customer')

urlpatterns = [path('', include(router.urls))]
