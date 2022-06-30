from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Fila,Turma,Aluno,Cardapio

class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )


class TurmaForm(ModelForm):
    
    class Meta:
        model = Turma
        fields = "__all__"

class AlunoForm(ModelForm):
    
    class Meta:
        model = Aluno
        fields = "__all__"


class FilaForm(ModelForm):
    
    class Meta:
        model = Fila
        fields = "__all__"

class CardapioForm(ModelForm):
    
    class Meta:
        model = Cardapio
        fields = "__all__"
