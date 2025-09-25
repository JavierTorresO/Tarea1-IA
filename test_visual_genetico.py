from laberinto import Laberinto
from algoritmo_genetico import AlgoritmoGenetico

def test_algoritmo_genetico():
    # Crear laberinto
    tamaño = 8
    laberinto = Laberinto(tamaño)
    
    # Colocar inicio, salidas y llave
    laberinto.colocar_inicio(0, 0)
    laberinto.generar_salidas_aleatorias(min_salidas=2, max_salidas=3)
    laberinto.colocar_llave()
    
    print("🗺️ Laberinto inicial:")
    laberinto.mostrar()  # Muestra el laberinto con salidas y llave

    # Ejecutar el algoritmo genético
    ag = AlgoritmoGenetico(laberinto)
    mejor_solucion, mejor_fitness, _ = ag.evolucionar()
    
    # Mostrar los resultados
    print("\n✨ Resultados:")
    print(f"Mejor fitness: {mejor_fitness}")
    print(f"Longitud de la solución: {len(mejor_solucion)}")
    print("\n🔄 Movimientos realizados por el agente:")
    for i, movimiento in enumerate(mejor_solucion):
        print(f"Movimiento {i+1}: {movimiento}")
# Ejecutar el test
if __name__ == "__main__":
    test_algoritmo_genetico()