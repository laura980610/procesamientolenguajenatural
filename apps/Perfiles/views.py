from string import punctuation
from django.http import HttpResponseRedirect, HttpResponse
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .forms import PerfilesForm
from .models import perfiles_ocupacionales, historico
from django.shortcuts import render, redirect
from django.contrib import messages

language_stopwords = stopwords.words('spanish')

non_words = list(punctuation)


from .reportes import ReportePersona

def reporte_personas(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="personas.pdf"'
    r = ReportePersona()
    response.write(r.run())
    return response

def reportehistorico(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            lista_perfiles = historico.objects.all()
            cont = 0
            if not lista_perfiles:
                cont = 1
            return render(request, 'admin_perfiles/historico.html', {'lista_perfiles': lista_perfiles, 'cont': cont})
        else:
            return render(request, 'usuario/index.html')
    else:
        return render(request, 'pages/index.html')

def perfiles_resultado(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            characters = "[], "
            resultado = historico.objects.get(id=id)
            arrayperfiles = resultado.perfiles
            cont = 1
            lista_perfiles = perfiles_ocupacionales.objects.all()
            for x in range(len(characters)):
                arrayperfiles = arrayperfiles.replace(characters[x], "")
            if arrayperfiles != "":
                cont=0
                arrayperfiles = list(arrayperfiles)
                idfiltro = str(arrayperfiles[0])
                idfiltro = int(idfiltro)
                arrayperfiles.pop(0)
                lista_perfiles = perfiles_ocupacionales.objects.filter(id=int(idfiltro))
                for idperfil in arrayperfiles:
                    idperfil2 = str(idperfil)
                    idbusqueda = int(idperfil2)
                    lista_perfiles = lista_perfiles | perfiles_ocupacionales.objects.filter(id=idbusqueda)
            return render(request, 'admin_perfiles/historico_busqueda.html', {'lista_perfiles': lista_perfiles, 'cont': cont})
        else:
            return render(request, 'usuario/index.html')
    else:
        return render(request, 'pages/index.html')

def perfiles(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            lista_perfiles = perfiles_ocupacionales.objects.filter(estado_id=1)
            cont = 0
            if not lista_perfiles:
                cont = 1
            return render(request, 'admin_perfiles/index.html', {'lista_perfiles': lista_perfiles, 'cont': cont})
        else:
            return render(request, 'usuario/index.html')
    else:
        return render(request, 'pages/index.html')

def crear_perfil(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            formulario_perfil = PerfilesForm(request.POST or None, request.FILES or None)
            if formulario_perfil.is_valid():
                formulario_perfil.save()
                return redirect('usersAuth:index_perfiles')
            return render(request, 'admin_perfiles/create.html', {'formulario_perfil': formulario_perfil})
        else:
            return render(request, 'usuario/index.html')
    else:
        return render(request, 'pages/index.html')

def inhabilitar_perfil(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            perfil = perfiles_ocupacionales.objects.get(id=id)
            perfil.estado_id_id = 2
            perfil.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return render(request, 'usuario/index.html')
    else:
        return render(request, 'pages/index.html')

def eliminacion_stopwords(text):
    texto_limpio = ''
    for word in text.split():
        if word in language_stopwords or word in non_words:
            continue
        else:
            texto_limpio += word + ' '
    return texto_limpio

def eliminar_puntuacion(string_inicial):
    for word in non_words:
        string_inicial = string_inicial.replace(word, '')
    return string_inicial

def procesar_texto(textnlp):
    text_content = textnlp
    # All to lower case
    text_content = text_content.lower()
    # Remove punctuation and spanish stopwords
    text_content = eliminar_puntuacion(text_content)
    text_content = eliminacion_stopwords(text_content)
    return text_content

def perfiles_usuario(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == False:
            lista_perfiles = perfiles_ocupacionales.objects.filter(estado_id=1)
            cont = 0
            if not lista_perfiles:
                cont = 1
            querysetfiltro = request.GET.get("filtro")
            querysetbusqueda = request.GET.get("busqueda")
            text = str(querysetbusqueda)
            nlp_text = procesar_texto(text)

            if querysetfiltro == '1':
                vector_perfiles = []
                for textprocesamiento in lista_perfiles:
                    institucion = str(textprocesamiento.universidad)
                    nlp_registro = procesar_texto(institucion)
                    # TF-IDF
                    vectorizer = TfidfVectorizer()
                    X = vectorizer.fit_transform([nlp_text, nlp_registro])
                    similarity_matrix = cosine_similarity(X, X)
                    if(similarity_matrix[0][1] >= 0.7):
                        vector_perfiles = vector_perfiles + [textprocesamiento.id]
                if vector_perfiles:
                    idfiltro = vector_perfiles[0]
                    vector_perfiles.pop(0)
                    perfil_array = perfiles_ocupacionales.objects.filter(id=idfiltro)
                    for idperfil in vector_perfiles:
                        perfil_array = perfil_array | perfiles_ocupacionales.objects.filter(id=idperfil)
                    return render(request, 'usuariosperfil/filtro.html', {'perfil_array': perfil_array})
                else:
                    messages.error(request,'LO SENTIMOS, NO ENCONTRAMOS COINCIDENCIAS')
                    return render(request, 'usuariosperfil/index.html',{'lista_perfiles': lista_perfiles, 'cont': cont})
            elif querysetfiltro == '2':
                vector_perfiles = []
                for textprocesamiento in lista_perfiles:
                    programa = str(textprocesamiento.programa)
                    nlp_registro = procesar_texto(programa)
                    # TF-IDF
                    vectorizer = TfidfVectorizer()
                    X = vectorizer.fit_transform([nlp_text, nlp_registro])
                    similarity_matrix = cosine_similarity(X, X)
                    if(similarity_matrix[0][1] >= 0.2):
                        vector_perfiles = vector_perfiles + [textprocesamiento.id]
                    #print(similarity_matrix[0][1], similarity_matrix[1][1])
                if vector_perfiles:
                    idfiltro = vector_perfiles[0]
                    vector_perfiles.pop(0)
                    perfil_array = perfiles_ocupacionales.objects.filter(id=idfiltro)
                    lista_perfiles = perfiles_ocupacionales.objects.all()
                    for idperfil in vector_perfiles:
                        perfil_array = perfil_array | perfiles_ocupacionales.objects.filter(id=idperfil)
                    return render(request, 'usuariosperfil/filtro.html', {'perfil_array': perfil_array})
                else:
                    messages.error(request, 'LO SENTIMOS, NO ENCONTRAMOS COINCIDENCIAS')
                    return render(request, 'usuariosperfil/index.html', {'lista_perfiles': lista_perfiles, 'cont': cont})
            elif querysetfiltro == '3':
                vector_perfiles = []
                for textprocesamiento in lista_perfiles:
                    perfil = str(textprocesamiento.perfil)
                    nlp_registro = procesar_texto(perfil)
                    # TF-IDF
                    vectorizer = TfidfVectorizer()
                    X = vectorizer.fit_transform([nlp_text, nlp_registro])
                    similarity_matrix = cosine_similarity(X, X)
                    if(similarity_matrix[0][1] >= 0.2):
                        vector_perfiles = vector_perfiles + [textprocesamiento.id]
                p = historico(busqueda=text, perfiles=vector_perfiles)
                p.save()
                if vector_perfiles:

                    idfiltro = vector_perfiles[0]
                    vector_perfiles.pop(0)
                    perfil_array = perfiles_ocupacionales.objects.filter(id=idfiltro)
                    lista_perfiles = perfiles_ocupacionales.objects.all()
                    for idperfil in vector_perfiles:
                        perfil_array = perfil_array | perfiles_ocupacionales.objects.filter(id=idperfil)
                    return render(request, 'usuariosperfil/filtro.html', {'perfil_array': perfil_array})
                else:
                    messages.error(request, 'LO SENTIMOS, NO ENCONTRAMOS COINCIDENCIAS')
                    return render(request, 'usuariosperfil/index.html', {'lista_perfiles': lista_perfiles, 'cont': cont})
            else:
                lista_perfiles = perfiles_ocupacionales.objects.all()
                return render(request, 'usuariosperfil/index.html', {'lista_perfiles': lista_perfiles, 'cont': cont})
        else:
            return render(request, 'admin/principal.html')
    else:
        return render(request, 'pages/index.html')

def editar_perfil(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            perfiles = perfiles_ocupacionales.objects.get(id = id)
            if request.method == 'GET':
                formulario_perfil = PerfilesForm(instance=perfiles)
            else:
                formulario_perfil = PerfilesForm(request.POST, instance=perfiles)
                if formulario_perfil.is_valid():
                    formulario_perfil.save()
                return redirect('usersAuth:index_perfiles')
            return render(request, 'admin_perfiles/create.html', {'formulario_perfil': formulario_perfil})
        else:
            return render(request, 'usuario/index.html')
    else:
        return render(request, 'pages/index.html')