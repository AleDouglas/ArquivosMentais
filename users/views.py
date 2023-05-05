from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.http.response import FileResponse
from django.http import HttpResponseForbidden

from forum.models import Arquivo

# Objetivo: Verificar se o usuário está logado, além disso, verificar se rota URL contém a mesma secretkey do usuário logado
class CheckBaseView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return str(self.request.user.secretKey) == str(self.kwargs['secretkey'])

    def handle_no_permission(self):
        return redirect(reverse('redirect',))

# Objetivo: Realizar as mesmas verificações, porém, ele verificar se parâmetros da rota está correto
class CheckDetailView(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        user_key = str(self.request.user.secretKey) # Pegando SECRETKEY do usuário
        url_userkey = self.kwargs['secretkey'] # Pegando SECRETKEY da URL
        url_objkey = self.kwargs['pk'] # Pegando ID da URL
        obj_key = self.model.objects.get(id=url_objkey).autor_key # Pegando ID do objeto

        return ((user_key == url_userkey) and (user_key == obj_key)) # Verificando

    def handle_no_permission(self):
        return redirect(reverse('redirect',))


# Objetivo: Restringir acesso a rota de mídia
def media_access(request, path):    
    access_granted = False
    user = request.user
    if user.is_authenticated:
        get_path = f"arquivo/{path}"
        get_obj = Arquivo.objects.get(arquivo=get_path) #Pegando arquivo a ser acessado
        if user.is_staff:
            # Caso seja Administrator, acesso a rota está garantido
            access_granted = True
        else:
            # Permite o acesso apenas se a Key do usuário corresponder a Key do Arquivo
            if get_obj.autor_key == user.secretKey:
                access_granted = True

    if access_granted:
        response = FileResponse(get_obj.arquivo)
        return response
    else:
        return HttpResponseForbidden('Acesso proíbido! Contate o Administrator.')
