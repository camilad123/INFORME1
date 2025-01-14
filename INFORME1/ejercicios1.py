# -*- coding: utf-8 -*-
"""ejercicios1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-uJaQZdGyCIopfhnBGFJs43Lv6qp8W4e
"""

#Ejercicio 1: Calcular cual es la distancia menor entre dos puntos 

from math import sqrt

class Punto:
   def __init__(self, x, y, z):
       self.x = x
       self.y = y
       self.z = z


def CalcularDistancia(p1,p2):

#La siguiente funcion es para calcular la distancia entre dos puntos en R3  
     return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

punto1 = Punto(2, 2, 3)
punto2 = Punto(2, 3, 4)
punto3 = Punto(1, 1, 3) 
punto4 = Punto(0.5, 0.5, 2) 
punto5 = Punto(1, 2, 1) 
punto6 = Punto(1, 0.5, 1)
punto7 = Punto(3, 2, 0.5)
punto8 = Punto(3, 1, 2)
punto9 = Punto(0, 0, 0)
punto10 = Punto(2, 0, 0.5) 



print(CalcularDistancia(punto1,punto2))
print(CalcularDistancia(punto1,punto3))
print(CalcularDistancia(punto1,punto4))
print(CalcularDistancia(punto1,punto5))
print(CalcularDistancia(punto1,punto6))
print(CalcularDistancia(punto1,punto7))
print(CalcularDistancia(punto1,punto8))
print(CalcularDistancia(punto1,punto9))
print(CalcularDistancia(punto1,punto10))
print(CalcularDistancia(punto2,punto3))
print(CalcularDistancia(punto2,punto4))
print(CalcularDistancia(punto2,punto5))
print(CalcularDistancia(punto2,punto6))
print(CalcularDistancia(punto2,punto7))
print(CalcularDistancia(punto2,punto8))
print(CalcularDistancia(punto2,punto9))
print(CalcularDistancia(punto2,punto10))
print(CalcularDistancia(punto3,punto4))
print(CalcularDistancia(punto3,punto5))
print(CalcularDistancia(punto3,punto6))
print(CalcularDistancia(punto3,punto7))
print(CalcularDistancia(punto3,punto8))
print(CalcularDistancia(punto3,punto9))
print(CalcularDistancia(punto3,punto10))
print(CalcularDistancia(punto4,punto5))
print(CalcularDistancia(punto4,punto6))
print(CalcularDistancia(punto4,punto7))
print(CalcularDistancia(punto4,punto8))
print(CalcularDistancia(punto4,punto9))
print(CalcularDistancia(punto4,punto10))
print(CalcularDistancia(punto5,punto6))
print(CalcularDistancia(punto5,punto7))
print(CalcularDistancia(punto5,punto8))
print(CalcularDistancia(punto5,punto9))
print(CalcularDistancia(punto5,punto10))
print(CalcularDistancia(punto6,punto7))
print(CalcularDistancia(punto6,punto8))
print(CalcularDistancia(punto6,punto9))
print(CalcularDistancia(punto6,punto10))
print(CalcularDistancia(punto7,punto8))
print(CalcularDistancia(punto7,punto9))
print(CalcularDistancia(punto7,punto10))
print(CalcularDistancia(punto8,punto9))
print(CalcularDistancia(punto8,punto10))
print(CalcularDistancia(punto9,punto10))

parCercano = "P4-P6"

#Ejercicio 2
lista1=[]
lista2=[]
lista3=[]

n=0
a=-1
while n<26:
  a=a*-1
  n=n+1
  lista1.append(a)
  
print(lista1)

n=101
while n>1:
    n=n-1 
    lista2.append(n)
    lista2.append(-1)

print(lista2)

n=1
while n<600:
  n=n+1
  num=[int(i) for i in str(n)]  
  # funcion que permite separar el numero en su digitos.
  x=num[len(num)-1]            
  # Len indica el ultimo numero.
  if x != 1 and x != 3 and x != 7 and x != 9: 
    lista3.append(n)

print(lista3)

