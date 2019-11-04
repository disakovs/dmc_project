import django_filters
from django.db import models
from . import models
from django import forms


def create_jurisdiction_choices():
    qs = models.Agency.objects.values_list('jurisdiction', flat=True).order_by().distinct()
    return ((jurisdiction, jurisdiction) for jurisdiction in qs)

    
class DebtorDataFilter(django_filters.FilterSet):
    OWNERSHIP_CHOICES =  (
        ('', 'All'),
        ('Public', 'Public'),
        ('Private', 'Private'),
    )
    
    ownership = django_filters.CharFilter(field_name='ownership', label='Ownership', widget=forms.Select(choices=OWNERSHIP_CHOICES))
    pay_terms = django_filters.RangeFilter(label='Pay Terms Range (min-max)')
    jurisdiction = django_filters.MultipleChoiceFilter(field_name='jurisdiction', choices=create_jurisdiction_choices, widget=forms.CheckboxSelectMultiple)
    oarex_rating = django_filters.RangeFilter(label='Oarex rating range (min-max)')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Company Search')
    
    class Meta:
        model = models.Agency
        fields = ['name', 'oarex_rating', 'pay_terms', 'jurisdiction', 'ownership']
