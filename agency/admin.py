from django.contrib import admin
from . import models


class DebtorDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'pay_terms', 'jurisdiction', 'ownership')
    
admin.site.register(models.Agency, DebtorDataAdmin)
