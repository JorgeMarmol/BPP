import funciones as fun
import pandas as pd
import pytest


datos = pd.read_csv("C:/Users/Jorge/Desktop/MasterPython/BuenasPracticas/Ejercicio_2_Jorge_Marmol/finanzas2020.csv", delimiter=";")



def test_soloIngresos():
    x = list(fun.soloIngresos(pd.Series([1, 2, 3, -4, 5, 6, -7])))
    resultado = list(pd.Series([1, 2, 3, 5, 6]))
    assert x == resultado


def test_soloIngresos2():
    x = list(fun.soloGastos(pd.Series([3, -5, 1, 4, -3, -9])))
    resultado = list(pd.Series([3, 1, 4]))
    assert x == resultado



def test_soloIngresos_error():
    x = list(fun.soloIngresos(pd.Series([0, 2, 3, -5, 7])))
    resultado = list(pd.Series([0, 2, 3, 7]))
    assert x == resultado


def test_soloGastos():
    x = list(fun.soloGastos(pd.Series([1, 2, 3, -4, 5,6, 7])))
    resultado = list(pd.Series([-4]))
    assert x == resultado


def test_soloGastos2():
    x = list(fun.soloGastos(pd.Series([3, -4, 0, 7, -2, -9])))
    resultado = list(pd.Series([-4, 0, -2, -9]))
    assert x == resultado


def test_soloGastos3():
    x = list(fun.soloGastos(pd.Series([1, -1, 2, 3, -2, -3])))
    resultado = list(pd.Series([1, 2, 3]))
    assert x == resultado


#Recordamos que en la funcion estadistica la salida es un array que la primera componente
#corresponde a la suma de ingresos, la segunda a la suma de gastos y la tercera media de Gastos


def test_SumaIngresos():
    x = fun.estadisticas(pd.Series([3, -4, 0, 7, -2, -9]))[0]
    assert x[0] == 10


def test_SumaIngresos():
    x = fun.estadisticas(pd.Series([3, -4, 0, 7, -2, -9]))[0]
    assert x[0] == 1


def test_SumaGastos():
    x = fun.estadisticas(pd.Series([3, -4, 0, 7, -2, -9]))[0]
    assert x[1] == -15


def test_SumaGastos2():
    x = fun.estadisticas(pd.Series([3, -3, 0, 7, -2, -9]))[0]
    assert x[1] == -16


def test_MediaGastos():
    x = funcionesA1.estadisticas(pd.Series([3, -4, 0, 7, -2, -9]))[0]
    assert x[2] == -5


def test_MediaGastoss2():
    x = fun.estadisticas(pd.Series([3, -4, 0, 7, -2, -9]))[0]
    assert x[2] == -3.75
