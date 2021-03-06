from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
UserModel = get_user_model()
from django.template.loader import get_template
from  django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .forms import RegisterUserForm


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('rxWod:index'))
    else:
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                messages.add_message(request=request, level=messages.SUCCESS, message="Su registro se ha realizado con éxito")
                return render(request, 'pages/index.html')
            else:
                if form.errors:
                    for key, values in form.errors.as_data().items():
                        if key == 'email':
                            messages.info(request, 'Correo registrado')
                            break
                        else:
                            for error_value in values:
                                messages.info(request, '%s' % (error_value.message))
                return HttpResponseRedirect(reverse('usersAuth:register'))
        else:
            form = RegisterUserForm()
            context = {
                'form': form
            }
            return render(request, 'usersAuth/register.html', context)

def principal(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            return render(request, 'admin/principal.html')
        else:
            return render(request, 'usuario/index.html')
    else:
        return render(request, 'pages/index.html')

def index(request):
    return render(request, 'pages/index.html')

def index_nosotros(request):
    return render(request, 'pages/nosotros.html')


def ingreso(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            return render(request, 'admin/principal.html')
        else:
            return render(request, 'usuario/index.html')
    # Do something for authenticated users.
    else:
        return render(request, 'pages/index.html')

def index_usuario(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == False:
            return render(request, 'usuario/index.html')
        else:
            return render(request, 'admin/principal.html')
    else:
        return render(request, 'pages/index.html')


def usuarios_activos(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            lista_usuarios = User.objects.all()
            return render(request, 'admin/usuarios_activos.html', {'lista_usuarios': lista_usuarios})
        else:
            return render(request, 'usuario/index.html')
    else:
        return render(request, 'pages/index.html')

def usuarios_inactivos(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            lista_usuarios = User.objects.all()
            return render(request, 'admin/usuarios_inactivos.html', {'lista_usuarios': lista_usuarios})
        else:
            return render(request, 'usuario/index.html')
    else:
        return render(request, 'pages/index.html')

def send_email(nombre, mail, estado_id):
        context = {'nombre': nombre, 'estado_id': estado_id}
        template = get_template('admin/correo.html')
        content = template.render(context)
        email = EmailMultiAlternatives(
            'PROCESAMIENTO DE LENGUAJE NATURAL',
            'Procesamiento de lenguaje natural',
            settings.EMAIL_HOST_USER,
            [mail]
        )
        email.attach_alternative(content, 'text/html')
        email.send()


def aceptar_preregistro(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            preregistro = User.objects.get(id=id)
            preregistro.is_active = True
            preregistro.save()
            mail = preregistro.email
            nombre = preregistro.first_name
            estado_id = preregistro.is_active
            send_email(nombre, mail, estado_id)
            messages.add_message(request=request, level=messages.SUCCESS, message="Se ha enviado el correo de notificación")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'pages/index.html')


def rechazar_preregistro(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            preregistro = User.objects.get(id=id)
            preregistro.is_active = False
            preregistro.save()
            mail = preregistro.email
            nombre = preregistro.first_name
            estado_id = preregistro.is_active
            send_email(nombre, mail, estado_id)
            messages.add_message(request=request, level=messages.SUCCESS, message="Se ha enviado el correo de notificación")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'pages/index.html')





