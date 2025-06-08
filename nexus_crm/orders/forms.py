from django import forms
from .models import Orders, Service, OrderFile


class OrderForm(forms.ModelForm):
    service = forms.ModelChoiceField(
        label='Услуга',
        queryset=Service.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    class Meta:
        model = Orders
        fields = [  "service", "client", 'description', ]
        widgets = {
            'service': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            # 'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            # 'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'total_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'service': 'Услуга',
            'client': 'Клиент',
            'description': 'Описание заявки',
            # 'address': 'Адрес',
            # 'cost_price': 'Себестоимость',
            # 'total_price': 'Общая стоимость',
        }
        help_texts = {
            'description': 'Введите подробное описание заявки...',
        }

    def clean_total_price(self):
        total = self.cleaned_data.get('total_price')
        cost = self.cleaned_data.get('cost_price')
        if total is not None and cost is not None and total < cost:
            raise forms.ValidationError('Общая стоимость не может быть меньше себестоимости.')
        return total





class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["title"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class OrderFileForm(forms.ModelForm):
    class Meta:
        model = OrderFile
        fields = ['file']
