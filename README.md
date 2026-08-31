# 🕯️ Guía en las Sombras

## Descripción
**Guía en las Sombras** es un videojuego de laberintos desarrollado como proyecto final de la asignatura Estructuras de Datos. El proyecto consiste en crear laberintos representados mediante matrices bidimensionales, donde un agente debe encontrar el camino desde un punto de inicio hasta una meta utilizando diferentes estructuras de datos y algoritmos de búsqueda.

## Objetivo
Aplicar de forma práctica los conceptos de complejidad algorítmica, estructuras de datos estáticas y dinámicas (matrices, pilas, colas, recursividad) y teoría de grafos, mediante la generación y resolución visual de laberintos.

## Características
- ✅ Generación de laberintos usando algoritmos de backtracking.
- ✅ Representación mediante matrices bidimensionales.
- ✅ Validación de estructura de laberintos.
- ✅ Carga de laberintos desde archivos de texto.
- ✅ Operaciones sobre matrices (búsqueda, recorrido, validación).
- ✅ Visualización en consola con símbolos.
- ✅ Pruebas unitarias completas con pytest.
- ✅ Documentación detallada de componentes.

## Estructura del Proyecto

```
guia-en-la-sombra-1/
├── src/
│   ├── laberinto.py          # Clase principal Laberinto
│   ├── generador.py          # Generación de laberintos
│   └── operaciones.py        # Operaciones sobre matrices
├── tests/
│   ├── test_laberinto.py     # Pruebas de la clase Laberinto
│   ├── test_generador.py     # Pruebas de generación
│   └── test_operaciones.py   # Pruebas de operaciones
├── laberintos/
│   ├── nivel1.txt            # Laberinto pequeño (5×7)
│   ├── nivel2.txt            # Laberinto mediano (9×9)
│   └── nivel3.txt            # Laberinto grande (15×15)
├── docs/
│   ├── estructura-laberinto.md      # Documentación de estructura
│   └── material-de-entrega.md       # Documentación de operaciones
├── main.py                   # Script principal
├── ver_laberintos.py         # Visualizador de laberintos en consola
├── conftest.py               # Configuración de pytest
└── requirements.txt          # Dependencias del proyecto
```

## Representación del Laberinto

El laberinto se representa mediante una matriz 2D con los siguientes valores:

| Valor | Significado |
|:-----:|-------------|
| `0`   | Camino libre |
| `1`   | Pared |
| `2`   | Entrada |
| `3`   | Salida |

### Ejemplo:
```
1111111
1200011
1011001
1000031
1111111
```

## Módulos Principales

### `src/laberinto.py`
Clase principal que encapsula la representación del laberinto.
- `__init__(matriz)` - Inicializa con una matriz
- `desde_archivo(ruta)` - Carga un laberinto desde archivo
- `validar()` - Valida la estructura del laberinto
- `mostrar()` - Imprime el laberinto en consola

### `src/generador.py`
Genera laberintos automáticamente usando algoritmos de backtracking.
- `generar_laberinto(filas, columnas)` - Genera un laberinto aleatorio
- `colocar_entrada_salida(matriz)` - Coloca entrada y salida
- `existe_camino(matriz)` - Verifica que exista solución
- `guardar_en_archivo(matriz, ruta)` - Guarda a archivo
- `imprimir_visual(matriz)` - Imprime con símbolos visuales

### `src/operaciones.py`
Operaciones sobre vectores/matrices:
- `esta_dentro_de_limites()` - Validación de límites
- `obtener_celda()` - Acceso a celdas
- `recorrer_por_filas/columnas()` - Iteradores de recorrido
- `buscar_valor()` - Busca una celda específica
- `buscar_entrada/salida()` - Localiza puntos especiales
- `buscar_todas_las_coincidencias()` - Encuentra todas las coincidencias
- `imprimir_laberinto()` - Imprime con formato

## Uso del Proyecto

### Ejecutar el programa principal:
```bash
python main.py
```

### Ver visualización de laberintos:
```bash
python ver_laberintos.py
```

### Ejecutar pruebas:
```bash
pytest tests/ -v
```

### Ejecutar pruebas con cobertura:
```bash
pytest tests/ --cov=src
```

## Tecnologías Utilizadas
- **Lenguaje:** Python 3.8+
- **Testing:** pytest
- **Control de versiones:** Git y GitHub

## Integrantes
- Carlos Daniel Jiménez
- Estevan Gonzalez Beltrán
- Isabella Flórez

## Uso Educativo de IA
Este proyecto ha sido desarrollado utilizando IA (GitHub Copilot) de manera **educativa y responsable** para:
- Recibir asesoramiento en el diseño de estructuras de datos
- Optimizar algoritmos y mejorar la calidad del código
- Facilitar la documentación del proyecto
- Acelerar el proceso de desarrollo sin comprometer el aprendizaje

El uso de IA ha sido complementario al aprendizaje, permitiendo que los integrantes se enfoquen en los conceptos fundamentales de Estructuras de Datos mientras se recibe retroalimentación técnica.

## Documentación Adicional
- [Estructura y Representación del Laberinto](docs/estructura-laberinto.md)
- [Material de Entrega - Operaciones](docs/material-de-entrega.md)
