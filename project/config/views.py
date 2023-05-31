from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render
from datetime import datetime

def saludo(request):
    nombre = input('Escribe tu nombre: ')
    return HttpResponse(f"<h1> Hola {nombre} <h1>") 

def saludo_con_input(request):
    nombre = input("Dime tu nombre: ")
    return HttpResponse(f"Hola {nombre}")

def segunda_vista(request):
    return HttpResponse("segunda vista")


def dia_de_hoy(request):
    from datetime import datetime
    dia = datetime.now()
    return HttpResponse (f"<h1> {dia} <h1>" )

def nombre(request, nombre:str, apellido: str):
    nombre= nombre.capitalize()
    apellido =apellido.capitalize()
    return HttpResponse(f"{apellido},{nombre}")

def probando_template(request):
    mi_html = open("./templates/template1.html", encoding="utf-8")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)

def numero_aleatorio(request):
    import random

    numero = random.randint(1, 6)
    if numero == 6:
        return HttpResponse(f"<h1> Has tirado el dado: 🎲{numero}✨ ¡Suerte! </h1")
    else:
        return HttpResponse(f"<h1> Has tirado el dado: 🎲{numero} <br> Sigue intentando hasta sacar 6 </h1")
    


def probando_template_render(request):
    
    nombre= "Louis"
    apellido = "Beethoven"
    datos = {"nombre": nombre, "apellido": apellido}
    fecha_hora = datetime.now()
    fecha_hora_f = fecha_hora.strftime(r"%d/%m/%Y a las %H:%M:%S.%f")
    datos['fecha_hora'] = fecha_hora_f
    return render(request,"template1.html",context=datos)

def probando_template2(request):
    lista_de_notas = [2,2,3,7,5]
    contexto = {"notas": lista_de_notas}
    return render(request, "template2.html", context=contexto )