# Generated by Django 4.0 on 2022-06-24 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_aluno_turma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='turma',
            field=models.CharField(choices=[('1AB', '1AB'), ('2AB', '2AB'), ('3AB', '3AB'), ('1AA', '1AA'), ('2AA', '2AA'), ('3AA', '3AA'), ('1BA', '1BA'), ('2BA', '2BA'), ('3BA', '3BA'), ('1AII', '1AII'), ('2AII', '2AII'), ('3AII', '3AII'), ('1BII', '1BII'), ('2BII', '2BII'), ('3BII', '3BII')], max_length=10),
        ),
    ]
