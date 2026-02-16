from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    stock = models.IntegerField()
    price = models.FloatField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.name
