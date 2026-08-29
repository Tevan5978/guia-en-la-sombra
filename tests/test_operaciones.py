"""
test_operaciones.py

Pruebas unitarias para src/operaciones.py.
Responsabilidad: Integrante 3.

Ejecutar desde la raíz del proyecto con:
    pytest tests/test_operaciones.py -v
"""

import pytest

from laberinto import Laberinto
from operaciones import (
    esta_dentro_de_limites,
    obtener_celda,
    recorrer_por_filas,
    recorrer_por_columnas,
    buscar_valor,
    buscar_entrada,
    buscar_salida,
    buscar_todas_las_coincidencias,
    imprimir_laberinto,
    CAMINO,
    PARED,
    ENTRADA,
    SALIDA,
)


# ---------------------------------------------------------------------------
# Fixtures: laberintos de prueba (chico, mediano, "grande")
# ---------------------------------------------------------------------------

@pytest.fixture
def laberinto_chico():
    """nivel1.txt: 5 filas x 7 columnas."""
    return Laberinto.desde_archivo("laberintos/nivel1.txt")


@pytest.fixture
def laberinto_mediano():
    """nivel2.txt: 9 filas x 9 columnas."""
    return Laberinto.desde_archivo("laberintos/nivel2.txt")


@pytest.fixture
def laberinto_grande():
    """
    nivel3.txt: 15 filas x 15 columnas, generado con
    generar_laberinto(15, 15) de src/generador.py (recursive backtracking).
    """
    return Laberinto.desde_archivo("laberintos/nivel3.txt")


# ---------------------------------------------------------------------------
# esta_dentro_de_limites
# ---------------------------------------------------------------------------

class TestEstaDentroDeLimites:

    def test_posicion_valida(self, laberinto_chico):
        assert esta_dentro_de_limites(laberinto_chico, 0, 0) is True
        assert esta_dentro_de_limites(laberinto_chico, 4, 6) is True  # última celda

    def test_posicion_fuera_de_rango(self, laberinto_chico):
        assert esta_dentro_de_limites(laberinto_chico, 5, 0) is False  # fila fuera
        assert esta_dentro_de_limites(laberinto_chico, 0, 7) is False  # columna fuera

    def test_indices_negativos(self, laberinto_chico):
        assert esta_dentro_de_limites(laberinto_chico, -1, 0) is False
        assert esta_dentro_de_limites(laberinto_chico, 0, -1) is False

    def test_funciona_con_laberinto_grande(self, laberinto_grande):
        assert esta_dentro_de_limites(laberinto_grande, 14, 14) is True
        assert esta_dentro_de_limites(laberinto_grande, 15, 15) is False


# ---------------------------------------------------------------------------
# obtener_celda
# ---------------------------------------------------------------------------

class TestObtenerCelda:

    def test_obtiene_valor_correcto(self, laberinto_chico):
        assert obtener_celda(laberinto_chico, 1, 1) == ENTRADA
        assert obtener_celda(laberinto_chico, 3, 5) == SALIDA
        assert obtener_celda(laberinto_chico, 0, 0) == PARED

    def test_lanza_indexerror_fuera_de_rango(self, laberinto_chico):
        with pytest.raises(IndexError):
            obtener_celda(laberinto_chico, 100, 100)

    def test_lanza_indexerror_con_indices_negativos(self, laberinto_chico):
        with pytest.raises(IndexError):
            obtener_celda(laberinto_chico, -1, -1)


# ---------------------------------------------------------------------------
# recorrer_por_filas / recorrer_por_columnas
# ---------------------------------------------------------------------------

