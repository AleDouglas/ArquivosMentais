from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import TemplateView ,ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Importações locais
from users.views import CheckBaseView, CheckDetailView
from .models import *

# Objetivo: redirectionar para página inicial
def RedirectBaseView(request):
    if request.user.is_authenticated:
        return redirect(reverse('forum', args=[str(request.user.secretKey)]))
    else:
        return redirect(reverse('account_login'))

class AvisoBaseView(LoginRequiredMixin, ListView):
    model = Aviso
    context_object_name = 'aviso_lista'
    template_name = 'forum/forum_aviso.html'

class AvisoDetailView(LoginRequiredMixin, DeleteView):
    model = Aviso
    context_object_name = 'aviso'
    template_name = 'forum/aviso.html'

class CategoriaBaseView(CheckBaseView, TemplateView):
    template_name = 'forum/forum_categoria.html'

    def get_context_data(self, **kwargs):
        context = super(CategoriaBaseView, self).get_context_data(**kwargs)
        context['categoria_lista'] = Categoria.objects.filter(autor_key=str(self.kwargs['secretkey']))
        return context

class SubcategoriaBaseView(CheckDetailView, DetailView):
    model = SubCategoria
    context_object_name = 'subcategoria_lista'
    template_name = 'forum/forum_subcategoria.html'

class TopicoBaseView(CheckDetailView, DetailView):
    model = Topico
    context_object_name = 'topico_lista'
    template_name = 'forum/forum_topico.html'

    def get_context_data(self, **kwargs):
        context = super(TopicoBaseView, self).get_context_data(**kwargs)
        context['subcategoria_id'] = self.kwargs['subcategoria']
        return context


### Configurações ###


#Adicionar
class CategoriaAddView(CheckBaseView, CreateView):
    model = Categoria
    template_name = 'forum/forum_form.html'
    fields = ['titulo', 'descricao', 'posicao']

    def get_context_data(self, **kwargs):
        context = super(CategoriaAddView, self).get_context_data(**kwargs)
        context['conf_tipo'] = 0
        return context

    def form_valid(self, form):
        user_key = str(self.request.user.secretKey)
        form.instance.autor_key = user_key
        return super(CategoriaAddView, self).form_valid(form)

class SubcategoriaAddView(CheckDetailView, CreateView):
    model = SubCategoria
    template_name = 'forum/forum_form.html'
    fields = ['titulo', 'descricao', 'posicao']

    def get_context_data(self, **kwargs):
        context = super(SubcategoriaAddView, self).get_context_data(**kwargs)
        context['conf_tipo'] = 0
        return context

    def form_valid(self, form):
        user_key = str(self.request.user.secretKey)
        url_objkey = self.kwargs['pk'] #ID da categoria
        form.instance.autor_key = user_key #Models recebendo Key do usuário
        form.instance.categoria = Categoria.objects.get(id=url_objkey)
        return super(SubcategoriaAddView, self).form_valid(form)

class TopicoAddView(CheckDetailView, CreateView):
    model = Topico
    template_name = 'forum/forum_form.html'
    fields = ['titulo', 'texto', 'fixo']

    def get_context_data(self, **kwargs):
        context = super(TopicoAddView, self).get_context_data(**kwargs)
        context['conf_tipo'] = 0
        return context

    def form_valid(self, form):
        user_key = str(self.request.user.secretKey)
        url_objkey = self.kwargs['pk'] #ID da subcategoria
        form.instance.autor_key = user_key
        form.instance.subcategoria = SubCategoria.objects.get(id=url_objkey)
        return super(TopicoAddView, self).form_valid(form)

class ArquivoAddView(CheckDetailView, CreateView):
    model = Arquivo
    template_name = 'forum/forum_form.html'
    fields = ['titulo', 'descricao', 'posicao','arquivo']

    def get_context_data(self, **kwargs):
        context = super(ArquivoAddView, self).get_context_data(**kwargs)
        context['conf_tipo'] = 0
        return context

    def form_valid(self, form):
        user_key = str(self.request.user.secretKey)
        url_objkey = self.kwargs['pk'] #ID do topico
        form.instance.autor_key = user_key
        form.instance.topico = Topico.objects.get(id=url_objkey)
        return super(ArquivoAddView, self).form_valid(form)

