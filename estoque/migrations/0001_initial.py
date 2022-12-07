# Generated by Django 4.1.4 on 2022-12-07 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome Completo', max_length=150, verbose_name='Nome')),
                ('codigo', models.CharField(max_length=64, verbose_name='Código do Produto')),
                ('descricao', models.CharField(max_length=256, verbose_name='Descrição do Produto')),
                ('quantidade', models.CharField(max_length=64, verbose_name='Quantidade do produto')),
                ('undMedida', models.CharField(choices=[('KG', 'Kilograma'), ('MT', 'Metros'), ('CM', 'Centimetros'), ('MG', 'Miligramas'), ('L', 'Litros')], max_length=2, verbose_name='Unidade de medida')),
                ('categoria', models.CharField(choices=[('APARATO FUNERARIO', 'APARATO FUNERARIO'), ('MATERIAL ESCRITORIO', 'MATERIAL ESCRITORIO'), ('MATERIAL AUTOMOTIVO', 'MATERIAL AUTOMOTIVO')], max_length=64, verbose_name='Categoria do Produto')),
            ],
        ),
    ]