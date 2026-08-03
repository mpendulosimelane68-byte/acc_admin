from django import forms
from .models import Case


PUBLIC_INSTITUTIONS = [
    ("ministry", "Government Ministry"),
    ("department", "Government Department"),
    ("municipality", "Municipality / Town Council"),
    ("parastatal", "Parastatal"),
    ("police", "Police Service"),
    ("public_health", "Public Health Facility"),
    ("public_school", "Public School"),
    ("public_university", "Public University / College"),
    ("procurement", "Procurement Unit"),
    ("revenue", "Revenue Collection Agency"),
    ("other_public", "Other Public Institution"),
]


PRIVATE_INSTITUTIONS = [
    ("insurance", "Insurance Company"),
    ("telecom", "Telecommunications"),
    ("transport", "Transport Company"),
    ("construction", "Construction Company"),
    ("textile", "Textile / Manufacturing"),
    ("retail", "Retail Business"),
    ("mining", "Mining Company"),
    ("agriculture", "Agriculture Business"),
    ("hotel", "Hotel / Tourism"),
    ("private_health", "Private Health Facility"),
    ("private_school", "Private School"),
    ("private_university", "Private University / College"),
    ("security", "Security Company"),
    ("other_private", "Other Private Institution"),
]


class CaseForm(forms.ModelForm):

    class Meta:
        model = Case
        fields = "__all__"

        widgets = {
            "institution": forms.Select(
                choices=[]
            )
        }

from .models import OrganisationSettings


class OrganisationSettingsForm(forms.ModelForm):

    class Meta:

        model = OrganisationSettings

        fields = [
            "name",
            "short_name",
            "email",
            "phone",
            "address",
            "website",
            "logo",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Organisation Name"
                }
            ),


            "short_name": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"ACC"
                }
            ),


            "email": forms.EmailInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Email Address"
                }
            ),


            "phone": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Telephone"
                }
            ),


            "address": forms.Textarea(
                attrs={
                    "class":"form-control",
                    "rows":3
                }
            ),


            "website": forms.URLInput(
                attrs={
                    "class":"form-control"
                }
            ),

        }

from .models import CaseManagementSettings


class CaseManagementSettingsForm(forms.ModelForm):

    class Meta:
        model = CaseManagementSettings

        fields = [
            "allow_custom_statuses",
            "automatic_case_numbering",
        ]