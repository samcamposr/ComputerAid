# Generated by Django 2.0.13 on 2019-05-16 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('senha', models.CharField(max_length=50)),
                ('nick', models.CharField(max_length=50)),
                ('pontuacao', models.IntegerField()),
                ('moedas', models.IntegerField()),
                ('nivel', models.IntegerField()),
                ('arena', models.CharField(max_length=300)),
                ('ano', models.CharField(max_length=300)),
            ],
        ),
    ]
