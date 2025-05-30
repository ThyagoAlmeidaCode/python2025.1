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
            "nome": forms.TextInput(attrs={"class": "","placeholder": "Digite seu nome"}),
            "sobrenome": forms.TextInput(attrs={"class": "","placeholder": "Digite seu Sobrenome"}),
            "cpf": forms.TextInput(attrs={"class": "","placeholder": "___.___.___-__"}), # Exemplo de placeholder para CPF
            "data_nascimento": forms.DateInput(attrs={"class": "","placeholder": "DD/MM/AAAA", 'type': 'date'}), # Usando DateInput e type='date'
            "endereco": forms.TextInput(attrs={"class": "","placeholder": "Digite seu endereço"}),
            "telefone": forms.TextInput(attrs={"class": "","placeholder": "(XX) XXXX-XXXX"}), # Exemplo de placeholder para Telefone
            "email": forms.EmailInput(attrs={"class": "","placeholder": "email@example.com"}), # Usando EmailInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='col-md-6 mb-0'),
                Column('sobrenome', css_class='col-md-6 mb-0'),
                css_class='form-row' # Usado para espaçamento em versões mais antigas do Bootstrap
            ),
            Row(
                Column('cpf', css_class='col-md-6 mb-0'),
                Column('data_nascimento', css_class='col-md-6 mb-0'),
                css_class='form-row'
            ),
            'endereco', # Este campo ficará em uma linha completa
            Row(
                Column('telefone', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Salvar Cliente', css_class='btn btn-primary mt-3')
        )
