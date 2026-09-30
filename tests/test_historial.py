"""
test_historial.py

Pruebas unitarias para src/validaciones.py sobre el historial de
movimientos (lista doblemente enlazada).

Cada bloque de pruebas corresponde a una de las funciones de validación,
y dentro de cada uno se cubren: el caso correcto (no debe lanzar error)
y los casos incorrectos (debe lanzar el error esperado).

Ejecutar::
    python -m pytest tests/test_historial.py -v
"""

import pytest  # Framework de pruebas: permite escribir funciones test_* y usar fixtures.

from historial import HistorialMovimientos  # Clase sobre la que se valida.
from validaciones import (  # Funciones de validación e inserción/eliminación.
    validar_posicion,
    validar_no_vacio,
    validar_indice,
    agregar_al_final_seguro,
    agregar_al_inicio_seguro,
    eliminar_seguro,
    obtener_por_indice,
)


# -----------
# Fixtures
# -----------
# Un "fixture" es una función que prepara datos de prueba reutilizables.
# Pytest la ejecuta automáticamente cada vez que un test la pide como
# parámetro, entregando una copia nueva y limpia en cada prueba.

@pytest.fixture
def historial_vacio():
    """Historial recién creado, sin movimientos. Para probar los
    casos de error relacionados con listas vacías."""
    return HistorialMovimientos()


@pytest.fixture
def historial_con_datos():
    """Historial con 3 movimientos ya cargados: (0,0) -> (0,1) -> (1,1).
    Se usa como base para probar operaciones sobre un historial "normal"."""
    h = HistorialMovimientos()
    h.agregar_al_final((0, 0))
    h.agregar_al_final((0, 1))
    h.agregar_al_final((1, 1))
    return h


# ------------------
# validar_posicion
# ------------------
# Esta función revisa que un movimiento sea una tupla (fila, columna)
# de dos enteros no negativos, antes de dejarlo entrar al historial.

class TestValidarPosicion:

    def test_posicion_valida_no_lanza_error(self):
        # Caso correcto: una tupla de dos enteros >= 0 debe pasar sin
        # lanzar ninguna excepción.
        validar_posicion((0, 0))
        validar_posicion((3, 5))

    def test_no_es_tupla_lanza_typeerror(self):
        # Si el valor no es una tupla (es texto, lista o número suelto),
        # debe rechazarse con TypeError: el TIPO de dato está mal,
        # no importa si el contenido sería válido.
        with pytest.raises(TypeError):
            validar_posicion("no es tupla")
        with pytest.raises(TypeError):
            validar_posicion([1, 2])  # una lista [1, 2] no es lo mismo que la tupla (1, 2)
        with pytest.raises(TypeError):
            validar_posicion(5)

    def test_tupla_de_tamano_incorrecto_lanza_typeerror(self):
        # Una posición siempre debe tener exactamente 2 elementos
        # (fila, columna).
        with pytest.raises(TypeError):
            validar_posicion((1,))  # solo un elemento
        with pytest.raises(TypeError):
            validar_posicion((1, 2, 3))  # tres elementos

    def test_elementos_no_enteros_lanza_typeerror(self):
        # Fila y columna deben ser números enteros. Decimales, texto
        # o None no son coordenadas válidas.
        with pytest.raises(TypeError):
            validar_posicion((1.5, 2))  # decimal
        with pytest.raises(TypeError):
            validar_posicion(("a", "b"))  # texto
        with pytest.raises(TypeError):
            validar_posicion((None, 2))  # vacío/nulo

    def test_booleanos_no_se_aceptan_como_enteros(self):
        # Detalle de Python: True y False técnicamente son una
        # subclase de int (True == 1, False == 0). Sin rechazarlos
        # explícitamente, alguien podría insertar (True, 1) por error
        # y pasaría la validación sin que tenga sentido como posición.
        with pytest.raises(TypeError):
            validar_posicion((True, 1))

    def test_valores_negativos_lanza_valueerror(self):
        # Aquí el tipo sí es correcto (son enteros), pero el valor no
        # tiene sentido: no existen filas o columnas negativas en una
        # matriz. Por eso se usa ValueError en vez de TypeError —
        # el dato está bien formado, pero su valor es inválido.
        with pytest.raises(ValueError):
            validar_posicion((-1, 0))
        with pytest.raises(ValueError):
            validar_posicion((0, -5))


