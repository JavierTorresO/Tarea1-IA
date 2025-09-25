import time
from laberinto import Laberinto
from agente import Agente
from algoritmo_a_estrella import a_estrella_con_llave  

# que mantenemos siempre igual: delay, salidas min y max, el inicio siempre en 0,0

def correr_prueba(prob_muro, tam, repeticiones=20, delay=0.0):
    # hace varias repeticiones a la vez con una probabilidad y un tamaño dado 
    print(f"\n===== PRUEBA: tamaño={tam}, prob_muro={prob_muro}, repeticiones={repeticiones} =====")

    tiempos = [] #almacenar los tiempos por iteracion
    pasos_lista = [] #almacenar los pasos por iteracion
    completados = 0 #cuantos intentos exitosos

    for i in range(1, repeticiones + 1):
        # crear laberinto y agente nuevos cada vez
        lab = Laberinto(tam, prob_muro)
        lab.colocar_inicio(0, 0) #siempre el inicio será en o,o
        lab.generar_salidas_aleatorias(min_salidas=2, max_salidas=5) #siempre las salidas entre ese rango
        lab.colocar_llave()
        agente = Agente(lab)

        start = time.time()
        pasos = a_estrella_con_llave(lab, agente, delay=delay)
        end = time.time()
        duracion = end - start # cuanto dura cada intento

        tiempos.append(duracion)
        if pasos is not None:   # si no quedó bloqueado...
            completados += 1 # es un juego que se completó y suma al contador de completados
            pasos_lista.append(pasos)
            print(f"Iteración {i} lista (tiempo = {duracion:.3f}s, pasos = {pasos})") #cada iteracion con su tiempo y sus pasos
        else:
            print(f"Iteración {i} falló (bloqueado) (tiempo = {duracion:.3f}s)") #cada iteracion fallida con su tiempo

    # resutados finales
    prom_tiempo = sum(tiempos) / repeticiones 
    prom_pasos = sum(pasos_lista) / len(pasos_lista) if pasos_lista else 0 
    print("\n===== RESULTADOS =====")
    print(f"Éxitos: {completados}/{repeticiones}") #cuantos casos fueron completados correctamente
    print(f"Tiempo promedio: {prom_tiempo:.3f}s") #promedio de todos los tiempos segun la cantidad de repeticiones 
    print(f"Pasos promedio (solo casos exitosos): {prom_pasos:.2f}") #promedio de todos los pasos (casos exitosos)

if __name__ == "__main__":
    # Cambiar los valores para cada prueba que se haga (mantener el delay si siempre)
    correr_prueba(prob_muro=0.2, tam=10, repeticiones=20, delay=0.0)
