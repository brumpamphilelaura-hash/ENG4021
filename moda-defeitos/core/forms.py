from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'is_active']
        labels = {
            'name': 'Nome do produto',
            'description': 'Descrição do defeito',
            'price': 'Preço',
            'is_active': 'Exibir na vitrine',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
