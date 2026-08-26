from src.generador import (
    generar_laberinto,
    existe_camino,
)
from src.laberinto import Laberinto


def test_tamano_correcto():

    matriz = generar_laberinto(9, 9)

    assert len(matriz) == 9
    assert len(matriz[0]) == 9


def test_tiene_una_entrada_y_una_salida():

    matriz = generar_laberinto(9, 9)

    entradas = 0
    salidas = 0

    for fila in matriz:
        for valor in fila:
            if valor == Laberinto.ENTRADA:
                entradas += 1
            elif valor == Laberinto.SALIDA:
                salidas += 1

    assert entradas == 1
    assert salidas == 1


def test_existe_camino_valido():

    matriz = generar_laberinto(9, 9)

    assert existe_camino(matriz) is True


def test_solo_contiene_valores_validos():

    matriz = generar_laberinto(9, 9)

    valores_validos = (
        Laberinto.CAMINO,
        Laberinto.PARED,
        Laberinto.ENTRADA,
        Laberinto.SALIDA,
    )

    for fila in matriz:
        for valor in fila:
            assert valor in valores_validos


def test_matriz_generada_es_compatible_con_laberinto():

    matriz = generar_laberinto(9, 9)

    # Si Laberinto(matriz) no lanza error, es compatible
    laberinto = Laberinto(matriz)
    assert laberinto.validar() is True