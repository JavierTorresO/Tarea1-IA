class Agente:
    
    def __init__(self, laberinto):
        self.laberinto = laberinto        # referencia al laberinto
        self.posicion = laberinto.inicio  # inicia en la posición inicial
        self.camino = [self.posicion]     # para guardar el camino recorrido
        self.tiene_llave = False          # para saber si se recogio la llave o no

    # Métodos de movimiento

    def mover_arriba(self):
        f, c = self.posicion # tomo posicion actual
        if f > 0 and self.laberinto.grid[f-1][c] != self.laberinto.MUROS: # se ve que este dentro del laberinto y que la posicion de arriba no sea un muro
            self.posicion = (f-1, c) #mueve al agente
            self.camino.append(self.posicion) # guarda el movimiento
            self.laberinto.mover_muros()  # despues de moverse hace el posible movimiento aleatorio de los muros

    def mover_abajo(self):
        f, c = self.posicion 
        if f < self.laberinto.n - 1 and self.laberinto.grid[f+1][c] != self.laberinto.MUROS: #que la posicion de abajo no sea muro
            self.posicion = (f+1, c) 
            self.camino.append(self.posicion)
            self.laberinto.mover_muros()

    def mover_izquierda(self):
        f, c = self.posicion 
        if c > 0 and self.laberinto.grid[f][c-1] != self.laberinto.MUROS: #que la posicion de la izq no sea muro
            self.posicion = (f, c-1)
            self.camino.append(self.posicion)
            self.laberinto.mover_muros()

    def mover_derecha(self):
        f, c = self.posicion 
        if c < self.laberinto.n - 1 and self.laberinto.grid[f][c+1] != self.laberinto.MUROS: #que la posicion de la der no sea muro
            self.posicion = (f, c+1)
            self.camino.append(self.posicion)
            self.laberinto.mover_muros()

    # NUEVO: Manejar tema de la llave y comprobación de salidas

    def verificar_llave_y_salida(self):
        f, c = self.posicion
        celda = self.laberinto.grid[f][c]

        # recoger la llave si está en la celda
        if celda == self.laberinto.LLAVE:
            self.tiene_llave = True                            # marca que el agente tiene la llave
            self.laberinto.grid[f][c] = self.laberinto.LIBRES  # borramos la llave del mapa
            print("¡Llave recogida! 🔑")

        # intentar entrar a una salida
        if celda == self.laberinto.SALIDAS:
            if not self.tiene_llave:  # si no se recogió la llave
                print("Necesitas la llave para entrar a una salida 🔑")
                return False
            elif (f, c) != self.laberinto.salida_real:  # la salida es falsa
                print("Ups, la salida era falsa. Sigue buscando...")
                return False
            else:  # recogió la llave y llegó a la salida real
                print("¡Llegaste a la salida real! 🎉")
                return True

        return False  # no es salida


    # Visualizar laberinto con el agente dentro y actualizar como se va moviendo
    def mostrar_laberinto(self):
        simbolos = { #representaciones
                    self.laberinto.LIBRES: '⬜',
                    self.laberinto.MUROS: '🟥',
                    self.laberinto.PUNTO_PARTIDA: '🟢',
                    self.laberinto.SALIDAS: '🚪',   
                    self.laberinto.LLAVE: '🔑'
                    }
        for f in range(self.laberinto.n):
            fila = ""
            for c in range(self.laberinto.n):
                if (f, c) == self.posicion: # visualizar agente con la posicion actual
                    fila += "🤖 " #un robot es el agente
                else:
                    fila += simbolos[self.laberinto.grid[f][c]] + " "
            print(fila)
        print()


    # Guardar camino recorrido
    def mostrar_camino(self):
        print("Camino recorrido:", self.camino)
