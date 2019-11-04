from django.contrib import admin

from django.urls import path
from django_filters.views import FilterView

from .filters import DebtorDataFilter
from .views import DataUploadView


app_name = 'agency'

urlpatterns = [
    path('', FilterView.as_view(filterset_class=DebtorDataFilter, template_name='agency/filter.html'), name='filter'),
    path('upload/', DataUploadView.as_view(), name='upload'),
]
