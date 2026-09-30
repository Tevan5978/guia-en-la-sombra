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

if __name__ == "__main__":

    h = HistorialMovimientos()

    h.agregar_al_final((1, 1))
    h.agregar_al_final((1, 2))
    h.agregar_al_final((1, 3))

    print("Adelante:", h.recorrer_adelante())
    print("Atrás:", h.recorrer_atras())

    h.agregar_al_inicio((1, 0))
    print("Con inicio agregado:", h.recorrer_adelante())

    h.eliminar((1, 2))
    print("Después de eliminar (1,2):", h.recorrer_adelante())

    print("Tamaño final:", h.tamano)