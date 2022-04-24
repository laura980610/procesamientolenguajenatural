from django.urls import path, include
from . import views
from  django.conf import settings
from django.contrib.staticfiles.urls import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('index/documentos', views.documentos, name='index_documentos'),
    path('index/informes', views.informes, name='index_informes'),
    path('documentos', views.crear_documento, name='subir_documentos'),
    path('informes', views.crear_informe, name='subir_informe'),
    path('eliminar/informe/<int:id>', views.eliminar_archivo, name='eliminar_archivo'),
    path('usuarios/documentos', views.listar_documentos, name='listar_documentos'),
    path('usuarios/informes', views.listar_informes, name='listar_informes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)