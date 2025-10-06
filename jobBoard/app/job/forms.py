from django import forms
from .models import Offer, EmployerProfil


class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        exclude = ['employer']
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'titre'}),
            'competence': forms.TextInput(attrs={'placeholder': 'compétences'}),
            'experience': forms.TextInput(attrs={'placeholder': 'éxperiences'}),
            'delay': forms.TextInput(attrs={'placeholder': 'durée'}),
            'profil': forms.TextInput(attrs={'placeholder': "profil"}),
            'description': forms.Textarea(attrs={'placeholder': 'description'}),
            'contract_type': forms.TextInput(attrs={'placeholder': 'type de contract'}),
            'salary': forms.NumberInput(attrs={'placeholder': 'salaire'}),
            'workplace': forms.TextInput(attrs={'placeholder': 'lieu du travail'}),
            'company_name': forms.TextInput(attrs={'placeholder': "nom de l'entreprise"}),
            'activity_sector': forms.TextInput(attrs={'placeholder': "secteur d'activité"}),
            'coordinate': forms.TextInput(attrs={'placeholder': 'coordonnés de contacts'}),
        }

        error_messages = {
            'title': {"required": "Le titre de l'emploi est réquis."},
            'competence': {"required": "Compétence est réquis."},
            'description': {"required": "La description est réquis."},
            'contract_type': {"required": "Type de contract réquis."},
            'company_name': {"required": "Nom de l'entreprise réquis."}
        }


class EmployerProfilForm(forms.ModelForm):

    class Meta:
        model = EmployerProfil
        exclude = ["user, id"]
        fields = "__all__"

        widget = {
            "logo": forms.FileField(),
            "website": forms.Textarea(attrs={'placeholder': 'website'}),
            "address": forms.TextInput(attrs={'placeholder': 'address'}),
            "phone_number": forms.NumberInput(attrs={'placeholder': "numéro de télephone"}),
            "description": forms.Textarea(attrs={'placeholder': 'description'}),
        }