listaDeListas = [lista1, lista2, lista3]

#Ejercicio 3
#cod      Nombre          Nota1   Nota2  Nota3  Nota4  Nota 5
#01    Miguel Pineda        1.0    1.1    2.3    1.1     ?
#02    Maria Gonzalez       3.1    3.1    1.2    3.0     ?
#03    Jose Nuñez           5.0    4.0    2.5    5.0     ?
#04    Angelica Lozano      3.1    1.0    2.6    1.0     ?
#05    Camilo Suarez        3.2    4.0    1.1    3.0     ?
#06    Mariana Rosero       5.0    5.0    5.0    3.9     ?
#07    Esteban Quesada      3.4    4.0    2.6    3.2     ?
#08    Julia Quintero       2.0    2.2    2.1    4.2     ?
#09    Mauricio Lizcano     3.7    4.1    4.7    4.0     ?
#10    Angie Gomez          4.1    4.7    4.4    5.0     ?
#11    Camilo Restrepo      5.0    5.0    1.0    3.2     ?
#12    Mauricio Velazquez   5.0    4.2    2.1    5.0     ?
#13    Esteban Rodriguez    3.2    4.1    2.2    3.3     ?

#Calculamos primero el prmedio de Las 4 notas con sus respectivos porcentajes.
import pandas as pd # Importamos las librerias necesarias.
import numpy as np

notasDatos = {'Miguel Pineda':[1.0*0.10,1.1*0.20,2.3*0.15,1.1*0.20],'Maria Gonzalez':[3.1*0.10,3.1*0.20,1.2*0.15,3.0*0.20],'Jose Nuñez':[5.0*0.10,4.0*0.20,2.5*0.15,5.0*0.20], \
              'Angelica Lozano':[3.1*0.10,1.0*0.20,2.6*0.15,1.0*0.20],'Camilo Suarez':[3.2*0.10,4.0*0.20,1.1*0.15,3.0*0.20],'Mariana Rosero':[5.0*0.10,5.0*0.20,5.0*0.15,3.9*0.20], \
              'Esteban Quesada':[3.4*0.10,4.0*0.20,2.6*0.15,3.2*0.20],'Julia Quintero':[2.0*0.10,2.2*0.20,2.1*0.15,4.2*0.20],'Mauricio Lizcano':[3.7*0.10,4.1*0.20,4.7*0.15, 4.0*0.20], \
              'Angie Gomez': [4.1*0.10,4.7*0.20,4.4*0.15,5.0*0.20],'Camilo Restrepo':[5.0*0.10,5.0*0.20,1.0*0.15,3.2*0.20],'Mauricio Velazquez':[5.0*0.10,4.2*0.20,2.1*0.15,5.0*0.20], \
              'Esteban Rodriguez':[3.2*0.10,4.1*0.20,2.2*0.15,3.3*0.20]} # Mediante una estructura de datos llamada diccionario, agrupamos la información de estudiantes y sus notas, con los porsentajes aplicados a cada una.

df = pd.DataFrame(data=notasDatos) #Dataframe a partir del diccionario, prodremos ver de manera ordenada los datos del mismo. 
df.round(2) # Mostramos el diccionario, redondeando los decimales a 2.

df.sum(axis=0) # Funcion que nos permite sumar todos los elementos de las columnas, para obtener un valor que será muy util más tarde. 
notaParcial = df.sum(axis=0) 
notaParcial # Con esta suma podemos notar que hay un par de estudiantes que ya han aprobado la materia.
# Pero es necesario hacer las comprobaciónes con el resto de estudiantes respecto a la nota 5 correspondiente al 35%.

df.sum(axis=0)
notaParcial = df.sum(axis=0) #Nota cinco se calcula a continuación mendiante la expreción [(3.0-notaParcial)/0.35]
nota5Pierde = (3 - notaParcial) / 0.35 
nota5Pierde = nota5Pierde[nota5Pierde > 5.0] #Averiguamos que estudiantes necesitan más de 5.0 para pasar la materia.
nota5Pierde

