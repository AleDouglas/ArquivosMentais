from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Objetivo: Serve para postar avisos/updates visíveis para TODOS OS USUÁRIOS
class Aviso(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    titulo = models.CharField('Título',max_length=200)
    descricao = models.CharField('Descrição',max_length=400, blank=True)
    posicao = models.IntegerField('Posição', blank=True, default=0)
    texto = models.TextField('Conteúdo do Tópico')
    fixo = models.BooleanField('Fixo', default=False)

    class Meta:
        ordering = ["-fixo","posicao","-criado",]

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    autor_key = models.CharField('Chave', max_length=40, editable=False)
    titulo = models.CharField('Título',max_length=200)
    descricao = models.CharField('Descrição',max_length=400, blank=True)
    posicao = models.IntegerField('Posição', blank=True, default=0)

    class Meta:
        indexes = [models.Index(fields=['id'], name='id_comentario')]
        ordering = ["posicao"]

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('forum', args=[str(self.autor_key)])

class SubCategoria(models.Model):
    autor_key = models.CharField('Chave', max_length=40, editable=False)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name='subcategoria')
    titulo = models.CharField('Título',max_length=200)
    descricao = models.CharField('Descrição',max_length=400, blank=True)
    posicao = models.IntegerField('Posição', blank=True, default=0)

    class Meta:
        ordering = ["posicao"]

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('forum', args=[str(self.autor_key)])

class Topico(models.Model):
    autor_key = models.CharField('Chave', max_length=40, editable=False)
    subcategoria = models.ForeignKey(SubCategoria,on_delete=models.CASCADE,related_name='topico')
    criado = models.DateField('Data de criação', auto_now_add=True)
    titulo = models.CharField('Título',max_length=100)
    texto = models.TextField('Conteúdo do Tópico')
    fixo = models.BooleanField('Fixo', default=False)

    class Meta:
        indexes = [models.Index(fields=['id'], name='id_topico')]
        ordering = ["-fixo", "-criado"]

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('topico', args=[str(self.autor_key), str(self.id)])

class Arquivo(models.Model):
    autor_key = models.CharField('Chave', max_length=40, editable=True)
    topico = models.ForeignKey(Topico,on_delete=models.CASCADE,related_name='arquivo')
    titulo = models.CharField('Título',max_length=100)
    descricao = models.CharField('Descrição',max_length=1000, blank=True)
    arquivo = models.FileField(upload_to="arquivo/")
    posicao = models.IntegerField('Posição', blank=True, default=0)


    class Meta:
        ordering = ["posicao"]

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('topico', args=[str(self.autor_key), str(self.topico.id)])

class Comentario(models.Model):
    autor_key = models.CharField('Chave', max_length=40, editable=False)
    topico = models.ForeignKey(Topico,on_delete=models.CASCADE,related_name='comentario')
    criado = models.DateField('Data de criação', auto_now_add=True)
    comentario = models.TextField('Comentário')
    posicao = models.IntegerField('Posição', blank=True, default=0)

    class Meta:
        ordering = ["-criado", "posicao"]

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('topico', args=[str(self.autor_key), str(self.topico.id)])

