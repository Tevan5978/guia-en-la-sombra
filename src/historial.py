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


    def __init__(self) -> None:
        self.cabeza: Optional[Nodo[T]] = None
        self.cola: Optional[Nodo[T]] = None
        self.tamano: int = 0

    def agregar_al_final(self, valor: T) -> None:
        """Agrega un nuevo movimiento al final del historial."""

        nuevo_nodo = Nodo(valor)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

        self.tamano += 1

    def agregar_al_inicio(self, valor: T) -> None:
        """Agrega un nuevo movimiento al inicio del historial."""

        nuevo_nodo = Nodo(valor)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

        self.tamano += 1

    def eliminar(self, valor: T) -> bool:
        """Elimina la primera aparición de un valor en el historial.

        Regresa True si se eliminó algo, False si no se encontró el valor.
        """

        nodo_actual = self.cabeza

        while nodo_actual is not None:

            if nodo_actual.valor == valor:

                if nodo_actual.anterior is not None:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                else:
                    self.cabeza = nodo_actual.siguiente

                if nodo_actual.siguiente is not None:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                else:
                    self.cola = nodo_actual.anterior

                self.tamano -= 1
                return True

            nodo_actual = nodo_actual.siguiente

        return False

    def recorrer_adelante(self) -> list[T]:
        """Regresa los valores del historial, de la cabeza a la cola."""

        valores = []
        nodo_actual = self.cabeza

        while nodo_actual is not None:
            valores.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

        return valores

    def recorrer_atras(self) -> list[T]:
        """Regresa los valores del historial, de la cola a la cabeza."""

        valores = []
        nodo_actual = self.cola

        while nodo_actual is not None:
            valores.append(nodo_actual.valor)
            nodo_actual = nodo_actual.anterior

        return valores

    def esta_vacia(self) -> bool:
        """Indica si el historial no tiene movimientos."""

        return self.cabeza is None

