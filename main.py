from src.laberinto import Laberinto
from src.operaciones import (
    imprimir_laberinto,
    buscar_entrada,
    buscar_salida,
    esta_dentro_de_limites,
    obtener_celda
)


print("=" * 50)
print("🕯️  GUÍA EN LAS SOMBRAS - VISUALIZADOR DE LABERINTOS")
print("=" * 50)

# Cargar laberinto
laberinto = Laberinto.desde_archivo("laberintos/nivel1.txt")

# 1. Validar estructura
print("\nVALIDACIÓN DEL LABERINTO")
print("-" * 50)
try:
    laberinto.validar()
    print("✅ Laberinto válido")
except ValueError as e:
    print(f"❌ Error de validación: {e}")

# 2. Mostrar información
print("\nINFORMACIÓN DEL LABERINTO")
print("-" * 50)
print(f"Dimensiones: {laberinto.filas} filas × {laberinto.columnas} columnas")
entrada = buscar_entrada(laberinto)
salida = buscar_salida(laberinto)
print(f"Entrada (E): {entrada}")
print(f"Salida (S): {salida}")

# 3. Visualización numérica
print("\nREPRESENTACIÓN NUMÉRICA")
print("-" * 50)
print("(0=Camino, 1=Pared, 2=Entrada, 3=Salida)")
laberinto.mostrar()

# 4. Visualización con símbolos
print("\nVISUALIZACIÓN CON SÍMBOLOS")
print("-" * 50)
print("(█=Pared, .=Camino, E=Entrada, S=Salida)")
imprimir_laberinto(laberinto, usar_simbolos=True)

# 5. Validación de acceso
print("\nPRUEBAS DE ACCESO")
print("-" * 50)
if entrada:
    f, c = entrada
    valor = obtener_celda(laberinto, f, c)
    print(f"Valor en entrada {entrada}: {valor} (esperado: 2)")
if salida:
    f, c = salida
    valor = obtener_celda(laberinto, f, c)
    print(f"Valor en salida {salida}: {valor} (esperado: 3)")

# 6. Validar límites
print("\nVALIDACIÓN DE LÍMITES")
print("-" * 50)
pruebas = [(0, 0), (laberinto.filas - 1, laberinto.columnas - 1), (100, 100)]
for fila, col in pruebas:
    dentro = esta_dentro_de_limites(laberinto, fila, col)
    print(f"¿({fila}, {col}) dentro de límites?: {dentro}")

print("\n" + "=" * 50)
print("Ejecución completada exitosamente")
print("=" * 50)