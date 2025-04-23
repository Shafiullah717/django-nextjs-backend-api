from django.db import models

# Create your models here.
class waitlistEntry(models.Model):
    # User = 
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)