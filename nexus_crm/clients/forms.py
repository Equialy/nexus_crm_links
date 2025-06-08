from django import forms

from clients.models import Clients


class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'phone', 'phone_2', 'telegram', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_2': forms.TextInput(attrs={'class': 'form-control'}),
            'telegram': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }