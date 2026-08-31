# Material de entrega — Operaciones con vectores/matrices, pruebas y documentación

**Proyecto:** Guía en las Sombras
**Componente:** `src/operaciones.py` y `tests/test_operaciones.py`

## 1. Resumen

Este documento describe las operaciones sobre vectores/matrices implementadas
sobre la clase `Laberinto` (definida en `src/laberinto.py`), y presenta las
pruebas realizadas para validarlas usando los laberintos del proyecto
(`laberintos/nivel1.txt`, `laberintos/nivel2.txt` y `laberintos/nivel3.txt`).

La representación del laberinto sigue el formato definido en
[`docs/estructura-laberinto.md`](../docs/estructura-laberinto.md):

| Valor | Significado |
|-------|-------------|
| 0     | Camino      |
| 1     | Pared       |
| 2     | Entrada     |
| 3     | Salida      |

## 2. Operaciones implementadas

Todas las funciones viven en `src/operaciones.py` y aceptan tanto una
instancia de `Laberinto` como una matriz "cruda" (lista de listas), lo que
facilita probarlas de forma aislada sin depender de un archivo `.txt`.

| Función | Descripción |
|---|---|
| `esta_dentro_de_limites(objeto, fila, columna)` | Valida que una posición exista dentro de la matriz. |
| `obtener_celda(objeto, fila, columna)` | Devuelve el valor de una celda; lanza `IndexError` si está fuera de rango. |
| `recorrer_por_filas(objeto)` | Recorre la matriz fila por fila (izquierda a derecha). |
| `recorrer_por_columnas(objeto)` | Recorre la matriz columna por columna (arriba a abajo). |
| `buscar_valor(objeto, valor)` | Busca la primera celda con un valor dado. |
| `buscar_entrada(objeto)` / `buscar_salida(objeto)` | Atajos para localizar la entrada (2) y la salida (3). |
| `buscar_todas_las_coincidencias(objeto, valor)` | Lista todas las celdas con un valor dado (soporte para validar que solo exista una entrada y una salida). |
| `imprimir_laberinto(objeto, usar_simbolos=True)` | Imprime el laberinto en consola, con símbolos legibles o valores numéricos. |

## 3. Casos de prueba

Las pruebas se implementaron con `pytest` en `tests/test_operaciones.py`,
cubriendo tres tamaños de laberinto:

- **Chico** — `laberintos/nivel1.txt` (5×7)
- **Mediano** — `laberintos/nivel2.txt` (9×9)
- **Grande** — `laberintos/nivel3.txt` (15×15)

Se agrupan en cuatro categorías:

1. **Validación de límites** (`TestEstaDentroDeLimites`): posiciones válidas,
   fuera de rango e índices negativos.
2. **Acceso a elementos** (`TestObtenerCelda`): lectura correcta de celdas y
   manejo de `IndexError` en posiciones inválidas.
3. **Recorridos** (`TestRecorridos`): verificación de que se visitan todas
   las celdas, en el orden esperado, tanto por filas como por columnas.
4. **Búsqueda de celdas** (`TestBusqueda`): localización de entrada y salida
   en los tres tamaños de laberinto, valor inexistente, y verificación de
   que exista exactamente una entrada y una salida.
5. **Impresión** (`TestImpresion`): la función de impresión no falla y
   produce salida coherente con y sin símbolos.

**Resultado: 23 pruebas, todas exitosas.**

