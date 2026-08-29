"""
operaciones.py

Operaciones sobre vectores/matrices para el proyecto Guía en las Sombras.
Responsabilidad: Integrante 3.

Trabaja sobre la clase Laberinto (src/laberinto.py) o directamente sobre
una matriz representada como lista de listas de enteros.

Convenciones de la matriz (ver docs/estructura-laberinto.md y Laberinto):
    0 -> Camino
    1 -> Pared
    2 -> Entrada
    3 -> Salida
"""

from typing import List, Tuple, Optional, Iterator, Union

from laberinto import Laberinto

Matriz = List[List[int]]

CAMINO = Laberinto.CAMINO
PARED = Laberinto.PARED
ENTRADA = Laberinto.ENTRADA
SALIDA = Laberinto.SALIDA

SIMBOLOS = {
    CAMINO: ".",
    PARED: "█",
    ENTRADA: "E",
    SALIDA: "S",
}


def _obtener_matriz(objeto: Union[Laberinto, Matriz]) -> Matriz:
    """
    Permite que todas las funciones acepten tanto un objeto Laberinto
    como una matriz "cruda" (lista de listas), sin duplicar código.
    """
    if isinstance(objeto, Laberinto):
        return objeto.matriz
    return objeto


# ------------------------------
# Validación de límites
# ------------------------------

def esta_dentro_de_limites(objeto: Union[Laberinto, Matriz], fila: int, columna: int) -> bool:
    """
    Indica si la posición (fila, columna) existe dentro de la matriz.
    """
    matriz = _obtener_matriz(objeto)
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    return 0 <= fila < filas and 0 <= columna < columnas


# ------------------------------
# Acceso a elementos
# ------------------------------

def obtener_celda(objeto: Union[Laberinto, Matriz], fila: int, columna: int) -> int:
    """
    Devuelve el valor de la celda (fila, columna).

    Raises:
        IndexError: si la posición está fuera de los límites de la matriz.
    """
    matriz = _obtener_matriz(objeto)
    if not esta_dentro_de_limites(matriz, fila, columna):
        filas = len(matriz)
        columnas = len(matriz[0]) if filas > 0 else 0
        raise IndexError(
            f"Posición ({fila}, {columna}) fuera de los límites de la matriz "
            f"({filas}x{columnas})."
        )
    return matriz[fila][columna]


# ------------------------------
# Recorridos
# ------------------------------

def recorrer_por_filas(objeto: Union[Laberinto, Matriz]) -> Iterator[Tuple[int, int, int]]:
    """
    Recorre la matriz fila por fila, de izquierda a derecha.

    Yields:
        Tuplas (fila, columna, valor) en orden de recorrido.
    """
    matriz = _obtener_matriz(objeto)
    for f, fila in enumerate(matriz):
        for c, valor in enumerate(fila):
            yield f, c, valor


def recorrer_por_columnas(objeto: Union[Laberinto, Matriz]) -> Iterator[Tuple[int, int, int]]:
    """
    Recorre la matriz columna por columna, de arriba a abajo.

    Yields:
        Tuplas (fila, columna, valor) en orden de recorrido.
    """
    matriz = _obtener_matriz(objeto)
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    for c in range(columnas):
        for f in range(filas):
            yield f, c, matriz[f][c]


# ------------------------------
# Búsqueda de celdas
# ------------------------------

def buscar_valor(objeto: Union[Laberinto, Matriz], valor: int) -> Optional[Tuple[int, int]]:
    """
    Busca la primera celda que contenga el valor indicado (recorrido por filas).

    Returns:
        Tupla (fila, columna) de la primera coincidencia, o None si no existe.
    """
    matriz = _obtener_matriz(objeto)
    for f, fila in enumerate(matriz):
        for c, val in enumerate(fila):
            if val == valor:
                return f, c
    return None


def buscar_entrada(objeto: Union[Laberinto, Matriz]) -> Optional[Tuple[int, int]]:
    """Atajo para buscar la celda de entrada (valor 2)."""
    return buscar_valor(objeto, ENTRADA)


def buscar_salida(objeto: Union[Laberinto, Matriz]) -> Optional[Tuple[int, int]]:
    """Atajo para buscar la celda de salida (valor 3)."""
    return buscar_valor(objeto, SALIDA)


def buscar_todas_las_coincidencias(objeto: Union[Laberinto, Matriz], valor: int) -> List[Tuple[int, int]]:
    """
    Busca todas las celdas que contengan el valor indicado.

    Útil, junto con Laberinto.validar(), para verificar que solo exista
    una entrada y una salida.
    """
    matriz = _obtener_matriz(objeto)
    return [
        (f, c)
        for f, fila in enumerate(matriz)
        for c, val in enumerate(fila)
        if val == valor
    ]


# -----------------------------------------------
# Impresión / visualización básica en consola
# -----------------------------------------------

def imprimir_laberinto(objeto: Union[Laberinto, Matriz], usar_simbolos: bool = True) -> None:
    """
    Imprime el laberinto en consola.

    Args:
        usar_simbolos: si es True, imprime símbolos legibles (█, ., E, S).
            Si es False, imprime los valores numéricos crudos (como Laberinto.mostrar()).
    """
    matriz = _obtener_matriz(objeto)
    for fila in matriz:
        if usar_simbolos:
            linea = "".join(SIMBOLOS.get(valor, "?") for valor in fila)
        else:
            linea = "".join(str(valor) for valor in fila)
        print(linea)


if __name__ == "__main__":
    # Prueba manual rápida cargando un laberinto real del proyecto
    laberinto = Laberinto.desde_archivo("laberintos/nivel3.txt")

    print("Laberinto (símbolos):")
    imprimir_laberinto(laberinto)

    print("\nEntrada:", buscar_entrada(laberinto))
    print("Salida:", buscar_salida(laberinto))
    print("Celda (1,1):", obtener_celda(laberinto, 1, 1))
    print("¿(10,10) dentro de límites?:", esta_dentro_de_limites(laberinto, 10, 10))