from django.shortcuts import render, redirect
from .forms import DocumentoForm
from .models import archivos
from django.http import HttpResponseRedirect
from django.contrib import messages

def crear_documento(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            formulario_documento = DocumentoForm(request.POST or None, request.FILES or None)
            if formulario_documento.is_valid():
                formulario_documento.save()
                messages.add_message(request=request, level=messages.SUCCESS, message="Documento registrado con éxito")
                return redirect('usersAuth:index_documentos')
            return render(request, 'admin/subir_documento.html', {'formulario_documento': formulario_documento})
        else:
            return render(request, 'usuario/index.html')
    else:
        return render(request, 'pages/index.html')

def documentos(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            cont = 0
            lista_documentos = archivos.objects.filter(tipo_id=1)
            if not lista_documentos:
                cont = 1
            return render(request, 'admin/documentos.html', {'lista_documentos': lista_documentos, 'cont': cont})
        else:
            return render(request, 'usuario/index.html')
    else:
        return render(request, 'pages/index.html')

def informes(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            cont = 0
            lista_informes = archivos.objects.filter(tipo_id=2)
            if not lista_informes:
                cont = 1
            return render(request, 'admin/informes.html', {'lista_informes': lista_informes, 'cont': cont})
        else:
            return render(request, 'usuario/index.html')
    else:
        return render(request, 'pages/index.html')

def crear_informe(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            formulario_informe = DocumentoForm(request.POST or None, request.FILES or None)
            if formulario_informe.is_valid():
                formulario_informe.save()
                messages.add_message(request=request, level=messages.SUCCESS, message="Informe registrado con éxito")
                return redirect('usersAuth:index_informes')
            return render(request, 'admin/subir_informe.html', {'formulario_informe': formulario_informe})
        else:
            return render(request, 'usuario/index.html')
    else:
        return render(request, 'pages/index.html')

def eliminar_archivo(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            archivo = archivos.objects.get(id=id)
            archivo.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return render(request, 'usuario/index.html')
    else:
        return render(request, 'pages/index.html')


def listar_documentos(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == False:
            cont = 0
            listar_documento = archivos.objects.filter(tipo_id=1)
            if not listar_documento:
                cont = 1
            return render(request, 'usuario/documentacion_usuarios.html', {'listar_documento': listar_documento, 'cont': cont})
        else:
            return render(request, 'admin/principal.html')
    else:
        return render(request, 'pages/index.html')


def listar_informes(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == False:
            cont = 0
            listar_informe = archivos.objects.filter(tipo_id=2)
            if not listar_informe:
                cont = 1
            return render(request, 'usuario/informes_usuarios.html', {'listar_informe': listar_informe, 'cont': cont})
        else:
            return render(request, 'admin/principal.html')
    else:
        return render(request, 'pages/index.html')