# -----------------
# validar_no_vacio
# -----------------
# Verifica que el historial tenga al menos un movimiento antes de
# permitir operaciones como eliminar o consultar por índice.

class TestValidarNoVacio:

    def test_historial_vacio_lanza_valueerror(self, historial_vacio):
        # Un historial recién creado no tiene movimientos: cualquier
        # intento de quitar o leer algo de él debe fallar con
        # un mensaje claro.
        with pytest.raises(ValueError):
            validar_no_vacio(historial_vacio)

    def test_historial_con_datos_no_lanza_error(self, historial_con_datos):
        # Si ya hay movimientos guardados, la validación debe dejar
        # pasar sin lanzar ningún error.
        validar_no_vacio(historial_con_datos)  # no debe lanzar nada


# ----------------
# validar_indice
# ----------------
# Revisa que un índice (posición dentro del historial, no coordenada del
# laberinto) exista realmente: debe estar entre 0 y tamano-1.

class TestValidarIndice:

    def test_indice_valido_no_lanza_error(self, historial_con_datos):
        # historial_con_datos tiene 3 movimientos, así que los índices
        # válidos son 0, 1 y 2. Probamos el primero y el último límite.
        validar_indice(historial_con_datos, 0)
        validar_indice(historial_con_datos, 2)  # último índice válido

    def test_indice_fuera_de_rango_lanza_indexerror(self, historial_con_datos):
        # Con 3 movimientos, pedir el índice 3 (o cualquiera mayor)
        # se sale del historial: debe lanzar IndexError.
        with pytest.raises(IndexError):
            validar_indice(historial_con_datos, 3)
        with pytest.raises(IndexError):
            validar_indice(historial_con_datos, 100)

    def test_indice_negativo_lanza_indexerror(self, historial_con_datos):
        # Aquí los índices negativos se consideran inválidos
        # para mantener la validación simple y explícita.
        with pytest.raises(IndexError):
            validar_indice(historial_con_datos, -1)

    def test_indice_no_entero_lanza_typeerror(self, historial_con_datos):
        # Un índice debe ser un número entero.
        with pytest.raises(TypeError):
            validar_indice(historial_con_datos, "0")
        with pytest.raises(TypeError):
            validar_indice(historial_con_datos, 1.5)


# ---------------------------------------------------
# agregar_al_final_seguro / agregar_al_inicio_seguro
# ---------------------------------------------------
# Estas funciones combinan: primero validar_posicion(), y si pasa,
# se llaman a las operaciones reales de HistorialMovimientos
# (agregar_al_final / agregar_al_inicio).

class TestAgregarSeguro:

    def test_agregar_al_final_con_valor_valido(self, historial_vacio):
        # Con una posición válida, el movimiento debe quedar guardado
        # y el tamaño del historial debe aumentar en 1.
        agregar_al_final_seguro(historial_vacio, (2, 3))
        assert historial_vacio.tamano == 1
        assert historial_vacio.recorrer_adelante() == [(2, 3)]

    def test_agregar_al_inicio_con_valor_valido(self, historial_con_datos):
        # Al agregar al inicio, el nuevo movimiento debe aparecer
        # primero en el recorrido hacia adelante (antes que los 3 que
        # ya existían en historial_con_datos).
        agregar_al_inicio_seguro(historial_con_datos, (9, 9))
        assert historial_con_datos.recorrer_adelante()[0] == (9, 9)

    def test_agregar_valor_invalido_no_modifica_el_historial(self, historial_vacio):
        # Prueba: si el valor es inválido, la validación debe
        # detener la operación antes de tocar la estructura. El
        # historial debe quedar exactamente igual que antes del intento
        # (sigue vacío), no a medio modificar.
        with pytest.raises(TypeError):
            agregar_al_final_seguro(historial_vacio, "posicion_invalida")
        assert historial_vacio.tamano == 0
        assert historial_vacio.esta_vacia() is True


# ----------------
# eliminar_seguro
# ----------------
# Combina dos validaciones antes de eliminar: que el historial no esté
# vacío, y que el valor a eliminar sea una posición válida.

