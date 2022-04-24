from django.urls import path, include
from . import views
from  django.conf import settings
from django.contrib.staticfiles.urls import static
from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path('index/perfiles', views.perfiles, name='index_perfiles'),
    path('index/perfiles/historico', views.reportehistorico, name='index_perfiles_historico'),
    path('index/pdf', views.reporte_personas, name='index_pdf'),
    path('crear/perfil', views.crear_perfil, name='crear_perfil'),
    path('perfil/inhabilitar/<int:id>', views.inhabilitar_perfil, name='inhabilitar_perfil'),
    path('index/perfiles/usuarios', views.perfiles_usuario, name='index_perfiles_usuarios'),
    path('index/perfiles/<int:id>', views.editar_perfil, name='index_editar_perfil'),
    path('index/historico/<int:id>', views.perfiles_resultado, name='index_historico_resultado'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)