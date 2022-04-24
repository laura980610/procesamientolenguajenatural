from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = 'usersAuth'

urlpatterns = [
    path('principal/', views.principal, name='principal'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('accounts/login/ingreso/', views.ingreso, name='ingreso'),
    path('usuarios/activos', views.usuarios_activos, name='usuarios_activos'),
    path('usuarios/inactivos', views.usuarios_inactivos, name='usuarios_inactivos'),
    path('rechazar/<int:id>', views.rechazar_preregistro, name='rechazar_registro'),
    path('usuarios/aceptacion/<int:id>', views.aceptar_preregistro, name='aceptar'),
    path('index/usuarios', views.index_usuario, name='index_usuarios'),
    path('index/nosotros', views.index_nosotros, name='index_nosotros'),
    path('', include('apps.Documentos.urls')),
    path('', include('apps.Perfiles.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





