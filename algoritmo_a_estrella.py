from queue import PriorityQueue

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

def a_estrella_con_llave(laberinto):
    #Devuelve el camino inicio→llave→salida_real, o None si no hay camino
    
    camino_a_llave = a_estrella(laberinto, laberinto.inicio, laberinto.llave)
    if camino_a_llave is None:
        return None

    camino_a_salida = a_estrella(laberinto, laberinto.llave, laberinto.salida_real)
    if camino_a_salida is None:
        return None

    return camino_a_llave + camino_a_salida[1:]