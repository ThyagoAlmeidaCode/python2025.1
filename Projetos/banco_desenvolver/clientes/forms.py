from django import forms
from .models import Cliente
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'data_nascimento',
            'endereco',
            'telefone',
            'email',
        ]

        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome', # Corrigido: 'Sobrenome' deve ser 'sobrenome' (minúsculo)
            'cpf': 'CPF',
            'data_nascimento': 'Data de Nascimento',
            'endereco': 'Endereço',
            'telefone': 'Telefone',
            'email': 'Email',
        }

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control","placeholder": "Digite seu nome"}),
            "sobrenome": forms.TextInput(attrs={"class":"form-control","placeholder": "Digite seu Sobrenome"}),
            "cpf": forms.TextInput(attrs={"class": "form-control","placeholder": "___.___.___-__"}), # Exemplo de placeholder para CPF
            "data_nascimento": forms.DateInput(attrs={"class": "form-control","placeholder": "DD/MM/AAAA", 'type': 'date'}), # Usando DateInput e type='date'
            "endereco": forms.TextInput(attrs={"class": "form-control","placeholder": "Digite seu endereço"}),
            "telefone": forms.TextInput(attrs={"class": "form-control","placeholder": "(XX) XXXX-XXXX"}), # Exemplo de placeholder para Telefone
            "email": forms.EmailInput(attrs={"class": "form-control","placeholder": "email@example.com"}), # Usando EmailInput
        }
