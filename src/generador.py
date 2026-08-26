import random


def generar_laberinto(filas, columnas):
    """
    Genera un laberinto usando el algoritmo de
    recursive backtracking (DFS con retroceso).

    Regresa una matriz (lista de listas) con:
    0 = camino, 1 = pared
    """

    # Empezamos con una matriz llena de paredes (1)
    matriz = [[1 for _ in range(columnas)] for _ in range(filas)]

    # Empezamos a cavar desde la celda (1, 1)
    _cavar(matriz, 1, 1, filas, columnas)

    colocar_entrada_salida(matriz)

    return matriz


def _cavar(matriz, fila, columna, filas, columnas):
    """
    Función recursiva que abre caminos en la matriz,
    moviéndose de 2 en 2 celdas para dejar pared entre pasillos.
    """

    matriz[fila][columna] = 0  # marcamos la celda actual como camino

    direcciones = [(-2, 0), (2, 0), (0, -2), (0, 2)]  # arriba, abajo, izq, der
    random.shuffle(direcciones)  # orden aleatorio para que el laberinto varíe

    for delta_fila, delta_columna in direcciones:

        nueva_fila = fila + delta_fila
        nueva_columna = columna + delta_columna

        dentro_del_rango = (
            0 < nueva_fila < filas - 1
            and 0 < nueva_columna < columnas - 1
        )

        if dentro_del_rango and matriz[nueva_fila][nueva_columna] == 1:

            # rompemos la pared que está entre la celda actual y la nueva
            matriz[fila + delta_fila // 2][columna + delta_columna // 2] = 0

            _cavar(matriz, nueva_fila, nueva_columna, filas, columnas)


def colocar_entrada_salida(matriz):
    """
    Coloca la entrada (2) en la esquina superior izquierda
    y la salida (3) en la esquina inferior derecha del área
    transitable del laberinto.
    """

    filas = len(matriz)
    columnas = len(matriz[0])

    matriz[1][1] = 2  # entrada
    matriz[filas - 2][columnas - 2] = 3  # salida

    return matriz


def existe_camino(matriz):
    """
    Verifica que exista un camino válido entre la entrada (2)
    y la salida (3) usando una búsqueda en anchura (BFS).
    """

    filas = len(matriz)
    columnas = len(matriz[0])

    entrada = None
    salida = None

    for fila in range(filas):
        for columna in range(columnas):
            if matriz[fila][columna] == 2:
                entrada = (fila, columna)
            elif matriz[fila][columna] == 3:
                salida = (fila, columna)

    if entrada is None or salida is None:
        return False

    visitados = set()
    cola = [entrada]
    visitados.add(entrada)

    while cola:

        fila_actual, columna_actual = cola.pop(0)

        if (fila_actual, columna_actual) == salida:
            return True

        vecinos = [
            (fila_actual - 1, columna_actual),
            (fila_actual + 1, columna_actual),
            (fila_actual, columna_actual - 1),
            (fila_actual, columna_actual + 1),
        ]

        for vecino in vecinos:

            vecino_fila, vecino_columna = vecino

            dentro_del_rango = (
                0 <= vecino_fila < filas
                and 0 <= vecino_columna < columnas
            )

            if dentro_del_rango and vecino not in visitados:

                valor = matriz[vecino_fila][vecino_columna]

                if valor != 1:  # no es pared
                    visitados.add(vecino)
                    cola.append(vecino)

    return False


def guardar_en_archivo(matriz, ruta):
    """
    Guarda la matriz del laberinto en un archivo .txt,
    con el mismo formato que usa Laberinto.desde_archivo().
    """

    with open(ruta, "w") as archivo:

        for fila in matriz:

            linea = "".join(str(valor) for valor in fila)
            archivo.write(linea + "\n")

def imprimir_visual(matriz):
    """
    Imprime el laberinto en consola usando símbolos,
    para verlo de forma más parecida a un laberinto real.
    """

    simbolos = {
        0: " ",   # camino
        1: "█",   # pared
        2: "E",   # entrada
        3: "S",   # salida
    }

    for fila in matriz:

        linea = "".join(simbolos[valor] for valor in fila)
        print(linea)

if __name__ == "__main__":

    filas = 9
    columnas = 9

    matriz = generar_laberinto(filas, columnas)

    print("Laberinto generado:")
    imprimir_visual(matriz)

    if existe_camino(matriz):
        print("\n Existe un camino válido entre la entrada y la salida.")
    else:
        print("\n No se encontró un camino válido.")

    guardar_en_archivo(matriz, "laberintos/nivel2.txt")
    print("\nLaberinto guardado en laberintos/nivel2.txt")