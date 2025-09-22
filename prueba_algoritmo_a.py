from laberinto import Laberinto
from agente import Agente
from algoritmo_a_estrella import a_estrella
lab = Laberinto(10, prob_muro=0.2, radio_seguro=1)

lab.colocar_inicio(0, 0)
lab.generar_salidas_aleatorias(min_salidas=2, max_salidas=4)
lab.colocar_llave()

print("Laberinto generado:")
lab.mostrar()
print("Inicio:", lab.inicio)
print("Llave:", lab.llave)

    # Buscar camino con A*
camino = a_estrella(lab, lab.inicio, lab.llave)

if camino:
    print("\n✅ Se encontró un camino a la llave.")
    print("Camino:", camino)
        # Mostrar camino sobre el grid
    for f, c in camino:
        if lab.grid[f][c] == lab.LIBRES:
            lab.grid[f][c] = -1  # marcar el camino
    simbolos = {
        lab.LIBRES: '⬜', lab.MUROS: '🟥',
        lab.PUNTO_PARTIDA: '🟢', lab.SALIDAS: '🚪',
        lab.LLAVE: '🔑', -1: '🟩'
        }
    print("\nLaberinto con camino a la llave (🟩):")
    for fila in lab.grid:
        print(' '.join(simbolos[val] for val in fila))
else:
    print("\n❌ No hay camino hacia la llave.")
