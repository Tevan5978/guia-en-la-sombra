class Laberinto:

    CAMINO = 0
    PARED = 1
    ENTRADA = 2
    SALIDA = 3

    def __init__(self, matriz):
        if matriz is None:
            raise ValueError("La matriz no puede ser nula.")

        if not matriz:
            raise ValueError("La matriz no puede estar vacía.")

        if not all(isinstance(fila, (list, tuple)) for fila in matriz):
            raise ValueError("Cada fila de la matriz debe ser una lista o tupla.")

        if not matriz[0]:
            raise ValueError("La matriz no puede contener filas vacías.")

        numero_columnas = len(matriz[0])

        for fila in matriz:
            if len(fila) != numero_columnas:
                raise ValueError(
                    "Todas las filas del laberinto deben tener el mismo tamaño."
                )

            for valor in fila:
                if valor not in (self.CAMINO, self.PARED, self.ENTRADA, self.SALIDA):
                    raise ValueError(f"Valor inválido encontrado: {valor}")

        self.matriz = [list(fila) for fila in matriz]
        self.filas = len(self.matriz)
        self.columnas = len(self.matriz[0])

    def mostrar(self):
        for fila in self.matriz:
            print(fila)

    def validar(self):

        if not self.matriz:
            raise ValueError("El laberinto está vacío.")

        if any(len(fila) != self.columnas for fila in self.matriz):
            raise ValueError(
                "Todas las filas del laberinto deben tener el mismo tamaño."
            )

        entradas = 0
        salidas = 0

        for fila in self.matriz:

            for valor in fila:

                if valor == self.ENTRADA:
                    entradas += 1

                elif valor == self.SALIDA:
                    salidas += 1

                elif valor not in (
                    self.CAMINO,
                    self.PARED
                ):
                    raise ValueError(
                        f"Valor inválido encontrado: {valor}"
                    )

        if entradas != 1:
            raise ValueError(
                "El laberinto debe tener exactamente una entrada."
            )

        if salidas != 1:
            raise ValueError(
                "El laberinto debe tener exactamente una salida."
            )

        return True

    @classmethod
    def desde_archivo(cls, ruta):

        matriz = []

        with open(ruta, "r") as archivo:

            for linea in archivo:

                linea = linea.strip()

                if linea:
                    fila = [int(valor) for valor in linea]
                    matriz.append(fila)

        if not matriz:
            raise ValueError("El archivo del laberinto está vacío.")

        numero_columnas = len(matriz[0])

        for fila in matriz:

            if len(fila) != numero_columnas:
                raise ValueError(
                    "Todas las filas del laberinto deben tener el mismo tamaño."
                )

        laberinto = cls(matriz)

        laberinto.validar()

        return laberinto