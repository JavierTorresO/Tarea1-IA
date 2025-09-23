import random
import math

class AlgoritmoGenetico:
    def __init__(self, laberinto):
       
       #valores default (ajustar, me los dio la ia XD)
        self.laberinto = laberinto
        self.tam_poblacion = 30          # cuántos individuos por generación
        self.longitud_cromosoma = 50     # máximo movimientos por cromosoma
        self.prob_mutacion = 0.1         # probabilidad de cambiar un gen (10%)
        self.prob_cruce = 0.7            # probabilidad de cruce entre padres (70%)
        self.generaciones = 50           # cuántas generaciones evolucionar
        
        self.poblacion = []
        self.mejor_cromosoma = None
        self.mejor_fitness = 0
        self.fitness_por_generacion = []

    def crear_cromosoma_aleatorio(self):
        movimientos_posibles = ['ARRIBA', 'ABAJO', 'IZQUIERDA', 'DERECHA']
        longitud = random.randint(10, self.longitud_cromosoma) #longitud random entre 10 y la longitud max
        
        cromosoma = []
        for i in range(longitud):
            movimiento = random.choice(movimientos_posibles)
            cromosoma.append(movimiento)
        
        return cromosoma

    def crear_poblacion_inicial(self):
        self.poblacion = []
        for i in range(self.tam_poblacion):
            cromosoma = self.crear_cromosoma_aleatorio()
            self.poblacion.append(cromosoma)
        

    def simular_cromosoma(self, cromosoma): #somular movimientos del cromosoma en el laberinto
        fila_actual = self.laberinto.inicio[0]
        col_actual = self.laberinto.inicio[1]
        # rastrear progreso del cromosoma
        tiene_llave = False
        movimientos_exitosos = 0
        posiciones_visitadas = [(fila_actual, col_actual)]
        for movimiento in cromosoma:
            nueva_fila = fila_actual
            nueva_col = col_actual
            # Calcular nueva pos
            if movimiento == 'ARRIBA':
                nueva_fila = fila_actual - 1
            elif movimiento == 'ABAJO':
                nueva_fila = fila_actual + 1
            elif movimiento == 'IZQUIERDA':
                nueva_col = col_actual - 1
            elif movimiento == 'DERECHA':
                nueva_col = col_actual + 1
            
            movimiento_valido = True
            
            #si esta fuera del laberinto
            if nueva_fila < 0 or nueva_fila >= self.laberinto.n:
                movimiento_valido = False
            if nueva_col < 0 or nueva_col >= self.laberinto.n:
                movimiento_valido = False
            
            # si es muro
            if movimiento_valido:
                if self.laberinto.grid[nueva_fila][nueva_col] == self.laberinto.MUROS:
                    movimiento_valido = False
            
            #actualizar pos si el movimiento es valido
            if movimiento_valido:
                fila_actual = nueva_fila
                col_actual = nueva_col
                movimientos_exitosos += 1
                posiciones_visitadas.append((fila_actual, col_actual))
                
                #si recogio la llave
                if self.laberinto.grid[fila_actual][col_actual] == self.laberinto.LLAVE:
                    tiene_llave = True
                
                # si llega a la salida
                if self.laberinto.grid[fila_actual][col_actual] == self.laberinto.SALIDAS:
                    # verificar que es el objetivo salida real y tiene llave
                    if (fila_actual, col_actual) == self.laberinto.salida_real and tiene_llave:
                        return {
                            'posicion_final': (fila_actual, col_actual),
                            'tiene_llave': tiene_llave,
                            'salida_real': True,
                            'movimientos_exitosos': movimientos_exitosos,
                            'camino': posiciones_visitadas
                        }
        
        # si no llega a la salida real
        return {
            'posicion_final': (fila_actual, col_actual),
            'tiene_llave': tiene_llave,
            'salida_real': False,
            'movimientos_exitosos': movimientos_exitosos,
            'camino': posiciones_visitadas
        }

#revisar
    def mutar_cromosoma(self, cromosoma):
        cromosoma_mutado = cromosoma.copy()
        movimientos_posibles = ['ARRIBA', 'ABAJO', 'IZQUIERDA', 'DERECHA']
        
        # Revisar cada gen del cromosoma
        for i in range(len(cromosoma_mutado)):
            # si se puede mutar ese gen
            if random.random() < self.prob_mutacion:
                cromosoma_mutado[i] = random.choice(movimientos_posibles)
        return cromosoma_mutado

    #def calcular_fitness(self, cromosoma):

    #def elegir_padre(self):
        

    #def cruzar_cromosomas(self, padre1, padre2):
