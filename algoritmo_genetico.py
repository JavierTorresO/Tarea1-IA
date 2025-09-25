import random
import math

class AlgoritmoGenetico:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        # param del algoritmo
        self.tam_poblacion = 50          # tamaño de la poblacion
        self.longitud_cromosoma = 100    # longitud maxima de cada cromosoma
        self.prob_mutacion = 0.3         # probabilidad de mutacion (30%)
        self.prob_cruce = 0.8            # probabilidad de cruce (80%)
        self.generaciones = 100          # numero maximo de generaciones
        self.tam_torneo = 3              # tamaño del torneo para seleccion
        
        self.poblacion = []
        self.mejor_cromosoma = None
        self.mejor_fitness = float('-inf')
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
        

    def simular_cromosoma(self, cromosoma):
        fila_actual = self.laberinto.inicio[0]
        col_actual = self.laberinto.inicio[1]
        
        tiene_llave = False
        movimientos_exitosos = 0
        posiciones_visitadas = [(fila_actual, col_actual)]
        
        for movimiento in cromosoma:
            nueva_fila, nueva_col = fila_actual, col_actual
            if movimiento == 'ARRIBA':
                nueva_fila -= 1
            elif movimiento == 'ABAJO':
                nueva_fila += 1
            elif movimiento == 'IZQUIERDA':
                nueva_col -= 1
            elif movimiento == 'DERECHA':
                nueva_col += 1

            # verificar si es valido
            movimiento_valido = True
            if nueva_fila < 0 or nueva_fila >= self.laberinto.n or nueva_col < 0 or nueva_col >= self.laberinto.n:
                movimiento_valido = False
            if movimiento_valido:
                if self.laberinto.grid[nueva_fila][nueva_col] == self.laberinto.MUROS:
                    movimiento_valido = False

            if movimiento_valido:
                fila_actual = nueva_fila
                col_actual = nueva_col
                movimientos_exitosos += 1
                posiciones_visitadas.append((fila_actual, col_actual))

                # verificar si recogio la llave
                if self.laberinto.grid[fila_actual][col_actual] == self.laberinto.LLAVE:
                    tiene_llave = True

                # ver si llega a una salida
                if self.laberinto.grid[fila_actual][col_actual] == self.laberinto.SALIDAS:
                    if (fila_actual, col_actual) == self.laberinto.salida_real and tiene_llave:
                        return {
                            'posicion_final': (fila_actual, col_actual),
                            'tiene_llave': tiene_llave,
                            'salida_real': True,
                            'movimientos_exitosos': movimientos_exitosos + 10,  #bonus
                            'camino': posiciones_visitadas
                        }
                    else:
                        if tiene_llave:
                            movimientos_exitosos -= 2  #penalizacion
            
        # si es que no llego a la salida real o no tenia la llave
        return {
            'posicion_final': (fila_actual, col_actual),
            'tiene_llave': tiene_llave,
            'salida_real': False,
            'movimientos_exitosos': movimientos_exitosos,
            'camino': posiciones_visitadas
        }


    def mutar_cromosoma(self, cromosoma):
        cromosoma_mutado = cromosoma.copy()
        movimientos_posibles = ['ARRIBA', 'ABAJO', 'IZQUIERDA', 'DERECHA']
        
        # cambiar movimientos existentes
        for i in range(len(cromosoma_mutado)):
            if random.random() < self.prob_mutacion:
                movimientos_disponibles = [m for m in movimientos_posibles if m != cromosoma_mutado[i]]
                
                # si el agente esta cerca, se le ayuda para la salida
                if i == len(cromosoma_mutado) - 1:
                    movimientos_disponibles = ['ARRIBA', 'ABAJO', 'IZQUIERDA', 'DERECHA']
                
                cromosoma_mutado[i] = random.choice(movimientos_disponibles)

        if random.random() < 0.2 and len(cromosoma_mutado) < self.longitud_cromosoma:
            cromosoma_mutado.append(random.choice(movimientos_posibles))

        if random.random() < 0.2 and len(cromosoma_mutado) > 10:
            cromosoma_mutado.pop(random.randint(0, len(cromosoma_mutado) - 1))

        return cromosoma_mutado

    
    def expandir_cromosoma(self, cromosoma):
        # si el cromosoma no ha encontrado la salida despues de unos intentos, se expande
        if len(cromosoma) < self.longitud_cromosoma:
            movimientos_posibles = ['ARRIBA', 'ABAJO', 'IZQUIERDA', 'DERECHA']
            cromosoma.append(random.choice(movimientos_posibles))
        return cromosoma


    def calcular_fitness(self, cromosoma):
        resultado = self.simular_cromosoma(cromosoma)
        fitness = 0

        # bonificacion para mov exitosos
        fitness += resultado['movimientos_exitosos']

        # bonificacion por obtener la llave
        if resultado['tiene_llave']:
            fitness += 500

        # bonificacion por llegar a la salida real
        if resultado['salida_real']:
            fitness += 1000

        # penalizacion por longitud excesiva
        fitness -= len(cromosoma) * 0.1

        # calcular la distancia a la salida real
        pos_final = resultado['posicion_final']
        dist_salida = abs(pos_final[0] - self.laberinto.salida_real[0]) + abs(pos_final[1] - self.laberinto.salida_real[1])
        fitness -= dist_salida * 2 

        # penalizacion por no tener la llave
        if not resultado['tiene_llave']:
            dist_llave = abs(pos_final[0] - self.laberinto.llave[0]) + abs(pos_final[1] - self.laberinto.llave[1])
            fitness -= dist_llave * 2

        return fitness

    
    def seleccionar_por_torneo(self, torneo_tamaño=3):
        # elegimos al mejor
        torneo = random.sample(self.poblacion, torneo_tamaño)
        mejor_individuo = max(torneo, key=self.calcular_fitness)
        return mejor_individuo


    def seleccionar_padres(self):
        # seleccion por torneo
        def torneo():
            candidatos = random.sample(range(len(self.poblacion)), self.tam_torneo)
            mejor = max(candidatos, key=lambda i: self.calcular_fitness(self.poblacion[i]))
            return self.poblacion[mejor]
        
        padre1 = torneo()
        padre2 = torneo()
        return padre1, padre2

    def cruzar_cromosomas(self, padre1, padre2):
        longitud = min(len(padre1), len(padre2))
        punto = random.randint(1, longitud - 1)  #elegir un punto de cruce

        hijo = padre1[:punto] + padre2[punto:]
        return hijo


    
    def evolucionar(self):
        self.crear_poblacion_inicial()
        generaciones_sin_mejora = 0
        
        for gen in range(self.generaciones):
            fitness_actual = [self.calcular_fitness(c) for c in self.poblacion]
            
            # encontrar los mejores para elitismo
            indices_ordenados = sorted(range(len(self.poblacion)), 
                                    key=lambda i: fitness_actual[i],
                                    reverse=True)
            mejores = [self.poblacion[i].copy() for i in indices_ordenados[:2]]
            
            # actualizar al mejor global
            max_fitness = fitness_actual[indices_ordenados[0]]
            if max_fitness > self.mejor_fitness:
                self.mejor_fitness = max_fitness
                self.mejor_cromosoma = self.poblacion[indices_ordenados[0]].copy()
                generaciones_sin_mejora = 0
            else:
                generaciones_sin_mejora += 1
            
            self.fitness_por_generacion.append(max_fitness)
            
            # criterio para detenerse
            if generaciones_sin_mejora > 20:
                break
                
            # crear nueva población con elitismo
            nueva_poblacion = mejores
            
            # generar el resto de la poblacion
            while len(nueva_poblacion) < self.tam_poblacion:
                padre1, padre2 = self.seleccionar_padres()
                hijo = self.cruzar_cromosomas(padre1, padre2)
                hijo = self.mutar_cromosoma(hijo)
                nueva_poblacion.append(hijo)
            
            self.poblacion = nueva_poblacion
        
        return self.mejor_cromosoma, self.mejor_fitness, self.fitness_por_generacion