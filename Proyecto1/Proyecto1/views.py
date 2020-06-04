from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):

    def __init__(self, nombre, apellido):

        self.nombre = nombre
        self.apellido = apellido


def saludo(request): #primera vista

    temas_del_curso=["Plantillas","Modelos","Formularios","Vistas","Despliege"]

    p1=Persona("Carlos", "Hiram")

    #nombre="Marlene"

    #apellido="Díaz"

    ahora=datetime.datetime.now()

    doc_externo=open("C:/Users/cguillen/Desktop/DIRAM/PYTHON/CURSO DJANGO/Proyecto1/Proyecto1/PLANTILLAS/miplantilla.html")
    
    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora, "Temas":temas_del_curso})

    documento=plt.render(ctx)

    return HttpResponse(documento)

def despedida(request): #segunda vista
    return HttpResponse("Hasta luego")

def givedate(request):
    fecha_actual=datetime.datetime.now()
    documento="<html><body><h2>Fecha y hora actuales %s <html<body><h2>" % fecha_actual
    return HttpResponse(documento)

def calculaedad(request,edad,agno):
    #edadactual=18 
    periodo=agno-2020
    edadfutura=edad+periodo
    documento="<html><body><h2>En el año %s tendrás %s años<html<body><h2>" %(agno, edadfutura)
    return HttpResponse(documento)