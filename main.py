from src.laberinto import Laberinto


laberinto = Laberinto.desde_archivo(
    "laberintos/nivel1.txt"
)

laberinto.mostrar()