class TestRecorridos:

    def test_recorrer_por_filas_visita_todas_las_celdas(self, laberinto_chico):
        celdas = list(recorrer_por_filas(laberinto_chico))
        assert len(celdas) == laberinto_chico.filas * laberinto_chico.columnas

    def test_recorrer_por_filas_orden_correcto(self, laberinto_chico):
        celdas = list(recorrer_por_filas(laberinto_chico))
        # La primera celda visitada debe ser (0,0) y la segunda (0,1)
        assert celdas[0][:2] == (0, 0)
        assert celdas[1][:2] == (0, 1)

    def test_recorrer_por_columnas_visita_todas_las_celdas(self, laberinto_chico):
        celdas = list(recorrer_por_columnas(laberinto_chico))
        assert len(celdas) == laberinto_chico.filas * laberinto_chico.columnas

    def test_recorrer_por_columnas_orden_correcto(self, laberinto_chico):
        celdas = list(recorrer_por_columnas(laberinto_chico))
        # Al recorrer por columnas, tras (0,0) sigue (1,0), no (0,1)
        assert celdas[0][:2] == (0, 0)
        assert celdas[1][:2] == (1, 0)

    def test_recorridos_consistentes_en_laberinto_mediano(self, laberinto_mediano):
        por_filas = list(recorrer_por_filas(laberinto_mediano))
        por_columnas = list(recorrer_por_columnas(laberinto_mediano))
        # Mismo total de celdas, mismo multiconjunto de valores, distinto orden
        assert len(por_filas) == len(por_columnas)
        assert sorted(v for _, _, v in por_filas) == sorted(v for _, _, v in por_columnas)


# ---------------------------------------------------------------------------
# Búsqueda de celdas
# ---------------------------------------------------------------------------

class TestBusqueda:

    def test_buscar_entrada_nivel1(self, laberinto_chico):
        assert buscar_entrada(laberinto_chico) == (1, 1)

    def test_buscar_salida_nivel1(self, laberinto_chico):
        assert buscar_salida(laberinto_chico) == (3, 5)

    def test_buscar_entrada_nivel2(self, laberinto_mediano):
        assert buscar_entrada(laberinto_mediano) == (1, 1)

    def test_buscar_salida_nivel2(self, laberinto_mediano):
        assert buscar_salida(laberinto_mediano) == (7, 7)

    def test_buscar_valor_inexistente_devuelve_none(self, laberinto_chico):
        assert buscar_valor(laberinto_chico, 99) is None

    def test_buscar_todas_las_coincidencias_una_sola_entrada(self, laberinto_chico):
        entradas = buscar_todas_las_coincidencias(laberinto_chico, ENTRADA)
        salidas = buscar_todas_las_coincidencias(laberinto_chico, SALIDA)
        assert len(entradas) == 1
        assert len(salidas) == 1

    def test_buscar_en_laberinto_grande(self, laberinto_grande):
        # generar_laberinto/colocar_entrada_salida siempre ubican la
        # entrada en (1,1) y la salida en (filas-2, columnas-2).
        assert buscar_entrada(laberinto_grande) == (1, 1)
        assert buscar_salida(laberinto_grande) == (13, 13)

    def test_laberinto_grande_tiene_una_sola_entrada_y_salida(self, laberinto_grande):
        entradas = buscar_todas_las_coincidencias(laberinto_grande, ENTRADA)
        salidas = buscar_todas_las_coincidencias(laberinto_grande, SALIDA)
        assert len(entradas) == 1
        assert len(salidas) == 1


# ---------------------------------------------------------------------------
# Impresión (solo verificamos que no lance errores)
# ---------------------------------------------------------------------------

class TestImpresion:

    def test_imprimir_con_simbolos_no_falla(self, laberinto_chico, capsys):
        imprimir_laberinto(laberinto_chico, usar_simbolos=True)
        salida = capsys.readouterr().out
        assert "E" in salida
        assert "S" in salida

    def test_imprimir_sin_simbolos_no_falla(self, laberinto_chico, capsys):
        imprimir_laberinto(laberinto_chico, usar_simbolos=False)
        salida = capsys.readouterr().out
        assert "2" in salida  # entrada como valor numérico
        assert "3" in salida  # salida como valor numérico

    def test_imprimir_laberinto_grande_no_falla(self, laberinto_grande, capsys):
        imprimir_laberinto(laberinto_grande)
        salida = capsys.readouterr().out
        assert len(salida.splitlines()) == 15