from django import forms

from clients.models import Clients


class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'phone', 'phone_2', 'telegram', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control phone-input', 'id': 'id_phone', 'placeholder': '+7(XXX)XXX-XX-XX'}),
            'phone_2': forms.TextInput(attrs={'class': 'form-control phone-input', 'id': 'id_phone_2', 'placeholder': '+7(XXX)XXX-XX-XX'}),
            'telegram': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }