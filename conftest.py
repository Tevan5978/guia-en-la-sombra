"""
conftest.py

Agrega la carpeta src/ al path de Python para que los tests puedan
hacer `from laberinto import Laberinto` y `from operaciones import ...`
sin necesidad de reestructurar el proyecto en un paquete.
"""

import os
import sys

RAIZ_PROYECTO = os.path.dirname(os.path.abspath(__file__))
CARPETA_SRC = os.path.join(RAIZ_PROYECTO, "src")

if CARPETA_SRC not in sys.path:
    sys.path.insert(0, CARPETA_SRC)
    
    
    