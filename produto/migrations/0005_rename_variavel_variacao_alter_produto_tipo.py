# Generated by Django 4.0.1 on 2022-01-21 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_rename_variacao_variavel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Variavel',
            new_name='Variacao',
        ),
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('V', 'Variavel'), ('S', 'Simples')], default='V', max_length=1),
        ),
    ]