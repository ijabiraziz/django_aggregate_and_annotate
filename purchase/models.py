from django.db import models
from customer.models import Customers

# Create your models here.
class Purchase(models.Model):
    amount = models.FloatField(help_text="in PKR")
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='purchases')

    def __str__(self) -> str:
        return self.customer.name
    
    class Meta:
        verbose_name_plural = 'Purchase'
