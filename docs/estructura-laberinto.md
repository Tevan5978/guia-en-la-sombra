# Estructura y representación del laberinto

## Proyecto: Guía en la Sombra

Esta sección documenta la estructura utilizada para representar y cargar los laberintos del videojuego **Guía en la Sombra**.

La implementación corresponde al componente de **Estructura y representación del laberinto**.

---

## Responsabilidad

La función principal de este componente es definir cómo se representa un laberinto dentro del programa y proporcionar las herramientas necesarias para crear, cargar y validar diferentes laberintos.

Las principales funciones implementadas son:

- Representación del laberinto mediante una matriz 2D.
- Definición de los valores utilizados por cada celda.
- Creación e inicialización de la matriz.
- Carga de laberintos desde archivos `.txt`.
- Validación de la estructura del laberinto.
- Validación de la entrada y salida.
- Validación del tamaño de las filas.

---

# Representación del laberinto

El laberinto se representa mediante una **matriz bidimensional (2D)**.

Cada posición de la matriz representa una celda del laberinto.

Se utilizan los siguientes valores:

| Valor | Significado |
|------:|-------------|
| `0` | Camino |
| `1` | Pared |
| `2` | Entrada |
| `3` | Salida |

Esta representación será utilizada por los algoritmos de búsqueda del proyecto, como BFS, DFS y A*.

---

## Ejemplo de una matriz

Un laberinto puede representarse de la siguiente manera:

```text
1111111
1200011
1011001
1000031
1111111
```

---

## Uso Educativo de IA

Este componente y su documentación han sido desarrollados utilizando **IA (GitHub Copilot)** de manera educativa para:

- Asesoramiento en el diseño de estructuras de datos
- Validación de la representación matricial
- Documentación clara y organizada del componente
- Optimización del código de validación

El uso de IA ha sido complementario al aprendizaje, facilitando que los estudiantes se enfoquen en los **conceptos fundamentales** de Estructuras de Datos mientras reciben retroalimentación técnica sobre implementación y documentación.

---

**Proyecto:** Guía en las Sombras - Videojuego de Laberintos