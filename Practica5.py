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

def finalizar():
    print("Luces encendidad a todo color,")

def timer(minutos):
    print("Inicio de conteo de 15" + str(minutos))
    #Todo falta funcion que cuente los 15 minutos.
    print("Finaliza el conteo de 15")

def luces(tono, color):
    print("Se establece el color y el tono")
    print("Color establecido a " + color)
    print("tono establecido a" + str(tono))

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
    finalizar()

#Trigger Inicial
print("inicio de Manipulacion de luces")

inicio()