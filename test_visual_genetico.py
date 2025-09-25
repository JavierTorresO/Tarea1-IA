from laberinto import Laberinto
from algoritmo_genetico import AlgoritmoGenetico

def test_algoritmo_genetico():
    tamaño = 8
    prob_muro = 0.2
    laberinto = Laberinto(tamaño)
    
    laberinto.colocar_inicio(0, 0)
    laberinto.generar_salidas_aleatorias(min_salidas=2, max_salidas=3)
    laberinto.colocar_llave()
    laberinto.generar_muros_aleatorios(probabilidad=prob_muro, radio_seguro=1)
    
    print("\n🗺️ Laberinto inicial:")
    print(f"Inicio: {laberinto.inicio}")
    print(f"Llave: {laberinto.llave}")
    print(f"Salida real: {laberinto.salida_real}")
    laberinto.mostrar()

    ag = AlgoritmoGenetico(laberinto)
    mejor_solucion, mejor_fitness, _ = ag.evolucionar()
    
    resultado = ag.simular_cromosoma(mejor_solucion)
    
    print("\n✨ Resultados:")
    print(f"Mejor fitness: {mejor_fitness}")
    print(f"Longitud de la solución: {len(mejor_solucion)}")
    print(f"Encontró la llave: {'Sí' if resultado['tiene_llave'] else 'No'}")
    print(f"Llegó a la salida real: {'Sí' if resultado['salida_real'] else 'No'}")
    
    print("\n🔄 Camino recorrido:")
    for i, pos in enumerate(resultado['camino']):
        print(f"Paso {i+1}: posición {pos}")

if __name__ == "__main__":
    test_algoritmo_genetico()