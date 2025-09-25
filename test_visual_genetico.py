from laberinto import Laberinto
from algoritmo_genetico import AlgoritmoGenetico
import time
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def visualizar_movimientos(laberinto, cromosoma):
    # Posicion inicial
    fila_actual, col_actual = laberinto.inicio
    tiene_llave = False
    
    # copiar el laberinto para no modificar el original
    grid_original = [fila.copy() for fila in laberinto.grid]
    
    # simbolos
    AGENTE = '🤖'
    CAMINO = '👣'
    
    print("Simulando movimientos del mejor cromosoma encontrado...")
    print("🔑 Llave en:", laberinto.llave)
    print("🚪 Salida real en:", laberinto.salida_real)
    print("\nPresiona Enter para ver cada movimiento...")
    input()
    
    for i, movimiento in enumerate(cromosoma):
        limpiar_pantalla()
        
        # calcular nueva posicion
        nueva_fila, nueva_col = fila_actual, col_actual
        if movimiento == 'ARRIBA':
            nueva_fila -= 1
        elif movimiento == 'ABAJO':
            nueva_fila += 1
        elif movimiento == 'IZQUIERDA':
            nueva_col -= 1
        elif movimiento == 'DERECHA':
            nueva_col += 1
            
        # verificar si el movimiento es valido
        if (0 <= nueva_fila < laberinto.n and 
            0 <= nueva_col < laberinto.n and 
            laberinto.grid[nueva_fila][nueva_col] != laberinto.MUROS):
            
            # marcar el camino anterior
            if laberinto.grid[fila_actual][col_actual] == laberinto.LIBRES:
                laberinto.grid[fila_actual][col_actual] = -1  # Marcador de camino
                
            # actualizar posicion
            fila_actual, col_actual = nueva_fila, nueva_col
            
            # ver si recogio la llave
            if (fila_actual, col_actual) == laberinto.llave:
                tiene_llave = True
                print("🎉 ¡Ha recogido la llave!")
        
        print(f"Movimiento {i+1}/{len(cromosoma)}: {movimiento}")
        print(f"Posición actual: ({fila_actual}, {col_actual})")
        print(f"Tiene llave: {'✅' if tiene_llave else '❌'}")
        
        # mostrar laberinto
        simbolos = {
            laberinto.LIBRES: '⬜',
            laberinto.MUROS: '🟥',
            laberinto.PUNTO_PARTIDA: '🟢',
            laberinto.SALIDAS: '🚪',
            laberinto.LLAVE: '🔑',
            -1: '👣'  # Camino recorrido
        }
        
        # mostrar el laberinto con el agente
        for f in range(laberinto.n):
            fila = ""
            for c in range(laberinto.n):
                if (f, c) == (fila_actual, col_actual):
                    fila += AGENTE + " "
                else:
                    fila += simbolos[laberinto.grid[f][c]] + " "
            print(fila)
            
        input("Presiona Enter para el siguiente movimiento...")
    
    laberinto.grid = grid_original

def main():
    # crear laberinto
    tamaño = 8
    laberinto = Laberinto(tamaño)
    
    laberinto.colocar_inicio(0, 0)
    laberinto.generar_salidas_aleatorias(min_salidas=2, max_salidas=3)
    laberinto.colocar_llave()
    laberinto.generar_muros_aleatorios(0.2)
    
    print("🗺️ Laberinto inicial:")
    laberinto.mostrar()
    input("Presiona Enter para comenzar la búsqueda genética...")
    
    ag = AlgoritmoGenetico(laberinto)
    mejor_solucion, mejor_fitness, _ = ag.evolucionar()
    
    print("\n✨ Resultados:")
    print(f"Mejor fitness: {mejor_fitness}")
    print(f"Longitud de la solución: {len(mejor_solucion)}")
    
    visualizar_movimientos(laberinto, mejor_solucion)

if __name__ == "__main__":
    main()