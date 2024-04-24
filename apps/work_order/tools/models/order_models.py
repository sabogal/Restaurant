
from django.db import models
from apps.models import BaseModel
""" Import models """
from .products_models import Products

state_choice = (
    (1, "Procesado"),
    (2, "Listo")
)

class WorkOrder(BaseModel):
    """ Ordern de trabajo """
    description = models.TextField(verbose_name="descripcion", null=True, blank=True)
    fk_products = models.ManyToManyField(Products, through='WorkOrderProducts' ,verbose_name="productos")
    state = models.PositiveIntegerField(choices=state_choice, verbose_name="estado")
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'orders'
        verbose_name = 'order'
        verbose_name_plural = 'order'
        ordering = ['id']

class WorkOrderProducts(BaseModel):
    fk_products = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="Productos")
    fk_workorder = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, verbose_name="Productos")
    amount = models.PositiveBigIntegerField(verbose_name="cantidad")
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'work_order_products'
        verbose_name = 'orden de trabajo producto'
        verbose_name_plural = 'ordenes de trabajo productos'
        ordering = ['id']