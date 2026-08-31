import os

for nivel in ['nivel1', 'nivel2', 'nivel3']:
    archivo = f'laberintos/{nivel}.txt'
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            lineas = [l.strip() for l in f if l.strip()]
        
        print(f'\n╔{"="*50}╗')
        print(f'║ {nivel.upper():^48} ║')
        print(f'║ Dimensiones: {len(lineas)}x{len(lineas[0]):>37} ║')
        print(f'╚{"="*50}╝\n')
        
        for linea in lineas:
            visual = ''
            for char in linea:
                if char == '0':
                    visual += '  '
                elif char == '1':
                    visual += '██'
                elif char == '2':
                    visual += 'E '
                elif char == '3':
                    visual += 'S '
            print(visual)
        print()
