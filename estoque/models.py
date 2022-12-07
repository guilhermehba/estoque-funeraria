from django.db import models
from django.db.models.fields import DateTimeField
from django.core.validators import FileExtensionValidator

UND_CHOICE = (
    (u"KG", "Kilograma"),
    (u"MT", "Metros"),
    (u"CM", "Centimetros"),
    (u"MG", "Miligramas"),
    (u"L", "Litros"),
)

CATEGORIA_CHOICE = (
    (u"APARATO FUNERARIO", "APARATO FUNERARIO"),
    (u"MATERIAL ESCRITORIO", "MATERIAL ESCRITORIO"),
    (u"MATERIAL AUTOMOTIVO","MATERIAL AUTOMOTIVO"),
)


class produto (models.Model):
    nome = models.CharField(verbose_name='Nome',
                            max_length=150,
                            help_text='Nome Completo')
    codigo = models.CharField(verbose_name='Código do Produto',
                              max_length=64)
    descricao = models.CharField(verbose_name='Descrição do Produto',
                                 max_length=256)
    quantidade = models.CharField(verbose_name='Quantidade do produto',max_length=64)
    undMedida = models.CharField(verbose_name='Unidade de medida',
        max_length=2, choices=UND_CHOICE, blank=True, null=True)
    categoria = models.CharField(verbose_name='Categoria do Produto', max_length=64,choices=CATEGORIA_CHOICE)
# Create your models here.
