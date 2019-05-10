# Generated by Django 2.2.1 on 2019-05-09 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senha', models.CharField(max_length=50)),
                ('nick', models.CharField(max_length=50)),
                ('pontuacao', models.IntegerField()),
                ('moedas', models.IntegerField()),
                ('nivel', models.IntegerField()),
                ('arena', models.CharField(max_length=300)),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
