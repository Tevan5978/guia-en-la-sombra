"""Estructura base para almacenar un historial de movimientos."""  # Documenta la finalidad general de esta estructura.

# La lista es doblemente enlazada: cada nodo conoce al nodo siguiente y al
# anterior. Las operaciones y validaciones se pueden incorporar en esta base.

from __future__ import annotations  # Permite usar tipos de forma más flexible en annotations futuras.

from typing import Generic, Optional, TypeVar  # Importa utilidades de tipado y genéricos.


T = TypeVar("T")  # Define un tipo genérico que usará la lista enlazada.


class Nodo(Generic[T]):  # Crea una estructura de nodo genérico para la lista doblemente enlazada.
    """Nodo de la lista que almacena un valor y sus enlaces vecinos."""  # Explica el propósito del nodo.

    # Attributos:
    #     valor: Dato almacenado, por ejemplo una posición del jugador.
    #     siguiente: Nodo que viene después, o ``None`` si es el último.
    #     anterior: Nodo que viene antes, o ``None`` si es el primero.

    def __init__(self, valor: T) -> None:  # Inicializa cada nodo con el valor recibido y enlaces vacíos.
        self.valor: T = valor  # Guarda el dato contenido en el nodo.
        self.siguiente: Optional[Nodo[T]] = None  # Apunta al siguiente nodo o None si no existe.
        self.anterior: Optional[Nodo[T]] = None  # Apunta al nodo anterior o None si no existe.


class HistorialMovimientos(Generic[T]):  # Define la estructura principal para guardar movimientos.
    """Estructura doblemente enlazada para un historial de movimientos."""  # Describe la intención de la clase.

    # La lista comienza vacía. Las operaciones de inserción, eliminación y
    # recorrido, así como las validaciones, pueden añadirse posteriormente.

    # Attributos:
    #     cabeza: Primer nodo del historial, o ``None`` si está vacío.
    #     cola: Último nodo del historial, o ``None`` si está vacío.
    #     tamano: Cantidad de nodos almacenados.

    def __init__(self) -> None:  # Inicializa el historial vacío.
        self.cabeza: Optional[Nodo[T]] = None  # Guarda el primer nodo del historial.
        self.cola: Optional[Nodo[T]] = None  # Guarda el último nodo del historial.
        self.tamano: int = 0  # Cuenta cuántos elementos hay en el historial.