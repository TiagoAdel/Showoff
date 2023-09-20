# Generated by Django 4.2.5 on 2023-09-18 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_funcionario_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Actualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('recurso', models.CharField(max_length=100, verbose_name='Recurso')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete')], max_length=12, verbose_name='Icone')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]