class TestEliminarSeguro:

    def test_eliminar_valor_existente(self, historial_con_datos):
        # Si el valor sí está en el historial, eliminar_seguro debe
        # devolver True, quitarlo del recorrido y reducir el tamaño.
        resultado = eliminar_seguro(historial_con_datos, (0, 1))
        assert resultado is True
        assert (0, 1) not in historial_con_datos.recorrer_adelante()
        assert historial_con_datos.tamano == 2  # tenía 3, ahora 2

    def test_eliminar_valor_inexistente_devuelve_false(self, historial_con_datos):
        # Si el valor es una posición válida pero no está guardada,
        # no es un error — simplemente no hay nada que eliminar.
        # Por eso devuelve False en vez de lanzar una excepción.
        resultado = eliminar_seguro(historial_con_datos, (5, 5))
        assert resultado is False
        assert historial_con_datos.tamano == 3  # el tamaño no cambia

    def test_eliminar_de_historial_vacio_lanza_valueerror(self, historial_vacio):
        # No tiene sentido eliminar algo de un historial que no
        # tiene absolutamente ningún movimiento guardado.
        with pytest.raises(ValueError):
            eliminar_seguro(historial_vacio, (0, 0))

    def test_eliminar_valor_de_tipo_incorrecto_lanza_typeerror(self, historial_con_datos):
        # Aunque el historial sí tenga datos, si lo que se pide eliminar
        # no es una posición válida, debe rechazarse por tipo antes de
        # siquiera intentar buscarlo.
        with pytest.raises(TypeError):
            eliminar_seguro(historial_con_datos, "no es posicion")


# --------------------
# obtener_por_indice
# --------------------
# Función nueva (no existía en HistorialMovimientos): permite consultar
# un movimiento por su posición dentro del historial, recorriendo desde
# la cabeza hasta llegar al índice pedido. Reutiliza validar_no_vacio()
# y validar_indice() antes de recorrer la lista.

class TestObtenerPorIndice:

    def test_obtiene_valor_correcto(self, historial_con_datos):
        # historial_con_datos guarda, en orden: (0,0), (0,1), (1,1).
        # obtener_por_indice(0) debe ser el primero, y así sucesivamente.
        assert obtener_por_indice(historial_con_datos, 0) == (0, 0)
        assert obtener_por_indice(historial_con_datos, 1) == (0, 1)
        assert obtener_por_indice(historial_con_datos, 2) == (1, 1)

    def test_indice_fuera_de_rango_lanza_indexerror(self, historial_con_datos):
        # Solo hay 3 movimientos (índices 0, 1, 2); pedir el índice 10
        # debe fallar con un mensaje claro en vez de recorrer la lista
        # hasta quedarse sin nodos y fallar.
        with pytest.raises(IndexError):
            obtener_por_indice(historial_con_datos, 10)

    def test_historial_vacio_lanza_valueerror(self, historial_vacio):
        # No hay nada que consultar en un historial vacío, sin importar
        # qué índice se pida.
        with pytest.raises(ValueError):
            obtener_por_indice(historial_vacio, 0)


# -----------
# Recorridos
# -----------
# Estas pruebas no validan entradas directamente, pero confirman que
# los recorridos adelante/atrás —que dependen de los punteros
# siguiente y anterior de cada Nodo— son compatibles entre sí.

class TestRecorridos:

    def test_recorrer_adelante_y_atras_son_inversos(self, historial_con_datos):
        # Si el historial es [0,0 -> 0,1 -> 1,1] de cabeza a cola,
        # recorrer_atras() debe devolver exactamente lo mismo pero al
        # revés: [1,1 -> 0,1 -> 0,0]. Esto confirma que los punteros
        # `anterior` de cada nodo están bien enlazados (lista doble).
        adelante = historial_con_datos.recorrer_adelante()
        atras = historial_con_datos.recorrer_atras()
        assert adelante == list(reversed(atras))

    def test_recorrer_historial_vacio_devuelve_lista_vacia(self, historial_vacio):
        # Recorrer un historial sin movimientos no debe lanzar ningún
        # error: simplemente debe devolver una lista vacía en ambos
        # sentidos.
        assert historial_vacio.recorrer_adelante() == []
        assert historial_vacio.recorrer_atras() == []