"""
validaciones.py

Validación de entradas para el historial de movimientos (lista doblemente
enlazada).

Este módulo no reemplaza las operaciones de HistorialMovimientos
(agregar_al_final, agregar_al_inicio, eliminar, recorrer_adelante,
recorrer_atras, esta_vacia) — las envuelve, verificando primero que los
datos de entrada sean válidos antes de dejar que la operación ocurra.

Objetivo del proyecto: cada movimiento es una posición del laberinto,
representada como una tupla (fila, columna) de dos enteros no negativos.
"""

from typing import Any, Tuple

from historial import HistorialMovimientos


Posicion = Tuple[int, int]


# -----------------------------------------
# Validación de tipo del valor a insertar
# -----------------------------------------

def validar_posicion(valor: Any) -> None:
    """
    Valida que un valor sea una posición válida: una tupla (fila, columna)
    de dos enteros no negativos.

    Args:
        valor: dato a validar.

    Raises:
        TypeError: si valor no es una tupla de dos enteros.
        ValueError: si fila o columna son negativos.
    """
    if not isinstance(valor, tuple):
        raise TypeError(
            f"El movimiento debe ser una tupla (fila, columna), "
            f"se recibió {type(valor).__name__}."
        )

    if len(valor) != 2:
        raise TypeError(
            f"El movimiento debe tener exactamente 2 elementos (fila, columna), "
            f"se recibieron {len(valor)}."
        )

    fila, columna = valor

    if not isinstance(fila, int) or isinstance(fila, bool):
        raise TypeError(f"La fila debe ser un entero, se recibió {type(fila).__name__}.")

    if not isinstance(columna, int) or isinstance(columna, bool):
        raise TypeError(f"La columna debe ser un entero, se recibió {type(columna).__name__}.")

    if fila < 0 or columna < 0:
        raise ValueError(
            f"La posición ({fila}, {columna}) no es válida: "
            f"fila y columna deben ser mayores o iguales a 0."
        )


# ------------------------------------
# Validación de estado (lista vacía)
# ------------------------------------

def validar_no_vacio(historial: HistorialMovimientos) -> None:
    """
    Valida que el historial tenga al menos un movimiento.

    Args:
        historial: instancia de HistorialMovimientos.

    Raises:
        ValueError: si el historial está vacío.
    """
    if historial.esta_vacia():
        raise ValueError("No se puede operar sobre un historial vacío.")


# -----------------------
# Validación de índices
# -----------------------

def validar_indice(historial: HistorialMovimientos, indice: int) -> None:
    """
    Valida que un índice esté dentro del rango del historial.

    Args:
        historial: instancia de HistorialMovimientos.
        indice: posición a validar (0 = cabeza, tamano-1 = cola).

    Raises:
        TypeError: si el índice no es un entero.
        IndexError: si el índice está fuera de rango.
    """
    if not isinstance(indice, int) or isinstance(indice, bool):
        raise TypeError(f"El índice debe ser un entero, se recibió {type(indice).__name__}.")

    if indice < 0 or indice >= historial.tamano:
        raise IndexError(
            f"Índice {indice} fuera de rango. "
            f"El historial tiene {historial.tamano} movimiento(s) "
            f"(índices válidos: 0 a {historial.tamano - 1})."
        )


# ------------------------------------------------------------------------
# Operaciones seguras: validan antes de delegar en HistorialMovimientos
# ------------------------------------------------------------------------

def agregar_al_final_seguro(historial: HistorialMovimientos, valor: Any) -> None:
    """Valida el tipo del valor y lo agrega al final del historial."""
    validar_posicion(valor)
    historial.agregar_al_final(valor)


def agregar_al_inicio_seguro(historial: HistorialMovimientos, valor: Any) -> None:
    """Valida el tipo del valor y lo agrega al inicio del historial."""
    validar_posicion(valor)
    historial.agregar_al_inicio(valor)


def eliminar_seguro(historial: HistorialMovimientos, valor: Any) -> bool:
    """
    Valida que el historial no esté vacío y que el valor sea una posición
    válida, y luego intenta eliminarlo.

    Returns:
        True si se eliminó, False si el valor no estaba en el historial.

    Raises:
        ValueError: si el historial está vacío.
        TypeError: si valor no es una posición válida.
    """
    validar_no_vacio(historial)
    validar_posicion(valor)
    return historial.eliminar(valor)


def obtener_por_indice(historial: HistorialMovimientos, indice: int) -> Posicion:
    """
    Devuelve el valor almacenado en la posición indice del historial
    (0 = cabeza, tamano-1 = cola), recorriendo desde la cabeza.

    Args:
        historial: instancia de HistorialMovimientos.
        indice: posición a consultar.

    Raises:
        ValueError: si el historial está vacío.
        IndexError: si el índice está fuera de rango.

    Returns:
        La posición (fila, columna) almacenada en ese índice.
    """
    validar_no_vacio(historial)
    validar_indice(historial, indice)

    nodo_actual = historial.cabeza
    for _ in range(indice):
        nodo_actual = nodo_actual.siguiente

    return nodo_actual.valor