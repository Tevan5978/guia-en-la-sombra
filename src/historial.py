"""Estructura base para almacenar un historial de movimientos.

La lista es doblemente enlazada: cada nodo conoce al nodo siguiente y al
anterior. Las operaciones y validaciones se pueden incorporar en esta base.
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar


T = TypeVar("T")


class Nodo(Generic[T]):
    """Nodo de la lista que almacena un valor y sus enlaces vecinos.

    Attributos:
        valor: Dato almacenado, por ejemplo una posición del jugador.
        siguiente: Nodo que viene después, o ``None`` si es el último.
        anterior: Nodo que viene antes, o ``None`` si es el primero.
    """

    def __init__(self, valor: T) -> None:
        self.valor: T = valor
        self.siguiente: Optional[Nodo[T]] = None
        self.anterior: Optional[Nodo[T]] = None


class HistorialMovimientos(Generic[T]):
    """Estructura doblemente enlazada para un historial de movimientos.

    La lista comienza vacía. Las operaciones de inserción, eliminación y
    recorrido, así como las validaciones, pueden añadirse posteriormente.

    Attributos:
        cabeza: Primer nodo del historial, o ``None`` si está vacío.
        cola: Último nodo del historial, o ``None`` si está vacío.
        tamano: Cantidad de nodos almacenados.
    """

    def __init__(self) -> None:
        self.cabeza: Optional[Nodo[T]] = None
        self.cola: Optional[Nodo[T]] = None
        self.tamano: int = 0