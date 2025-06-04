from django import forms #Importação da ferramenta forms
from .models import Cliente #Importação do modelo

#Criação da calsse
class ClienteForm(forms.ModelForm):
    class Meta:
        #Formatar o formulario
        model = Cliente #Conexão com o modelo
        #Cmpos do formulario (fields)
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'data_nascimento',
            'endereco',
            'telefone',
            'email',
        ]

        #Opcional - serve para conectar com as classe css e atributos do inpu 
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control","placeholder": "Digite seu nome"}),
            "sobrenome": forms.TextInput(attrs={"class":"form-control","placeholder": "Digite seu Sobrenome"}),
            "cpf": forms.TextInput(attrs={"class": "form-control","placeholder": "___.___.___-__"}), # Exemplo de placeholder para CPF
            "data_nascimento": forms.DateInput(attrs={"class": "form-control","placeholder": "DD/MM/AAAA", 'type': 'date'}), # Usando DateInput e type='date'
            "endereco": forms.TextInput(attrs={"class": "form-control","placeholder": "Digite seu endereço"}),
            "telefone": forms.TextInput(attrs={"class": "form-control","placeholder": "(XX) XXXX-XXXX"}), # Exemplo de placeholder para Telefone
            "email": forms.EmailInput(attrs={"class": "form-control","placeholder": "email@example.com"}), # Usando EmailInput
        }