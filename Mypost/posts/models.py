from django.db import models

# Create your models here.
class post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
