from email.policy import default
from enum import unique
from pickletools import optimize
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from PIL import Image
import os
from django.conf import settings
from django.utils.text import slugify
from utils.price_format import format_value



class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to='produto_imagens/%Y/%m/',
        blank=True,
        null=True,
        )
    slug = models.SlugField(unique=True, blank=True,null=True)
    preco_marketing = models.FloatField(verbose_name='Preço')
    preco_marketing_promocional = models.FloatField(default=0,verbose_name='Preço Promo',blank=True,null=False)
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V','Variavel'),
            ('S','Simples'),
        )
    )


    def __str__(self):
        return self.nome

    def get_preco_formatado(self):
        formatado = format_value(self.preco_marketing)   
        return formatado
    #muda o nome representativo da função para a 'Preço'
    get_preco_formatado.short_description = 'Preço'

    def get_preco_formatado_desconto(self):
        formatado = format_value(self.preco_marketing_promocional)
        return formatado
    get_preco_formatado_desconto.short_description = 'Desconto'

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return
        
        new_height = round((new_width * original_height) / original_width)
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )


    def save(self,*args,**kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug
        super().save(*args,**kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)


class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome
    
    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
