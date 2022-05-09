
import pandas as pd
import statistics as st
import matplotlib.pyplot as plt

# Comenzamos leyendo el archivo

try:
    datos = pd.read_csv( "C:/Users/Jorge/Desktop/Ejercicio_1_Jorge_Marmol/finanzas2020.csv", delimiter=";")
except Exception as e:
    print("Error al leer el archivo: ", e)
else:
    print("Se leyó el archivo, se muestra a continuación parte del mismo")
    datos.head()

nombres_columnas = datos.columns.values

#print("La función column ",datos.columns)

#print("La función Value ", datos.columns.values)

#Comprobamos que  haya 12 meses

if len(nombres_columnas==12):
 print("Existen 12 columnas en el dataset, que son", nombres_columnas)
else:
 print("No existen 12 columnas en el dataset")

#Comprobamos que todos los meses tengan datos

for values in nombres_columnas:
     if len(datos.values)==0:
         print("La columna", values, "no presenta valores")
     else:
         print("La columna", values, "presenta valores")

# Devuelve array de un array que sea menores que 0

def soloGastos(array):
    resultado = array[array <= 0]
    return resultado

# Devuelve array de un array que sea mayores que 0
def soloIngresos(array):
    resultado = array[array > 0]
    return resultado

# Definimos una función que tenga de entrada un array (mes) y devuelva un array con los escalares que necesitamos
def esdisticas(mes):
    try:
        st.mean(mes)
    except Exception as e:
        print(f"Se ha producido un error: {e}. Hay entradas no numéricas por lo que se van a convertir y eliminar")
    try:
        mes_numerico = pd.to_numeric(mes, errors='coerce').dropna()
        print("Se eliminaron las entradas no numéricas")
    except Exception as e:
        print(f"Ha ocurrido un error {e}")

    mes_ingresos = soloIngresos(mes_numerico)
    mes_gastos = soloGastos(mes_numerico)

    return [[sum(mes_ingresos), sum(mes_gastos), st.mean(mes_gastos)]]

# Llamamos a un DataFrame vacío que rellenaremos con los datos
datos_finales = pd.DataFrame()

# Vamos añadiendo por fila el array

for value in nombres_columnas:
     lista_mes = esdisticas(datos[value])
     datos_finales = datos_finales.append(lista_mes, ignore_index=True)

#Establecemos el nombre de las columnas e indexamos por meses

datos_finales.columns = ["Ingresos", "Gastos", "Media de gastos"]
datos_finales.index = nombres_columnas





#Preguntas numero 1

print(f"El mes en el que más se ha gastado es {nombres_columnas[(list(datos_finales.Gastos)).index(min(datos_finales.Gastos))]}")


#Preguntas numero 2

print(f"El mes en el que más he ahorrado es {nombres_columnas[(list(datos_finales.Ingresos + datos_finales.Gastos)).index(max(datos_finales.Ingresos + datos_finales.Gastos))]}")


# Preguntas numero 3

print(f"La media de gastos es {st.mean(datos_finales.Gastos)}")

# Pregunta numero 4

print(f"El gasto total ha sido {sum(datos_finales.Gastos)}")


# Pregunta numero 5


print(f"Los ingresos totales han sido {sum(datos_finales.Ingresos)}")


# Pregunta numero 6


plt.figure(figsize=(20,25))
plt.plot(datos_finales.Ingresos)
plt.show
