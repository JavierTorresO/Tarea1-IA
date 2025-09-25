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
                
                # si llega a una salida
                if self.laberinto.grid[fila_actual][col_actual] == self.laberinto.SALIDAS:
                    # si es real
                    if (fila_actual, col_actual) == self.laberinto.salida_real:
                        if tiene_llave:
                        
                            return {
                                'posicion_final': (fila_actual, col_actual),
                                'tiene_llave': tiene_llave,
                                'salida_real': True,
                                'movimientos_exitosos': movimientos_exitosos + 10,  # Bonus extra por éxito
                                'camino': posiciones_visitadas
                            }
                        else:
                            # ecnontro la salida pero sin la llave
                            movimientos_exitosos += 5  # bonus por encontrar la salida real
                    else:
                        # intento salida falsa
                        if tiene_llave:
                            movimientos_exitosos -= 2  # Penalización por probar salida falsa con llave
        
        # no llego a la salida real o no tenia la llave
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
        
        # para mutacion 1: cambiar los movimientos existentes
        for i in range(len(cromosoma_mutado)):
            if random.random() < self.prob_mutacion:
                # evitar seleccionar el mismo movimiento
                movimientos_disponibles = [m for m in movimientos_posibles if m != cromosoma_mutado[i]]
                cromosoma_mutado[i] = random.choice(movimientos_disponibles)

        # para mutacion 2: agregar un nuevo movimiento con prob de 20%
        if random.random() < 0.2 and len(cromosoma_mutado) < self.longitud_cromosoma:
            posicion = random.randint(0, len(cromosoma_mutado))
            cromosoma_mutado.insert(posicion, random.choice(movimientos_posibles))

        # para mutacion 3: eliminar un movimiento con prob de 20% (NOTA: probrar estos porcentajes a ver si son validos para el problema)
        if random.random() < 0.2 and len(cromosoma_mutado) > 10: #mantiene un min de 10 movimientos
            posicion = random.randint(0, len(cromosoma_mutado) -  1)
            cromosoma_mutado.pop(posicion)

        return cromosoma_mutado

    def calcular_fitness(self, cromosoma):
        resultado = self.simular_cromosoma(cromosoma)
        fitness = 0

        #bonificacion por los movimientos exitosos
        fitness += resultado['movimientos_exitosos']

        #bonificacion por obtener la llave
        if resultado['tiene_llave']:
            fitness += 500

        #bonificaion por llegar a la salida real
        if resultado['salida_real']:
            fitness += 1000

        #penalizacion por longitud excesiva
        fitness -= len(cromosoma) * 0.1

        #calcular la distancia a objetivos
        pos_final = resultado['posicion_final'] ##revisar

        # si no tiene llave, considerar la distancia a la llave
        if not resultado['tiene_llave']:
            dist_llave = abs(pos_final[0] - self.laberinto.llave[0]) + abs(pos_final[1] - self.laberinto.llave[1])
            fitness -= dist_llave * 2

        #si tiene la llave pero no llego a la salida, considerar la distancia a la salida real
        elif not resultado['salida_real']:
            dist_salida = abs(pos_final[0] - self.laberinto.salida_real[0]) + abs(pos_final[1] - self.laberinto.salida_real[1])
            fitness -= dist_salida * 2

        return fitness

    def elegir_padre(self):
        idx1 = random.randint(0, len(self.poblacion) - 1)
        idx2 = random.randint(0, len(self.poblacion) - 1)

        fitness1 = self.calcular_fitness(self.poblacion[idx1])
        fitness2 = self.calcular_fitness(self.poblacion[idx2])

        return self.poblacion[idx1] if fitness1 > fitness2 else self.poblacion[idx2]

    def cruzar_cromosomas(self, padre1, padre2):
        if random.random() > self.prob_cruce:
            return padre1.copy()
        
        #cruce en un punto
        punto = random.randint(1, min(len(padre1), len(padre2)) - 1)
        hijo = padre1[:punto] + padre2[punto:]
        return hijo
    
    def evolucionar(self):
        #crear poblacion inicial
        self.crear_poblacion_inicial()

        for generacion in range(self.generaciones):
            #evaluar pob actual
            fitness_actual = [self.calcular_fitness(c) for c in self.poblacion]

            #actualizar la mejor solucion encontrada
            max_fitness = max(fitness_actual)
            if max_fitness > self.mejor_fitness:
                self.mejor_fitness = max_fitness
                self.mejor_cromosoma = self.poblacion[fitness_actual.index(max_fitness)]

            self.fitness_por_generacion.append(max_fitness)

            #crar nueva poblacion
            nueva_poblacion = []

            while len(nueva_poblacion) < self.tam_poblacion:
                #selecion
                padre1 = self.elegir_padre()
                padre2 = self.elegir_padre()

                #cruce
                hijo = self.cruzar_cromosomas(padre1, padre2)

                #mutacion
                hijo = self.mutar_cromosoma(hijo)

                nueva_poblacion.append(hijo)

            self.poblacion = nueva_poblacion

        return self.mejor_cromosoma, self.mejor_fitness, self.fitness_por_generacion