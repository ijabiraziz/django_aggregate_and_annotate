from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Customers'
