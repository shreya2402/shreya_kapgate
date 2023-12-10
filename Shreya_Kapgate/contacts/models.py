from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.TextField(max_length=200, default="")
    is_done = models.BooleanField(default=False)
