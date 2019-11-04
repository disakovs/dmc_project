from django.db import models

import csv


class Agency(models.Model):
    name = models.CharField(max_length=120, unique=True)
    oarex_rating = models.DecimalField(max_digits=4, decimal_places=2)
    pay_terms = models.IntegerField(blank=True, null=True)
    jurisdiction = models.CharField(max_length=30)
    ownership = models.CharField(max_length=20)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    
    @classmethod
    def update_from_csv(cls, csv_file):
        """
        Takes a csv file and upsert each line to an Agency model
        """
        # Create a CSV reader
        reader = csv.DictReader(csv_file)

        agency_name_list = []

        # Iterate through each row
        for row in reader:
            
            # Check to see if an agency with this name exists
            name = row.get("name")

            if name is None:
                raise self.NoNameColumn("The csv file did not have a `name` column")

            try:
                agency = cls.objects.get(name=name)
            except cls.DoesNotExist:
                agency = cls()
                agency.name = name

            # Update all fields on the agency
            agency.update_from_dict(row)

            # Save it
            agency.save()

            # Add the name to a list of agency names
            agency_name_list.append(agency.name)

        # Delete all agencies whose name is not in the list of agency names
        cls.objects.exclude(name__in=agency_name_list).delete()
    
    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ('name',)

    def update_from_dict(self, data):
        """
        Sets all attributes in the dict to this object
        Saves this object
        """

        for key, value in data.items():
            setattr(self, key, value or None)

        self.save()

    class AgencyException(Exception):
        pass

    class NoNameColumn(AgencyException):
        """
        There was no name on a row from a csv file
        """
