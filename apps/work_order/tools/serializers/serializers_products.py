from rest_framework import serializers
from django.core.validators import RegexValidator
from ..models.order_models import WorkOrder
from ..models.products_models import Products
    
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'description', 'price')
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["id"] = instance.id
        representation["name"] = str(instance.name).title()
        return representation
    