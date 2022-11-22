# -*- coding: utf-8 -*-
"""ejercicios3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gTqo5FLd4JbccJEbCFaXsKtFU0Xiumrb
"""

nombre_completo = "Camila Duran Salazar"

"""Ejercicio 1"""

import conversiones
import conversor
import unittest


class TestConversiones(unittest.TestCase):
    def test_binario_decimal(self):
        esperado = 7
        actual = conversiones.binario_a_decimal("111")
        self.assertEqual(actual, esperado)

    def test_decimal_binario(self):
        esperado = "111"
        actual = conversiones.decimal_a_binario(7)
        self.assertEqual(actual, esperado)

    def test_octal_decimal(self):
        esperado = 123
        actual = conversiones.octal_a_decimal("173")
        self.assertEqual(actual, esperado)

    def test_decimal_octal(self):
        esperado = "173"
        actual = conversiones.decimal_a_octal(123)
        self.assertEqual(actual, esperado)

    def test_hexadecimal_decimal(self):
        esperado = 255
        actual = conversiones.hexadecimal_a_decimal("ff")
        self.assertEqual(actual, esperado)

    def test_decimal_hexadecimal(self):
        esperado = "ff"
        actual = conversiones.decimal_a_hexadecimal(255)
        self.assertEqual(actual, esperado)

    def test_obtener_numero_decimal(self):
        valores = [
            {
                "base": "2",
                "numero": "111",
                "esperado": 7,
            },
            {
                "base": "8",
                "numero": "173",
                "esperado": 123,
            },
            {
                "base": "16",
                "numero": "f",
                "esperado": 15,
            },
        ]
        for valor in valores:
            esperado = valor["esperado"]
            actual = conversor.obtener_numero_decimal(
                valor["base"], valor["numero"])
            self.assertEqual(actual, esperado)


if __name__ == "__main__":
    unittest.main()

# regresa una tupla con la base de origen, el número a convertir y la base de destino
def solicitar_datos_a_usuario():
    bases_soportadas = ["2", "8", "10", "16", ]
    base_origen = input("""
2 - Binario
8 - Octal
10 - Decimal
16 - Hexadecimal
Elige la base desde donde conviertes: [2, 8, 10, 16]: """)
    if base_origen not in bases_soportadas:
        print("La base que ingresaste no está soportada")
        return
    numero = input(
        f"Ok, vas a convertir desde la base {base_origen}. Ingresa el número a convertir: ")
    base_destino = input("""
2 - Binario
8 - Octal
10 - Decimal
16 - Hexadecimal
Elige la base a la que conviertes: [2, 8, 10, 16]: """)
    if base_destino not in bases_soportadas:
        print("La base de destino no está soportada")
        return
    return (base_origen, numero, base_destino)


def obtener_numero_decimal(base_origen, numero):
    if base_origen == "2":
        return conversiones.binario_a_decimal(numero)
    elif base_origen == "8":
        return conversiones.octal_a_decimal(numero)
    elif base_origen == "10":
        return int(numero)
    elif base_origen == "16":
        return conversiones.hexadecimal_a_decimal(numero)


def convertir(numero, base_destino):
    if base_destino == "2":
        return conversiones.decimal_a_binario(numero)
    elif base_destino == "8":
        return conversiones.decimal_a_octal(numero)
    elif base_destino == "10":
        return int(numero)
    elif base_destino == "16":
        return conversiones.decimal_a_hexadecimal(numero)


if __name__ == '__main__':
    datos = solicitar_datos_a_usuario()
    # Comprobamos si los datos son correctos
    if datos:
        base_origen, numero, base_destino = datos
        # Para ahorrarnos código, vamos a convertir el número a decimal (sin importar la base de origen) y luego ese número
        # lo convertimos a la base de destino
        numero_decimal = obtener_numero_decimal(base_origen, numero)
        # Y a ese decimal lo convertimos a la base deseada
        resultado = convertir(numero_decimal, base_destino)
        print(resultado)

"""Ejercicio 2"""

import pandas as pd
archivo = "estudiantes.csv"
ruta = "INFORME3/" + archivo
hojaEstudiantes = pd.read_csv(ruta, index_col="codigo", dtype={"codigo":str})

