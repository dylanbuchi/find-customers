from rest_framework import serializers, viewsets

from rest_framework.response import Response
from app.customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for the Customer model to translate the model data in other formats"""
    class Meta:
        model = Customer
        fields = '__all__'
        depth = 1


class CustomerView(viewsets.ReadOnlyModelViewSet):
    """CustomerView view for the Customer model for the API"""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_customer_by_id(self, request, *args, **kwargs):
        """Returns the customer data by his unique id number"""

        customer_data = self.get_serializer(self.get_object().id).data
        return Response(customer_data)
