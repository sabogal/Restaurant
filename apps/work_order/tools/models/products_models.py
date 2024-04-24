
from django.db import models
from apps.models import BaseModel
""" Import models """
from apps.user.models import User

class Products(BaseModel):
    """ Ordern de trabajo """

    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(verbose_name="tipo de daño", blank=True, null=True)
    price = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['id']