A = len(nota5Pierde) #Guardamos el número de estudiantes que pierden la materia en la variable A.
A

df.sum(axis=0)
notaParcial = df.sum(axis=0) 
nota5Apro = (3 - notaParcial) / 0.35 
nota5Apro = nota5Apro[nota5Apro <= 0.0] #Averiguamos que estudiantes tienen aprobada la materia ya que necesitan 0,0 o menos en la nota 5 para aprobar. 
nota5Apro

C = len(nota5Apro)
C

df.sum(axis=0)
notaParcial = df.sum(axis=0) 
nota5Posi = (3 - notaParcial) / 0.35 
nota5Posi = nota5Posi[nota5Posi <= 5.0] #Averiguamos que estudiantes tienen opción de pasar la materia. 
nota5Posi

B = len (nota5Posi) -2 # Guardamos el numero de estudiantes con posibilidad de aprobar en la variable B.
B

estudiantes = [A,C,B]
estudiantes

print (' La cantidad de estudiantes que pierden la materia es ',A ,'\n','La cantidad de estudiantes que ganan la materia es ' ,C, '\n','La cantidad de estudiantes que tiene posibilidad de aprobar la materia es ',B )

#Ejercicio4

lunes = [["si", "si"], ["si", "si"], ["si", "si"], ["si", "no"], ["si", "no"], ["si", "si"]]
martes = [["si", "si"], ["no", "no"], ["no", "no"], ["si", "no"], ["no", "no"], ["no", "no"]]
miercoles = [["si", "si"], ["si", "no"], ["si", "si"], ["si", "si"], ["no", "no"], ["si", "si"]]
jueves = [["si", "no"], ["no", "no"], ["si", "si"], ["no", "no"], ["si", "si"], ["no", "no"]]
viernes = [["no", "no"], ["si", "no"], ["no", "no"], ["no", "no"], ["si", "no"], ["no", "no"]]

total_juan = 0
total_camila = 0
total_jose = 0
total_maria = 0
total_esteban = 0
total_angie = 0

tarifa = 15000
tarifa_no_servicio = 10000
total_lunes_ida = 0
total_lunes_vuelta = 0
total_martes_ida = 0
total_martes_vuelta = 0
total_miercoles_ida = 0
total_miercoles_vuelta = 0
total_jueves_ida = 0
total_jueves_vuelta = 0
total_viernes_ida = 0
total_viernes_vuelta = 0

for x in range(6):
  if lunes[x][0] == "si":
    total_lunes_ida += 1

  if lunes[x][1] == "si":
    total_lunes_vuelta += 1

if total_lunes_ida == 0:
    total_juan += tarifa_no_servicio/6
    total_camila += tarifa_no_servicio/6
    total_jose += tarifa_no_servicio/6
    total_maria += tarifa_no_servicio/6
    total_esteban += tarifa_no_servicio/6
    total_angie += tarifa_no_servicio/6
if total_lunes_vuelta == 0:
    total_juan += tarifa_no_servicio/6
    total_camila += tarifa_no_servicio/6
    total_jose += tarifa_no_servicio/6
    total_maria += tarifa_no_servicio/6
    total_esteban += tarifa_no_servicio/6
    total_angie += tarifa_no_servicio/6

if lunes[0][0] == "si":
  total_juan += tarifa/total_lunes_ida
if lunes[1][0] == "si":
  total_camila += tarifa/total_lunes_ida
if lunes[2][0] == "si":
  total_jose += tarifa/total_lunes_ida
if lunes[3][0] == "si":
  total_maria += tarifa/total_lunes_ida
if lunes[4][0] == "si":
  total_esteban += tarifa/total_lunes_ida
if lunes[5][0] == "si":
  total_angie += tarifa/total_lunes_ida

if lunes[0][1] == "si":
  total_juan += tarifa/total_lunes_vuelta
if lunes[1][1] == "si":
  total_camila += tarifa/total_lunes_vuelta
if lunes[2][1] == "si":
  total_jose += tarifa/total_lunes_vuelta
