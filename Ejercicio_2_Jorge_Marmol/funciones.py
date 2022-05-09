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
