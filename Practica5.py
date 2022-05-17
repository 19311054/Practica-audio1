#Practica-5 Manejo de metodos
#Luis Alberto Aguilar

#Manipulación de luces en ciclo de 60 minutos

#4 tiempos (15min)
#4 tonos
#2 colores

#trigger

#Declaracion de variables

varTiempo=15
varColorI="#F7FF87"
varColorF="#FFF"

varTono1=.25
varTono2=.5
varTono3=.75
varTono4=1

#Declaracion de funciones

def inicio():
    etapaUno()

def Finalizar():
    print("Luces encendidad a todo color,")

def timer(int):
    print("Inicio de conteo de 15")
    #Todo falta funcion que cuente los 15 minutos.
    print("Finaliza el conteo de 15")


def etapaUno():
    print("Etapa Uno Iniciada")
    timer(varTiempo)
    luces(varTono1, varColorI)
    print("Etapa uno finalizada")
    etapaDos()

def etapaDos():
    print("Etapa Dos Iniciada")
    timer(varTiempo)
    luces(varTono2, varColorI)
    print("Etapa Dos finalizada")
    etapaTres()

def etapaTres():
    print("Etapa Tres Iniciada")
    timer(varTiempo)
    luces(varTono3, varColorF)
    print("Etapa Tres finalizada")
    etapaCuatro()

def etapaCuatro():
    print("Etapa Cuatro Iniciada")
    timer(varTiempo)
    luces(varTono4, varColorF)
    print("Etapa Cuatro finalizada")
    Finalizar()

#Trigger Inicial
print("inicio de Manipulacion de luces")