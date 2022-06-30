
from imaplib import _Authenticator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import Cardapio, Turma, Aluno, Fila
from .forms import TurmaForm,AlunoForm,FilaForm, CardapioForm, UserForm
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
from .utils import Gerar_Pdf
def home(request):
    return render(request, 'home.html')
@login_required
def cadastro_turma(request):
    if request.method == "POST":
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/turma/cadastro")
    else:
        form = TurmaForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'turma/cadastro.html', context)
# Aluno
@login_required
def listar_aluno(request):
    aluno = Aluno.objects.all
    
    context = {
        'alunos': aluno,
    }
    
    return render(request, 'aluno/listar.html', context)
@login_required
def excluir_aluno(request, id):
    
    Aluno.objects.get(pk=id).delete()
    
    return HttpResponseRedirect("/listar/aluno")

@login_required
def cadastro_aluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("")
    else:
        form = AlunoForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'aluno/cadastro.html', context)
@login_required
def editar_aluno(request,aluno_id):

    aluno = Aluno.objects.get(id=aluno_id)

    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/aluno")
    else:
        form = AlunoForm(instance=aluno)
    
    context = {
        'form': form,
        'aluno_id': aluno_id
    }
    return render(request, 'aluno/editar.html', context)    

@login_required
def excluir_aluno(request, aluno_id):
    
    Aluno.objects.get(pk=aluno_id).delete()
    
    return HttpResponseRedirect("/aluno")
@login_required
def cadastro_fila(request):
    if request.method == "POST":
        form = FilaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("")
    else:
        form = FilaForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'fila/cadastro.html', context)



# cardapio
@login_required
def cadastro_cardapio(request):
    if request.method == "POST":
        form = CardapioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("")
    else:
        form = CardapioForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'cardapio/cadastro.html', context)


def cadastro_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("")
    else:
        form = UserForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'teste.html', context)


def login_fila(request):
    context = {}

    if request.method == 'POST':

        username = request.POST.get('nome')
        senha = request.POST.get('senha')

        user = authenticate(username = username, password = senha) 
        if user:
            login(request, user)
            return render(request, 'home.html', context)
        else:
            context['error'] = 'Senha ou usuário invalidos'
    
    return render(request, 'login.html', context)




@login_required
def listar_cardapio(request):
    cardapio = Cardapio.objects.all
    
    context = {
        'cardapios': cardapio,
    }
    
    return render(request, 'cardapio/listar.html', context)
@login_required
def excluir_cardapio(request, id):
    
    Aluno.objects.get(pk=id).delete()
    
    return HttpResponseRedirect("/listar/cardapio")

@login_required
def editar_cardapio(request,cardapio_id):

    cardapio = Cardapio.objects.get(id=cardapio_id)

    if request.method == "POST":
        form = CardapioForm(request.POST, instance=cardapio)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/cardapio")
    else:
        form = CardapioForm(instance=cardapio)
    
    context = {
        'form': form,
        'cardapio': cardapio
    }
    return render(request, 'cardapio/editar.html', context)    

@login_required
def excluir_cardapio(request, cardapio_id):
    
    Cardapio.objects.get(pk=cardapio_id).delete()
    
    return HttpResponseRedirect("/cardapio")



# fila
@login_required
def fila(request):
    alunos = Aluno.objects.order_by('?') 
    context1 = {
    'aluno': alunos,
    }

    
    return render(request, 'fila/fila.html', context1,)

@login_required
class Fila_View(View, Gerar_Pdf ):

    def get(self,request, *args, **kwargs):
        alunos = Aluno.objects.order_by('?') 
        context1 = {
        'aluno': alunos,
        }
        pdf = Gerar_Pdf()
        
        return pdf.render_to_pdf('fila/fila.html',context1)

    
    
