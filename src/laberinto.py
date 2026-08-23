class Laberinto:
    
    CAMINO = 0
    PARED = 1
    ENTRADA = 2
    SALIDA = 3

    def __init__(self, matriz):
        self.matriz = matriz
        self.filas = len(matriz)
        self.columnas = len(matriz[0])

    def mostrar(self):
        for fila in self.matriz:
            print(fila)

    @classmethod
    def desde_archivo(cls, ruta):

        matriz = []

        with open(ruta, "r") as archivo:

            for linea in archivo:

                linea = linea.strip()

                if linea:
                    fila = [int(valor) for valor in linea]
                    matriz.append(fila)

        return cls(matriz)
        def validar(self):
    
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
                        f"Valor inválido: {valor}"
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
