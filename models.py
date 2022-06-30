from re import X
from django.db import models

class Turma(models.Model):
    
    nome = models.CharField( max_length=5)

    
    def __str__(self):
        return self.nome
    


class Aluno(models.Model):
    
    TURMA = (
        ("1AB", "1AB"),
        ("2AB", "2AB"),
        ("3AB", "3AB"),
        ("1AA", "1AA"),
        ("2AA", "2AA"),
        ("3AA", "3AA"),
        ("1BA", "1BA"),
        ("2BA", "2BA"),
        ("3BA", "3BA"),
        ("1AII", "1AII"),
        ("2AII", "2AII"),
        ("3AII", "3AII"),
        ("1BII", "1BII"),
        ("2BII", "2BII"),
        ("3BII", "3BII"),

    )

    STATUS = (
        ("Ativo", "Ativo"),
        ("Inativo", "Inativo"),
    )
    nome = models.CharField( max_length=200)
    email = models.EmailField(max_length=254)
    status = models.CharField(max_length=10, choices=STATUS, blank=False, null=False)
    turma = models.CharField(max_length=10, choices=TURMA, blank=False, null=False)
    

    def __str__(self):
        return self.nome    

    def get_turma(self):
        return self.turma    

class Cardapio(models.Model):
    FEIJAO = (
        ("Caldo", "Caldo"),
        ("Tropeiro", "Tropeiro"),
        ("Feijoada", "Feijoada"),
    )

    PROTEINA = (
        ("Carne de Boi Cozida", "Carne de Boi Cozida"),
        ("Ovo Cozido", "Ovo Cozido"),
        ("Frango Assado", "Frango Assado"),
        ("Estrogonofe", "Estrogonofe"),
        ("Lasanha", "Lasanha"),
    )
    
    arroz = 'Arroz'
    feijao = models.CharField(max_length=20, choices=FEIJAO, blank=False, null=False)
    proteina = models.CharField(max_length=20, choices=PROTEINA, blank=False, null=False)
    descricao = models.CharField( max_length=200)

    def __str__(self):
        return self.descricao
    
class Fila(models.Model):

    cardapio = models.ForeignKey("app.Cardapio", on_delete=models.CASCADE)
    data = models.DateField( auto_now_add=True)
    DIA = (
        ("SEGUNDA", "SEGUNDA"),
        ("TERÇA", "TERÇA"),
        ("QUARTA", "QUARTA"),
        ("QUINTA", "QUINTA"),
        ("SEXTA", "SEXTA"),
    )
    dia = models.CharField(max_length=10, choices=DIA, blank=False, null=False)
    descricao = models.CharField( max_length=200)

    def __str__(self):
        return self.descricao


class Posicao_fila(models.Model):
    aluno = models.ForeignKey("app.Aluno", on_delete=models.CASCADE)
    fila = models.ForeignKey("app.Fila", on_delete=models.CASCADE)
    pisicao = models.IntegerField()

