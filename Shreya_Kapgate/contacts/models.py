from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField()
    created_time = models.DateTimeField(auto_now_add=True, editable=False)
