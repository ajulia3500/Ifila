# Generated by Django 4.0 on 2022-06-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_cardapio_fila_cardapio'),
    ]

    operations = [
        migrations.AddField(
            model_name='fila',
            name='descricao',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]