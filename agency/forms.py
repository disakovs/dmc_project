from django import forms


class UploadDataForm(forms.Form):
    csv_file = forms.FileField()
    
    class Meta:
        fields = ['csv_file']
