# Generated by Django 2.2.1 on 2019-05-09 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(max_length=300),
        ),
    ]
