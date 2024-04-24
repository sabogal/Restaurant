from django.contrib import admin
from .tools.models.order_models import WorkOrder, WorkOrderProducts
from .tools.models.products_models import Products
# Register your models here.

admin.site.register(WorkOrder)
admin.site.register(Products)
admin.site.register(WorkOrderProducts)
