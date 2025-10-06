
from django import forms
from .models import User

class UserForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label="Nom",
        widget=forms.TextInput(attrs={
            'placeholder': "nom de l'entreprise",
            'id': 'reg-company'
        })
    )
    email = forms.EmailField(
        label="Email:",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Entrer votre email'
        })
    )
    password = forms.CharField(
        max_length=50,
        label="Password:",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Entrer votre mot de passe'
        })
    )
    role = forms.ChoiceField(
        choices=[("candidate", "Candidate"), ("employer", "Employer")],
        widget=forms.HiddenInput(),
        required=True
    )


    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("L'utilisateur existe déjà.")
        
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("L'email existe déjà.")
        
        return email
    
    def clean_password(self):
        password = self.cleaned_data['password']

        if password and len(password) < 8:
            raise forms.ValidationError("Le mot de passe doit contenir au moin 8 caractères.")
        
        return password
    

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label="Nom",
        widget=forms.TextInput(attrs={
            'placeholder': 'Entrer votre nom'
        })
    )

    password = forms.CharField(
        max_length=50,
        label="Password:",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Entrer votre mot de passe'
        })
    )
