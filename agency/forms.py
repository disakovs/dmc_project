from django import forms
from django.core import exceptions

from . import models

import csv, io


class UploadDataForm(forms.Form):
    csv_file = forms.FileField()

    def clean(self):
        cleaned_data = super().clean()

        csv_file = cleaned_data.get("csv_file")

        if not csv_file:
            raise exceptions.ValidationError("Please select a file")

        if not csv_file.name.endswith(".csv"):
            raise exceptions.ValidationError("File is not a CSV type")

        return cleaned_data

    def load_data(self):
        """
        Take the csv file and load all records into the Agency models
        """
        assert "csv_file" in self.cleaned_data

        csv_file = io.TextIOWrapper(self.cleaned_data["csv_file"],
                                    encoding="utf-8",
                                    errors="replace")

        models.Agency.update_from_csv(csv_file)