if lunes[3][1] == "si":
  total_maria += tarifa/total_lunes_vuelta
if lunes[4][1] == "si":
  total_esteban += tarifa/total_lunes_vuelta
if lunes[5][1] == "si":
  total_angie += tarifa/total_lunes_vuelta

for x in range(6):
  if martes[x][0] == "si":
    total_martes_ida += 1

  if martes[x][1] == "si":
    total_martes_vuelta += 1

if total_martes_ida == 0:
    total_juan += tarifa_no_servicio/6
    total_camila += tarifa_no_servicio/6
    total_jose += tarifa_no_servicio/6
    total_maria += tarifa_no_servicio/6
    total_esteban += tarifa_no_servicio/6
    total_angie += tarifa_no_servicio/6
if total_martes_vuelta == 0:
    total_juan += tarifa_no_servicio/6
    total_camila += tarifa_no_servicio/6
    total_jose += tarifa_no_servicio/6
    total_maria += tarifa_no_servicio/6
    total_esteban += tarifa_no_servicio/6
    total_angie += tarifa_no_servicio/6

if martes[0][0] == "si":
  total_juan += tarifa/total_martes_ida
if martes[1][0] == "si":
  total_camila += tarifa/total_martes_ida
if martes[2][0] == "si":
  total_jose += tarifa/total_martes_ida
if martes[3][0] == "si":
  total_maria += tarifa/total_martes_ida
if martes[4][0] == "si":
  total_esteban += tarifa/total_martes_ida
if martes[5][0] == "si":
  total_angie += tarifa/total_martes_ida

if martes[0][1] == "si":
  total_juan += tarifa/total_martes_vuelta
if martes[1][1] == "si":
  total_camila += tarifa/total_martes_vuelta
if martes[2][1] == "si":
  total_jose += tarifa/total_martes_vuelta
if martes[3][1] == "si":
  total_maria += tarifa/total_martes_vuelta
if martes[4][1] == "si":
  total_esteban += tarifa/total_martes_vuelta
if martes[5][1] == "si":
  total_angie += tarifa/total_martes_vuelta

for x in range(6):
  if miercoles[x][0] == "si":
    total_miercoles_ida += 1

  if miercoles[x][1] == "si":
    total_miercoles_vuelta += 1

if total_miercoles_ida == 0:
    total_juan += tarifa_no_servicio/6
    total_camila += tarifa_no_servicio/6
    total_jose += tarifa_no_servicio/6
    total_maria += tarifa_no_servicio/6
    total_esteban += tarifa_no_servicio/6
    total_angie += tarifa_no_servicio/6
if total_miercoles_vuelta == 0:
    total_juan += tarifa_no_servicio/6
    total_camila += tarifa_no_servicio/6
    total_jose += tarifa_no_servicio/6
    total_maria += tarifa_no_servicio/6
    total_esteban += tarifa_no_servicio/6
    total_angie += tarifa_no_servicio/6

if miercoles[0][0] == "si":
  total_juan += tarifa/total_miercoles_ida
if miercoles[1][0] == "si":
  total_camila += tarifa/total_miercoles_ida
if miercoles[2][0] == "si":
  total_jose += tarifa/total_miercoles_ida
if miercoles[3][0] == "si":
  total_maria += tarifa/total_miercoles_ida
if miercoles[4][0] == "si":
  total_esteban += tarifa/total_miercoles_ida
if miercoles[5][0] == "si":
  total_angie += tarifa/total_miercoles_ida

if miercoles[0][1] == "si":
  total_juan += tarifa/total_miercoles_vuelta
if miercoles[1][1] == "si":
  total_camila += tarifa/total_miercoles_vuelta
if miercoles[2][1] == "si":
  total_jose += tarifa/total_miercoles_vuelta
if miercoles[3][1] == "si":
  total_maria += tarifa/total_miercoles_vuelta
if miercoles[4][1] == "si":
  total_esteban += tarifa/total_miercoles_vuelta
if miercoles[5][1] == "si":
  total_angie += tarifa/total_miercoles_vuelta

