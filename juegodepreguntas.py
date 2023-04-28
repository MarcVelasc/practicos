#Programa de preguntas que un usuario debe hacer y dar las respuestas "si" "no"
#Inicializamos vectores para la preguntas y respuestas
import random
preguntas = []
respuestas_correctas = []
#vectores para si y para no
respuesta_si= []
respuesta_no= []
#vector para preguntas incorretas conseccutivamente
preguntas_incorrectas_consecutivamente= []
n = int(input("¿Cuántas preguntas deseas hacer? "))

#Pedimos al usuario que ingrese las preguntas y respuestas
for i in range(n):
    pregunta = input("Ingresa la pregunta número {}: ".format(i+1))
    respuesta = input("¿Es cierto? (si/no): ")
    preguntas.append(pregunta)
    respuestas_correctas.append(respuesta.lower())
#preguntamos las pregutas al jugador y almacenamos las respuestas   
preguntas_correctas = 0
preguntas_incorrectas = 0
pregunta_anterior_correcta = True
    

#inicializamos un vector para almacenar las respuestas
respuesta_jugador=[]

#preguntamos las preguntas al jugador y almacenamos las respuestas
for pregunta in preguntas:
    respuesta = input(pregunta + " (si/no): ")
    respuestas_jugador.append(respuesta.lower())
     if respuesta.lower() == "si":
        respuestas_si.append(pregunta)
         if respuestas_correctas[i] == "si":
            preguntas_correctas += 1
            pregunta_anterior_correcta = True
        else:
            preguntas_incorrectas += 1
            pregunta_anterior_correcta = False
            preguntas_incorrectas_consecutivas.
    elif respuesta.lower() == "no":
        respuestas_no.append(pregunta)
        if respuestas_correctas[i] == "no":
            preguntas_correctas += 1
            pregunta_anterior_correcta = True
        else:
            preguntas_incorrectas += 1
            pregunta_anterior_correcta = False
            preguntas_incorrectas_consecutivas.append(pregunta)
    
#calculamos el porcentaje de respuestas correctas
respuestas_correctas_jugador = sum([respuestas_jugador[i] == respuestas_correctas[i] for i in range(n)])
preguntas_de_jugador= sum
porcentaje_correctas = respuestas_correctas_jugador / n * 100

#aqui mostramos el resultado del jugador
print("Has acertado el {}% de las preguntas.".format(porcentaje_correctas))
preguntas_jugador= preguntas
respuestas_jugador=respuesta_jugador
respuesta_si=respuesta_si
respuesta_no=respuesta_no
preguntas_incorrectas_consecutivamente=preguntas_incorrectas_consecutivamente










