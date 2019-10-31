from django.contrib import admin
from .models import DebtorData
# Register your models here.
class DebtorDataAdmin(admin.ModelAdmin):
    list_display = ('company', 'pay_terms', 'jurisdiction', 'ownership')
    
admin.site.register(DebtorData, DebtorDataAdmin)

