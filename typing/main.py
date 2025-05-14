def procesar_datos(datos):
    resultado = datos.filtrar().calcular_total()
    return resultado


# Python 3.5+
def procesar_datos(datos: DatosCliente) -> ResultadoProcesado:
    resultado = datos.filtrar().calcular_total()
    return resultado


nombre: str = "Ana"
edad: int = 30
activo: bool = True

from typing import List, Dict, Tuple, Optional

# Lista de enteros
numeros: List[int] = [1, 2, 3]
# Diccionario de string a float
precios: Dict[str, float] = {"manzana": 1.5, "naranja": 2.0}
# Tupla con tipos específicos
coordenada: Tuple[float, float] = (10.5, -20.3)
# Valor que podría ser None
usuario: Optional[str] = None


class DatosCliente:
    def filtrar(self) -> 'DatosFiltrados':
        pass


class DatosFiltrados:
    def calcular_total(self) -> float:
        pass


class ResultadoProcesado:
    total: float
    timestamp: str


from datetime import datetime


def obtener_timestamp() -> str:
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def procesar_datos(datos: DatosCliente) -> ResultadoProcesado:
    filtrado = datos.filtrar()
    total = filtrado.calcular_total()
    resultado = ResultadoProcesado()
    resultado.total = total
    resultado.timestamp = obtener_timestamp()
    return resultado











