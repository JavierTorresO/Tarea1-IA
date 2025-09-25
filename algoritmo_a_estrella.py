from queue import PriorityQueue
import time
import random

def heuristica(fila, columna):
    # distancia Manhattan como heuristica
    distancia_m = abs(fila[0] - columna[0]) + abs(fila[1] - columna[1])
    return distancia_m

def a_estrella(laberinto, inicio, objetivo):
    tamaño = laberinto.n
    # priority queue para guardar por su costo f(n) = g(n) + h(n)
    explorar_cola = PriorityQueue()
    explorar_cola.put((0, inicio))  # añadimos el nodo inicio con f(n)=0
    nodo_anterior = {inicio: None} #aqui reconstruir el camino del algoritmo
    g_n = {inicio: 0} #costo real desde el inicio a cada nodo

    while not explorar_cola.empty(): #mientras haya nodos por explorar
        i, actual = explorar_cola.get() #sacamos el nodo con menor f(n)

        if actual == objetivo: # si llegamos al objetivo
            # reconstruir camino hacia atras
            camino = [] 
            while actual:
                camino.append(actual)
                actual = nodo_anterior[actual] 
            return camino[::-1]  # invertir para tener camino de inicio a objetivo

        # generar los vecinos (arriba, abajo, izquierda, derecha)
        for df, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nf, nc = actual[0] + df, actual[1] + dc
            #debe estar dentro del laberinto
            if 0 <= nf < tamaño and 0 <= nc < tamaño:
                if laberinto.grid[nf][nc] == laberinto.MUROS:
                    continue  #saltar si es un muro

                vecino = (nf, nc)
                
                costo_vecino_g = g_n[actual] + 1  # costo g vecino
                #si no hay vecino o encontramos camino mas barato
                if vecino not in g_n or costo_vecino_g < g_n[vecino]:
                    # actualizar costo g real
                    g_n[vecino] = costo_vecino_g
                    #calcular f(n) = g(n) + h(n)
                    f_n = costo_vecino_g + heuristica(vecino, objetivo)
                    #añadir a la cola de prioridad
                    explorar_cola.put((f_n, vecino))
                    nodo_anterior[vecino] = actual #guardaar por donde llegamos al vecino

    return None  # no se encontro camino


def mover_aleatoriamente(laberinto, agente, delay=0.5):
    # mueve al Agente a una posicion vecina  aleatoriamente (que no sea muro)...
    f, c = agente.posicion
    movimientos = [(-1,0),(1,0),(0,-1),(0,1)]
    random.shuffle(movimientos)
    for df, dc in movimientos:
        nf, nc = f + df, c + dc
        if 0 <= nf < laberinto.n and 0 <= nc < laberinto.n and laberinto.grid[nf][nc] != laberinto.MUROS:
            agente.posicion = (nf, nc)
            agente.verificar_llave_y_salida()
            laberinto.mover_muros()
            agente.mostrar_laberinto()
            time.sleep(delay)
            return True # siesque se movio a una posicion vecina al azar
    return False  # siesque no habian movimientos posibles


def a_estrella_con_llave(laberinto, agente, delay=0.3):
    """
    Se cambio a un 'A* incremental'
    -con cada paso que hace el agente se recalcula el camino
    -al recoger la llave se van a probar las salidas desde la más cercana hasta la más lejana del punto donde se recogio la llave hasta encontrar la real
    -ULTIMO AÑADIDO: juego infinito, si da la casualidad de que no haya ningun camino para llegar a la llave/salida, el agente se va a mover los lados hasta que de la probabilidad de mover los muros y que se libere un camino para llegar al objetivo
                    unico bloqueo posible: si al moverse el Agente se mueven los muros y lo dejan rodeado de muros y no pueda moverse a ningun lado
    """

    pasos_totales = 0

    # 1. Ir a la llave
    while not agente.tiene_llave:
        camino = a_estrella(laberinto, agente.posicion, laberinto.llave)
        if camino is None:
            pudo_mover = mover_aleatoriamente(laberinto, agente, delay)
            if not pudo_mover:
                print("El Agente fue rodeado por los muros, no se puede mover.\nFIN DEL JUEGO.")
                return None
            else:
                print("No se observa ningún camino posible hasta la llave... "
                      "Caminaré un poco por si se mueven los muros...\n")
            pasos_totales += 1 
            continue

        siguiente_paso = camino[1]
        agente.posicion = siguiente_paso
        agente.verificar_llave_y_salida()
        laberinto.mover_muros()
        agente.mostrar_laberinto()
        pasos_totales += 1
        time.sleep(delay)

    # 2. Ir a las salidas, de la más cercana a la más lejana
    salidas_ordenadas = sorted(laberinto.salidas, key=lambda x: heuristica(agente.posicion, x))
    salida_encontrada = False

    for salida in salidas_ordenadas:
        while agente.posicion != salida:
            camino = a_estrella(laberinto, agente.posicion, salida)
            if camino is None:
                pudo_mover = mover_aleatoriamente(laberinto, agente, delay)
                if not pudo_mover:
                    print("El Agente fue rodeado por los muros, no se puede mover.\nFIN DEL JUEGO.")
                    return None
                else:
                    print("No se observa ningún camino posible hasta la siguiente salida... "
                          "Caminaré un poco por si se mueven los muros...\n")
                pasos_totales += 1
                continue

            siguiente_paso = camino[1]
            agente.posicion = siguiente_paso
            if agente.verificar_llave_y_salida():
                salida_encontrada = True
                pasos_totales += 1
                break
            laberinto.mover_muros()
            agente.mostrar_laberinto()
            pasos_totales += 1
            time.sleep(delay)

        if salida_encontrada:
            break

    if not salida_encontrada:
        print("No se encontró la salida real después de probar todas las salidas.")
        return None

    return pasos_totales