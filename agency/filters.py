import django_filters
from django.db import models
from . import models
from django import forms


def create_jurisdiction_choices():
    return ()
    qs = models.Agency.objects.order_by().values('jurisdiction').distinct()
    print('qs:', qs)
    choices = []
    for object in qs:
        choice_tuple = (object['jurisdiction'], object['jurisdiction'])
        
        choices.append(choice_tuple)

    return choices 

    
class DebtorDataFilter(django_filters.FilterSet):
    OWNERSHIP_CHOICES =  (
        ('', 'All'),
        ('Public', 'Public'),
        ('Private', 'Private'),
    )
    JURISDICTION_CHOICES = create_jurisdiction_choices()
    
    ownership = django_filters.CharFilter(field_name='ownership', label='Ownership', widget=forms.Select(choices=OWNERSHIP_CHOICES))
    pay_terms = django_filters.RangeFilter(label='Pay Terms Range (min-max)')
    jurisdiction = django_filters.MultipleChoiceFilter(field_name='jurisdiction', choices=JURISDICTION_CHOICES, widget=forms.CheckboxSelectMultiple)
    oarex_rating = django_filters.RangeFilter(label='Oarex rating range (min-max)')
    company = django_filters.CharFilter(field_name='company', lookup_expr='icontains', label='Company Search')
    
    class Meta:
        model = models.Agency
        fields = ['company', 'oarex_rating', 'pay_terms', 'jurisdiction', 'ownership']
