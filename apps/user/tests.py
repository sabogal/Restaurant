from django.test import TestCase
from .models import User
# Create your tests here.

instance = User.objects.all().first()


instance.is_active = True
instance.save() 
print(instance.is_active)