```
$ python -m pytest tests/test_operaciones.py -v
============================= test session starts ==============================
collected 23 items

tests/test_operaciones.py::TestEstaDentroDeLimites::test_posicion_valida PASSED
tests/test_operaciones.py::TestEstaDentroDeLimites::test_posicion_fuera_de_rango PASSED
tests/test_operaciones.py::TestEstaDentroDeLimites::test_indices_negativos PASSED
tests/test_operaciones.py::TestEstaDentroDeLimites::test_funciona_con_laberinto_grande PASSED
tests/test_operaciones.py::TestObtenerCelda::test_obtiene_valor_correcto PASSED
tests/test_operaciones.py::TestObtenerCelda::test_lanza_indexerror_fuera_de_rango PASSED
tests/test_operaciones.py::TestObtenerCelda::test_lanza_indexerror_con_indices_negativos PASSED
tests/test_operaciones.py::TestRecorridos::test_recorrer_por_filas_visita_todas_las_celdas PASSED
tests/test_operaciones.py::TestRecorridos::test_recorrer_por_filas_orden_correcto PASSED
tests/test_operaciones.py::TestRecorridos::test_recorrer_por_columnas_visita_todas_las_celdas PASSED
tests/test_operaciones.py::TestRecorridos::test_recorrer_por_columnas_orden_correcto PASSED
tests/test_operaciones.py::TestRecorridos::test_recorridos_consistentes_en_laberinto_mediano PASSED
tests/test_operaciones.py::TestBusqueda::test_buscar_entrada_nivel1 PASSED
tests/test_operaciones.py::TestBusqueda::test_buscar_salida_nivel1 PASSED
tests/test_operaciones.py::TestBusqueda::test_buscar_entrada_nivel2 PASSED
tests/test_operaciones.py::TestBusqueda::test_buscar_salida_nivel2 PASSED
tests/test_operaciones.py::TestBusqueda::test_buscar_valor_inexistente_devuelve_none PASSED
tests/test_operaciones.py::TestBusqueda::test_buscar_todas_las_coincidencias_una_sola_entrada PASSED
tests/test_operaciones.py::TestBusqueda::test_buscar_en_laberinto_grande PASSED
tests/test_operaciones.py::TestBusqueda::test_laberinto_grande_tiene_una_sola_entrada_y_salida PASSED
tests/test_operaciones.py::TestImpresion::test_imprimir_con_simbolos_no_falla PASSED
tests/test_operaciones.py::TestImpresion::test_imprimir_sin_simbolos_no_falla PASSED
tests/test_operaciones.py::TestImpresion::test_imprimir_laberinto_grande_no_falla PASSED

============================== 23 passed in 0.21s ==============================
```

## 4. Imágenes — visualización en consola

### 4.1 `laberintos/nivel1.txt` (5×7)

```
███████
█E...██
█.██..█
█....S█
███████
Entrada: (1, 1)
Salida: (3, 5)
```

### 4.2 `laberintos/nivel2.txt` (9×9)

```
█████████
█E..█...█
███.█.█.█
█.█.█.█.█
█.█.█.█.█
█.█.█.█.█
█.█.███.█
█......S█
█████████
Entrada: (1, 1)
Salida: (7, 7)
```

### 4.3 `laberintos/nivel3.txt` (15×15)

```
███████████████
█E█.......█...█
█.███.███.█.█.█
█...█.█.█...█.█
███.█.█.█████.█
█.█.█.█.█.....█
█.█.█.█.█.███.█
█.█.█.█.█.█...█
█.█.█.█.█.█████
█.█.█.█.█.█...█
█.█.█.█.█.█.█.█
█...█...█...█.█
█.███████████.█
█............S█
███████████████
Entrada: (1, 1)
Salida: (13, 13)
```

> **Nota:** Las imágenes anteriores son la salida real de
> `imprimir_laberinto()` ejecutada en consola.

## 5. ¿Cómo ejecutar las pruebas?

Desde la raíz del proyecto, con `conftest.py`
y `pytest` instalado:

```bash
pip install pytest
python -m pytest tests/test_operaciones.py -v
```

---

## 6. Uso Educativo de IA

Este componente y su documentación han sido desarrollados utilizando **IA (GitHub Copilot)** de manera educativa para:

- Diseño de operaciones eficientes sobre matrices
- Definición de casos de prueba exhaustivos
- Documentación clara de funciones y su comportamiento
- Validación de la calidad del código

El uso de IA ha sido complementario al aprendizaje, facilitando que los estudiantes se enfoquen en los **algoritmos fundamentales** mientras reciben retroalimentación técnica sobre implementación, testing y documentación.

---

**Componente desarrollado por:** Estevan González Beltrán  
**Proyecto:** Guía en las Sombras - Videojuego de Laberintos