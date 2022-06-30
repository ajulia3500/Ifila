from django.contrib import admin

from .models import Aluno, Cardapio, Fila, Turma

admin.site.register(Turma)
admin.site.register(Fila)
admin.site.register(Aluno)
admin.site.register(Cardapio)
