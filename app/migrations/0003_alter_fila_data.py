# Generated by Django 4.0 on 2022-06-23 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_aluno_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fila',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
    ]
