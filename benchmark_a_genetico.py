import time
from laberinto import Laberinto
from algoritmo_genetico import AlgoritmoGenetico

def correr_prueba_genetico(prob_muro, tam, repeticiones=20, delay=0.0):
    """
    Corre varias pruebas usando el algoritmo genético con una probabilidad de muro y un tamaño dado.
    """
    print(f"\n===== PRUEBA GENÉTICO: tamaño={tam}, prob_muro={prob_muro}, repeticiones={repeticiones} =====")

    tiempos = []
    pasos_lista = []
    completados = 0
    fitness_lista = []

    for i in range(1, repeticiones + 1):
        # crear laberinto nuevo
        lab = Laberinto(tam, prob_muro)
        lab.colocar_inicio(0, 0)
        lab.generar_salidas_aleatorias(min_salidas=2, max_salidas=5)
        lab.colocar_llave()

        # correr el algoritmo genético
        start = time.time()
        ag = AlgoritmoGenetico(lab)
        mejor_cromosoma, mejor_fitness, historial = ag.evolucionar()
        end = time.time()
        duracion = end - start

        tiempos.append(duracion)
        fitness_lista.append(mejor_fitness)
     

        # evaluar si la mejor solución realmente salió
        resultado = lab.grid  # para referencia
        sim = ag.simular_cromosoma(mejor_cromosoma)

        if sim['salida_real'] and sim['tiene_llave']:
            completados += 1
            pasos_lista.append(len(sim['camino']))
            print(f"Iteración {i} lista (tiempo = {duracion:.3f}s, pasos = {len(sim['camino'])})")
        else:
            print(f"Iteración {i} falló (tiempo = {duracion:.3f}s, fitness={mejor_fitness})")

    # resultados finales
    prom_tiempo = sum(tiempos) / repeticiones
    prom_pasos = sum(pasos_lista) / len(pasos_lista) if pasos_lista else 0
    prom_fitness = sum(fitness_lista) / len(fitness_lista)
    print("\n===== RESULTADOS GENÉTICO =====")
    print(f"Éxitos: {completados}/{repeticiones}")
    print(f"Tiempo promedio: {prom_tiempo:.3f}s")
    print(f"Pasos promedio (solo casos exitosos): {prom_pasos:.2f}")
    print(f"Fitness promedio: {prom_fitness:.1f}")

if __name__ == "__main__":
    correr_prueba_genetico(prob_muro=0.1, tam=8, repeticiones=20, delay=0.0)
