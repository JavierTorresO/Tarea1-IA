class Agente:
    
    def __init__(self, laberinto):
        self.laberinto = laberinto  # referencia al laberinto
        self.posicion = laberinto.inicio  # inicia en la posición inicial
        self.camino = [self.posicion]  # para guardar el camino recorrido

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

    # Verificar si es la salida real
    def en_salida(self):
        return self.posicion == self.laberinto.salida_real #si la posicion del agente es la posicion de la salida real devuelve TRUE, si era salida falsa FALSE


    # Visualizar laberinto con el agente dentro y actualizar como se va moviendo
    def mostrar_laberinto(self):
        simbolos = { #representaciones
                    self.laberinto.LIBRES: '⬜',
                    self.laberinto.MUROS: '🟥',
                    self.laberinto.PUNTO_PARTIDA: '🟢',
                    self.laberinto.SALIDAS: '🏁'
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
