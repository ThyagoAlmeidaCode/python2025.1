from django import forms #Importar o forms
from .models import Cliente #Importa o modelo (ex: Cliente)
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente #Modelo (Classe do model)
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'data_nascimento',
            'endereco',
            'telefone',
            'email'
        ]

        #Opcional - Personlização do input do formulario
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control","placeholder": "Digite seu nome"}),
            "sobrenome": forms.TextInput(attrs={"class":"form-control","placeholder": "Digite seu Sobrenome"}),
            "cpf": forms.TextInput(attrs={"class": "form-control","placeholder": "___.___.___-__"}), # Exemplo de placeholder para CPF
            "data_nascimento": forms.DateInput(attrs={"class": "form-control","placeholder": "DD/MM/AAAA", 'type': 'date'}), # Usando DateInput e type='date'
            "endereco": forms.TextInput(attrs={"class": "form-control","placeholder": "Digite seu endereço"}),
            "telefone": forms.TextInput(attrs={"class": "form-control","placeholder": "(XX) XXXX-XXXX"}), # Exemplo de placeholder para Telefone
            "email": forms.EmailInput(attrs={"class": "form-control","placeholder": "email@example.com"}), # Usando EmailInput
        }
