from django.shortcuts import render
from django.views.generic import ListView,CreateView

from .models import ContaBancaria
# Create your views here.

class Conta_List(ListView):
    model = ContaBancaria
    template_name = "contas/ambiente_conta.html"
