from django.http import HttpResponse
from django.template import Context, Template

def saludo(request):
    nombre = input('Escribe tu nombre: ')
    return HttpResponse(f"<h1> Hola {nombre} <h1>") 

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

def mi_template(request):
    from .settings import BASE_DIR
    mi_html = open(BASE_DIR / "templates/template1.html")
    plantilla = Template(mi_html.read())
    datos = {'nombre': 'Juan', 'apellido': 'Perez'}
    contexto = Context(datos)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)