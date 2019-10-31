from django import forms
from .models import DebtorData

class UploadDataForm(forms.Form):
    csv_file = forms.FileField()
    
    class Meta:
        fields = ['csv_file']