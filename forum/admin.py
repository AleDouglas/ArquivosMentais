from django.contrib import admin
from .models import Categoria, SubCategoria ,Topico, Comentario, Arquivo, Aviso

# Responsável pelos Avisos
class AvisoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fixo')

admin.site.register(Aviso, AvisoAdmin)

# Responsável pela Categoria
class SubCategoriaInLine(admin.TabularInline):
    model = SubCategoria

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [SubCategoriaInLine]
    list_display = ("id","titulo", 'posicao', 'autor_key')

admin.site.register(Categoria, CategoriaAdmin)


# Responsável pela SubCategoria
class TopicoInLine(admin.TabularInline):
    model = Topico

class SubCategoriaAdmin(admin.ModelAdmin):
    inlines = [TopicoInLine]
    list_display = ("id","titulo", 'posicao',)

admin.site.register(SubCategoria, SubCategoriaAdmin)


# Responsável pelo Topico
class ArquivoInLine(admin.TabularInline):
    model = Arquivo

class ComentarioInline(admin.TabularInline): 
    model = Comentario

class TopicoAdmin(admin.ModelAdmin):
    inlines = [ArquivoInLine,ComentarioInline]
    list_display = ("id","titulo", "subcategoria",)


admin.site.register(Topico, TopicoAdmin)