from django.urls import path, include
from forum.views import *

urlpatterns = [

    path('', RedirectBaseView, name='redirect'),
    path('avisos/', AvisoBaseView.as_view(), name='avisos'),
    path('avisos/<int:pk>', AvisoDetailView.as_view(), name='avisostopico'),

    path('<secretkey>/', include([
        path('', CategoriaBaseView.as_view(), name='forum'),
        path('subforum/<int:pk>/', SubcategoriaBaseView.as_view(), name='subforum'),
        path('topico/<int:subcategoria>/<int:pk>/', TopicoBaseView.as_view(), name='topico'),
    ])),

    path('<secretkey>/conf/', include([
        path('0/', CategoriaAddView.as_view(), name='addForum'),
        path('subforum/<int:pk>/0', SubcategoriaAddView.as_view(), name='addsubforum'),
        path('topico/<int:pk>/0', TopicoAddView.as_view(), name='addtopico'),
        path('comentario/<int:pk>/0', ComentarioAddView.as_view(), name='addcomentario'),
        path('media/<int:pk>/0', ArquivoAddView.as_view(), name='addarquivo'),

        path('<int:pk>/1', CategoriaEditView.as_view(), name='editforum'),
        path('subforum/<int:pk>/1', SubcategoriaEditView.as_view(), name='editsubforum'),
        path('topico/<int:pk>/1', TopicoEditView.as_view(), name='edittopico'),
        path('comentario/<int:pk>/1', ComentarioEditView.as_view(), name='editcomentario'),
        path('media/<int:pk>/1', ArquivoEditView.as_view(), name='editarquivo'),

        path('<int:pk>/2', CategoriaDeleteView.as_view(), name='deleteforum'),
        path('subforum/<int:pk>/2', SubcategoriaDeleteView.as_view(), name='deletesubforum'),
        path('topico/<int:pk>/2', TopicoDeleteView.as_view(), name='deletetopico'),
        path('comentario/<int:pk>/2', ComentarioDeleteView.as_view(), name='deletecomentario'),
        path('media/<int:pk>/2', ArquivoDeleteView.as_view(), name='deletearquivo'),
    ])),
]