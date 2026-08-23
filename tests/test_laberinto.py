from src.laberinto import Laberinto


def test_cargar_laberinto():

    laberinto = Laberinto.desde_archivo(
        "laberintos/nivel1.txt"
    )

    assert laberinto.filas == 5
    assert laberinto.columnas == 7
    assert laberinto.matriz[1][1] == Laberinto.ENTRADA
    assert laberinto.matriz[3][5] == Laberinto.SALIDA