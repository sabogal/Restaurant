from rest_framework import serializers
from django.db.models import F, DecimalField, ExpressionWrapper
from django.core.validators import RegexValidator
from ..models.order_models import WorkOrder, WorkOrderProducts
from .serializers_products import ProductsSerializer
from ..models.products_models import Products
from django.core.serializers.json import DjangoJSONEncoder

import json    
class WorkOrderProductsSerializer(serializers.Serializer):
    fk_products = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
    amount = serializers.IntegerField()


class WorkOrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkOrder
        fields = ('id','description', 'fk_products','state')
        

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        queryset = instance.fk_products.annotate(
        full_price=ExpressionWrapper(
            F('price') * F('workorderproducts__amount'),
            output_field=DecimalField()  # Define el tipo de campo para el resultado
        )).values(
            'name', 
            'full_price',
            basic_price = F('price'),
            amount = F('workorderproducts__amount')
        )
        representation["fk_products"] = queryset 
        representation["state"] = {"label": instance.get_state_display(), "value":instance.state}
        representation["full_price"] = sum(list(queryset.values_list('full_price', flat=True)))
        return representation
        

class WorkOrderSerializer(serializers.ModelSerializer):
    products = WorkOrderProductsSerializer(many=True, allow_empty=False)

    class Meta:
        model = WorkOrder
        fields = ('description', 'products', 'state')

    def create(self, validated_data):
        products = validated_data.pop('products', [])  # obtenemos los datos de los productos
        work_order = WorkOrder.objects.create(**validated_data)
        work_order_products = [
            WorkOrderProducts(
                fk_products = instance["fk_products"],
                fk_workorder = work_order,
                amount = instance["amount"]
            ) 
            for instance in products 
        ]
        WorkOrderProducts.objects.bulk_create(work_order_products)
        return work_order
    
    def update(self, instance, validated_data):
        products = validated_data.pop('products', [])
        data = super().update(instance, validated_data)
        for value in products:
            WorkOrderProducts.objects.update_or_create(
                fk_workorder=data,
                fk_products=value["fk_products"],
                defaults={
                    'amount': value.get("amount")
                }  
            )
        return data
    
    def to_representation(self, instance):
        print(instance)
        data = super().to_representation(instance)
        return data