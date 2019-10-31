from django.db import models

# Create your models here.
class DebtorData(models.Model):
    company = models.CharField(max_length=120, unique=True)
    oarex_rating = models.DecimalField(max_digits=4, decimal_places=2)
    pay_terms = models.IntegerField(blank=True, null=True)
    jurisdiction = models.CharField(max_length=30)
    ownership = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.company
        
    class Meta:
        ordering = ('company',)