for x in range(6):
  if jueves[x][0] == "si":
    total_jueves_ida += 1

  if jueves[x][1] == "si":
    total_jueves_vuelta += 1

if total_jueves_ida == 0:
    total_juan += tarifa_no_servicio/6
    total_camila += tarifa_no_servicio/6
    total_jose += tarifa_no_servicio/6
    total_maria += tarifa_no_servicio/6
    total_esteban += tarifa_no_servicio/6
    total_angie += tarifa_no_servicio/6
if total_jueves_vuelta == 0:
    total_juan += tarifa_no_servicio/6
    total_camila += tarifa_no_servicio/6
    total_jose += tarifa_no_servicio/6
    total_maria += tarifa_no_servicio/6
    total_esteban += tarifa_no_servicio/6
    total_angie += tarifa_no_servicio/6

if jueves[0][0] == "si":
  total_juan += tarifa/total_jueves_ida
if jueves[1][0] == "si":
  total_camila += tarifa/total_jueves_ida
if jueves[2][0] == "si":
  total_jose += tarifa/total_jueves_ida
if jueves[3][0] == "si":
  total_maria += tarifa/total_jueves_ida
if jueves[4][0] == "si":
  total_esteban += tarifa/total_jueves_ida
if jueves[5][0] == "si":
  total_angie += tarifa/total_jueves_ida

if jueves[0][1] == "si":
  total_juan += tarifa/total_jueves_vuelta
if jueves[1][1] == "si":
  total_camila += tarifa/total_jueves_vuelta
if jueves[2][1] == "si":
  total_jose += tarifa/total_jueves_vuelta
if jueves[3][1] == "si":
  total_maria += tarifa/total_jueves_vuelta
if jueves[4][1] == "si":
  total_esteban += tarifa/total_jueves_vuelta
if jueves[5][1] == "si":
  total_angie += tarifa/total_jueves_vuelta

for x in range(6):
  if viernes[x][0] == "si":
    total_viernes_ida += 1

  if viernes[x][1] == "si":
    total_viernes_vuelta += 1

if total_viernes_ida == 0:
    total_juan += tarifa_no_servicio/6
    total_camila += tarifa_no_servicio/6
    total_jose += tarifa_no_servicio/6
    total_maria += tarifa_no_servicio/6
    total_esteban += tarifa_no_servicio/6
    total_angie += tarifa_no_servicio/6
if total_viernes_vuelta == 0:
    total_juan += tarifa_no_servicio/6
    total_camila += tarifa_no_servicio/6
    total_jose += tarifa_no_servicio/6
    total_maria += tarifa_no_servicio/6
    total_esteban += tarifa_no_servicio/6
    total_angie += tarifa_no_servicio/6

if viernes[0][0] == "si":
  total_juan += tarifa/total_viernes_ida
if viernes[1][0] == "si":
  total_camila += tarifa/total_viernes_ida
if viernes[2][0] == "si":
  total_jose += tarifa/total_viernes_ida
if viernes[3][0] == "si":
  total_maria += tarifa/total_viernes_ida
if viernes[4][0] == "si":
  total_esteban += tarifa/total_viernes_ida
if viernes[5][0] == "si":
  total_angie += tarifa/total_viernes_ida

if viernes[0][1] == "si":
  total_juan += tarifa/total_viernes_vuelta
if viernes[1][1] == "si":
  total_camila += tarifa/total_viernes_vuelta
if viernes[2][1] == "si":
  total_jose += tarifa/total_viernes_vuelta
if viernes[3][1] == "si":
  total_maria += tarifa/total_viernes_vuelta
if viernes[4][1] == "si":
  total_esteban += tarifa/total_viernes_vuelta
if viernes[5][1] == "si":
  total_angie += tarifa/total_viernes_vuelta

diccionarioPagos = {'JUAN': total_juan,
                    'CAMILA': total_camila,
                    'JOSE': total_jose,
                    'MARIA': total_maria,
                    'ESTEBAN': total_esteban,
                    'ANGIE': total_angie}

print(diccionarioPagos)