## Promedios de los estudiantes

listaPromEstu = [hojaEstudiantes.iloc[i,:].mean() for i in range(0,500)]
promediosEstudiantes = pd.Series(listaPromEstu, index = [hojaEstudiantes.index.get_level_values("codigo")[i] for i in range(0,500)])

## Promedios de los exámenes

listaExam = ["examen"+str(i) for i in range(1,11)]
listaPromExam = [hojaEstudiantes["examen"+str(i)].mean() for i in range(1,11)]
promediosExamenes = pd.Series(listaPromExam, index = listaExam)

## Identificamos quién es el mejor y peor estudiante

mejorEstudiante = promediosEstudiantes.idxmax()
peorEstudiante = promediosEstudiantes.idxmin()

## Resultado final

reporteEstudiantes = [promediosEstudiantes, promediosExamenes, mejorEstudiante, peorEstudiante]

"""Ejercicio 3"""

import pandas as pd

info = ["B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-12Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","A032-52Unidades","B001-29Unidades","A125-15Unidades","A032-22Unidades","P009-25Unidades","B005-20Unidades","B001-19Unidades","P009-31Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-52Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-21Unidades","A001-31unidades","A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades","P009-19Unidades","B005-11Unidades","B001-19Unidades","B005-20Unidades","B001-19Unidades","P009-31Unidades","B005-22Unidades","W307-15Unidades","Z278-30Unidades","Z025-24Unidades","P009-21Unidades","Z278-30Unidades","Z025-24Unidades","Z278-11Unidades","A001-91unidades","A032-52Unidades","B001-29Unidades","A125-15Unidades","A032-22Unidades","P009-25Unidades","B005-20Unidades","B001-19Unidades","P009-31Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-52Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-21Unidades","A001-31unidades","A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades","P009-19Unidades","B005-11Unidades","B001-19Unidades","P009-21Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-12Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-11Unidades","A001-91unidades","A032-52Unidades","B001-29Unidades","A125-10Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-52Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-21Unidades","A001-31unidades","A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades","P009-19Unidades","B005-11Unidades","B001-19Unidades","P009-21Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-21Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-15Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","A032-22Unidades","P009-25Unidades","Z278-11Unidades","A001-91unidades"]

codigos = []
unidades = []

for item in info:
    if item[0:4] in set(codigos):                    # El código son los primeros 4 dígitos del string, se verifica si el producto ya existe
        i = codigos.index(item[0:4])
        unidades[i] = unidades[i] + int(item[5:7])
    else:
        codigos.append(item[0:4]) 
        unidades.append(int(item[5:7]))


## Creamos la serie

ventasPorProducto = pd.Series(unidades, index = codigos)

## utilizamos los comandos de pandas para los datos de las estadísticas

media = int(ventasPorProducto.mean())
mediana = int(ventasPorProducto.median())
desviacion = int(ventasPorProducto.std())
maximo = int(ventasPorProducto.max())
minimo = int(ventasPorProducto.min())
estadisticas = [media, mediana,desviacion, maximo, minimo]

masVendido = ventasPorProducto.idxmax()
menosVendido = ventasPorProducto.idxmin()
extremos = [masVendido, menosVendido]

reporteVentas = [ventasPorProducto, estadisticas, extremos]

print(reporteVentas)

"""Ejercicio 4"""

import numpy as np

def graficaGenerica(x, y):

    # Valores numericos   

    y_derivadaOrden1 = np.diff(y)/np.diff(x)
    y_derivadaOrden2 = np.diff(y_derivadaOrden1)/np.diff(x[:-1])

    # Grafica

    import matplotlib.pyplot as plt
    plt.figure()
    plt.subplot(1,3,1)
    plt.plot(x,y)      # y vs x
    plt.title("función")
    plt.subplot(1,3,2)
    plt.plot(x[:-1], y_derivadaOrden1)      # y' vs x
    plt.title("derivada de orden 1")
    plt.subplot(1,3,3)
    plt.plot(x[:-2], y_derivadaOrden2)      # y'' vs x
    plt.title("derivada de orden 2")
    plt.suptitle("Gráficas del punto 4.")
    plt.show()