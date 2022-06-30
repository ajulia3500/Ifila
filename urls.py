from django.urls import path

from . import views

urlpatterns = [

     #cadastro
    path('cadastro/',views.cadastro_user, name='cadastro_fila'),
    path('login/',views.login_fila, name='login'),


    path('',views.home, name='home'),
    #aluno
    path('aluno/cadastro',views.cadastro_aluno, name='cadastro_aluno'),
    path('aluno',views.listar_aluno, name='listar_aluno'),
    path('aluno/editar/<int:aluno_id>/',views.editar_aluno, name='editar_aluno'),
    path('aluno/delete/<int:aluno_id>/',views.excluir_aluno, name='excluir_aluno'),

    #cardapio
    path('cardapio/cadastro',views.cadastro_cardapio, name='cadastro_cardapio'),
    path('cardapio',views.listar_cardapio, name='listar_cardapio'),
    path('cardapio/editar/<int:cardapio_id>/',views.editar_cardapio, name='editar_cardapio'),
    path('cardapio/delete/<int:cardapio_id>/',views.excluir_cardapio, name='excluir_cardapio'),


    #fila
    path('fila/cadastro',views.cadastro_fila, name='cadastro_fila'),
    path('fila/criar',views.fila, name='fila'),
    path('fila/criar/pdf',views.Gerar_Pdf, name = 'fila_pdf'),

    
]