class ComentarioAddView(CheckDetailView, CreateView):
    model = Comentario
    template_name = 'forum/forum_form.html'
    fields = ['comentario', 'posicao']

    def get_context_data(self, **kwargs):
        context = super(ComentarioAddView, self).get_context_data(**kwargs)
        context['conf_tipo'] = 0
        return context

    def form_valid(self, form):
        user_key = str(self.request.user.secretKey)
        url_objkey = self.kwargs['pk'] #ID do topico
        form.instance.autor_key = user_key
        form.instance.topico = Topico.objects.get(id=url_objkey)
        return super(ComentarioAddView, self).form_valid(form)


#Editar
class CategoriaEditView(CheckDetailView, UpdateView):
    model = Categoria
    template_name = 'forum/forum_form.html'
    fields = ['titulo', 'descricao', 'posicao']

    def get_context_data(self, **kwargs):
        context = super(CategoriaEditView, self).get_context_data(**kwargs)
        context['conf_tipo'] = 1
        return context

class SubcategoriaEditView(CheckDetailView, UpdateView):
    model = SubCategoria
    template_name = 'forum/forum_form.html'
    fields = ['titulo', 'descricao', 'posicao']

    def get_context_data(self, **kwargs):
        context = super(SubcategoriaEditView, self).get_context_data(**kwargs)
        context['conf_tipo'] = 1
        return context
    
class TopicoEditView(CheckDetailView, UpdateView):
    model = Topico
    template_name = 'forum/forum_form.html'
    fields = ['titulo', 'texto', 'fixo']

    def get_context_data(self, **kwargs):
        context = super(TopicoEditView, self).get_context_data(**kwargs)
        context['conf_tipo'] = 1
        return context

class ArquivoEditView(CheckDetailView, UpdateView):
    model = Arquivo
    template_name = 'forum/forum_form.html'
    fields = ['titulo', 'descricao','posicao', 'arquivo']

    def get_context_data(self, **kwargs):
        context = super(ArquivoEditView, self).get_context_data(**kwargs)
        context['conf_tipo'] = 1
        return context

class ComentarioEditView(CheckDetailView, UpdateView):
    model = Comentario
    template_name = 'forum/forum_form.html'
    fields = ['comentario','posicao']

    def get_context_data(self, **kwargs):
        context = super(ComentarioEditView, self).get_context_data(**kwargs)
        context['conf_tipo'] = 1
        return context


#Deletar
class CategoriaDeleteView(CheckDetailView, DeleteView):
    model = Categoria
    template_name = 'forum/forum_form.html'

    def get_context_data(self, **kwargs):
        context = super(CategoriaDeleteView, self).get_context_data(**kwargs)
        context['conf_tipo'] = 2
        return context

    def get_success_url(self):
        return reverse_lazy('redirect')

class SubcategoriaDeleteView(CheckDetailView, DeleteView):
    model = SubCategoria
    template_name = 'forum/forum_form.html'

    def get_context_data(self, **kwargs):
        context = super(SubcategoriaDeleteView, self).get_context_data(**kwargs)
        context['conf_tipo'] = 2
        return context
    
    def get_success_url(self):
        return reverse_lazy('redirect')

class TopicoDeleteView(CheckDetailView, DeleteView):
    model = Topico
    template_name = 'forum/forum_form.html'

    def get_context_data(self, **kwargs):
        context = super(TopicoDeleteView, self).get_context_data(**kwargs)
        context['conf_tipo'] = 2
        return context

    def get_success_url(self):
        return reverse_lazy('redirect')

class ArquivoDeleteView(CheckDetailView, DeleteView):
    model = Arquivo
    template_name = 'forum/forum_form.html'

    def get_context_data(self, **kwargs):
        context = super(ArquivoDeleteView, self).get_context_data(**kwargs)
        context['conf_tipo'] = 2
        return context

    def get_success_url(self):
        return reverse_lazy('redirect')

class ComentarioDeleteView(CheckDetailView, DeleteView):
    model = Comentario
    template_name = 'forum/forum_form.html'

    def get_context_data(self, **kwargs):
        context = super(ComentarioDeleteView, self).get_context_data(**kwargs)
        context['conf_tipo'] = 2
        return context

    def get_success_url(self):
        return reverse_lazy('redirect')