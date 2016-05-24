from django import forms

from .models import ContactUsInfo

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsInfo
        fields = [
            "fullname",
            "emailAddr",
            "contactNo",
            "locationPersonal",
            "locationTombstone",
            "howManyTombstones",
            "installationDate",
            "catalogueCodes",
            "colorTombstone",
            "otherInfo",
        ]
