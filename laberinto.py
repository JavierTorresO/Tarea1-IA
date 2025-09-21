import random

class Laberinto:
    LIBRES = 0          # casillas libres, por aqui se puede mover el agente
    MUROS = 1           # muros
    PUNTO_PARTIDA = 2   # donde inicia, solo un punto de partida en todo el laberinto
    SALIDAS = 3         # salidas (falsas y la real)
    LLAVE = 4           # llave que recoger para poder abrir la salida

    def __init__(self, n, prob_muro=0.0, radio_seguro=1):
        """
        Crea un laberinto n x n.
        - n: tamaño del laberinto
        - prob_muro: probabilidad (0-1) de poner muros aleatorios.
        - radio_seguro: distancia mínima alrededor de inicio/salidas para no colocar muros, es para no encerrar el punto de partida (evitar bloqueo y no poder salir) y las salidas (evitar una salida encerrada y no poder entrar en ella)
        """
        self.n = n
        self.grid = [[self.LIBRES for _ in range(n)] for _ in range(n)]
        self.inicio = None
        self.salidas = []
        self.salida_real = None
        self.llave = None

        if prob_muro > 0:
            self.generar_muros_aleatorios(prob_muro, radio_seguro)

    # Métodos de colocación

    def colocar_inicio(self, fila, col): # Coloca el punto de partida en la coordenada dada
        if 0 <= fila < self.n and 0 <= col < self.n:
            self.grid[fila][col] = self.PUNTO_PARTIDA
            self.inicio = (fila, col)
        else:
            raise ValueError("Coordenadas fuera del laberinto")

    def generar_salidas_aleatorias(self, min_salidas=2, max_salidas=5): # Genera las salidas aleatoriamente (min es 2 para que como minimo haya una real y una falsa) (max es 5 para tampoco saturar el laberinto)
        if self.inicio is None:
            raise ValueError("Debe colocar primero el inicio")

        k = random.randint(min_salidas, max_salidas) # elige cuantas posibles salidas
        self.salidas = [] # para guardas las coords de las salidas

        while len(self.salidas) < k:
            # genera coordenadas random...
            f = random.randint(0, self.n-1)
            c = random.randint(0, self.n-1)
            if (f, c) not in self.salidas and (f, c) != self.inicio: 
                self.salidas.append((f, c)) #si no se guardo antes y no es el punto de partida la guarda en la lista

        #elige aleatoriamente una de las salidas como la real
        self.salida_real = random.choice(self.salidas)

        #las coloca en el laberinto
        for f, c in self.salidas:
            self.grid[f][c] = self.SALIDAS

    def colocar_muro(self, fila, col): # Coloca muro manualmente en la coordenada dada 
        if 0 <= fila < self.n and 0 <= col < self.n:
            if self.grid[fila][col] not in (self.PUNTO_PARTIDA, self.SALIDAS):
                self.grid[fila][col] = self.MUROS
        else:
            raise ValueError("Coordenadas fuera del laberinto")

    # Métodos aleatorios/dinámicos

    def generar_muros_aleatorios(self, probabilidad, radio_seguro=1): # Llena el laberinto de muros aleatorios
        #recorrer filas y columnas...
        for fila in range(self.n):
            for col in range(self.n):
                if self.grid[fila][col] != self.LIBRES:
                    continue  # no sobreescribir inicio o salidas

                # respetando el radio seguro...        
                seguro = False
                if self.inicio:
                    seguro |= abs(fila - self.inicio[0]) <= radio_seguro and abs(col - self.inicio[1]) <= radio_seguro #que no este muy cerca del punto de partida...
                for f, c in self.salidas:
                    seguro |= abs(fila - f) <= radio_seguro and abs(col - c) <= radio_seguro #que no este muy cerca de las salidas..

                # si no está en la zona segura entonces coloca el muro
                if not seguro and random.random() < probabilidad:
                    self.grid[fila][col] = self.MUROS

    def mover_muros(self, prob_mover=0.2): # Movimiento de muros, se mueve a celdas vecinas libres
        movimientos = [(-1,0),(1,0),(0,-1),(0,1)]  # posibles direcciones: arriba, abajo, izquierda, derecha
        # lista para guardar todos los muros que hay
        muros = [(f, c) for f in range(self.n) for c in range(self.n) if self.grid[f][c] == self.MUROS]

        # recorre todos los muros...
        for f, c in muros:
            if random.random() < prob_mover: #decide aleatoriamente si se va a mover o no
                random.shuffle(movimientos) # se mezclan los posibles movimientos, para que los muros no se muevan siempre en el mismo orden arriba->abajo->izquierda->derecha
                for df, dc in movimientos: # intenta mover el muro a cada direccion...
                    nf, nc = f+df, c+dc # calcula la nueva fila y la nueva columna
                    if 0 <= nf < self.n and 0 <= nc < self.n and self.grid[nf][nc] == self.LIBRES: # la nueva posicion debe estar dentro del laberinto y tiene que estar libre
                        if (nf, nc) == self.inicio or (nf, nc) in self.salidas: # no puede ser el punto partida ni una salida...
                            continue
                        # se mueve el muro a la nueva posicion newfila,newcolumna
                        self.grid[nf][nc] = self.MUROS
                        # queda libre la posicion donde estaba el muro anteriormente
                        self.grid[f][c] = self.LIBRES
                        break

    # IDEA EXTRA: poner una llave en el mapa, se debe recoger antes de probar las salidas        
                 
    def colocar_llave(self):
        encontrado = False
        while not encontrado:
            f = random.randint(0, self.n - 1)
            c = random.randint(0, self.n - 1)
            if self.grid[f][c] == self.LIBRES and (f, c) != self.inicio and (f, c) not in self.salidas:
                self.grid[f][c] = self.LLAVE
                self.llave = (f, c)
                encontrado = True


    # Visualización del laberinto

    def mostrar(self):
        simbolos = {self.LIBRES: '⬜', self.MUROS: '🟥',
                    self.PUNTO_PARTIDA: '🟢', self.SALIDAS: '🚪',
                    self.LLAVE: '🔑'}
        for fila in self.grid:
            print(' '.join(simbolos[val] for val in fila))
        print()
