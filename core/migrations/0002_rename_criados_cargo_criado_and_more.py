# Generated by Django 4.2.5 on 2023-09-15 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargo',
            old_name='criados',
            new_name='criado',
        ),
        migrations.RenameField(
            model_name='cargo',
            old_name='modificados',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='criados',
            new_name='criado',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='modificados',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='servico',
            old_name='criados',
            new_name='criado',
        ),
        migrations.RenameField(
            model_name='servico',
            old_name='modificados',
            new_name='modificado',
        ),
    ]