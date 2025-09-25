import random
import math

class AlgoritmoGenetico:
    def __init__(self, laberinto):
       
       #valores default (ajustar, me los dio la ia XD)
        self.laberinto = laberinto
        self.tam_poblacion = 50          # cuántos individuos por generación
        self.longitud_cromosoma = 1000     # máximo movimientos por cromosoma
        self.prob_mutacion = 0.4         # probabilidad de cambiar un gen (40%)
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
        
        # cambiar los mov existentes
        for i in range(len(cromosoma_mutado)):
            if random.random() < self.prob_mutacion:
                movimientos_disponibles = [m for m in movimientos_posibles if m != cromosoma_mutado[i]]
                
                # si el agente esta cerca de la salida, favorece movimientos hacia la salida
                if i == len(cromosoma_mutado) - 1:  # Último movimiento (cerca de la salida)
                    movimientos_disponibles = ['ARRIBA', 'ABAJO', 'IZQUIERDA', 'DERECHA']
                
                cromosoma_mutado[i] = random.choice(movimientos_disponibles)

        # expansion dinamica: agregar un nuevo movimiento con probabilidad
        if random.random() < 0.2 and len(cromosoma_mutado) < self.longitud_cromosoma:
            cromosoma_mutado.append(random.choice(movimientos_posibles))

        # eliminar un movimiento con probabilidad si el cromosoma es largo
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
    
    def seleccionar_por_torneo(self, torneo_tamaño=3):
        # elegimos al mejor
        torneo = random.sample(self.poblacion, torneo_tamaño)
        mejor_individuo = max(torneo, key=self.calcular_fitness)
        return mejor_individuo


    def elegir_padre(self):
        idx1 = random.randint(0, len(self.poblacion) - 1)
        idx2 = random.randint(0, len(self.poblacion) - 1)

        fitness1 = self.calcular_fitness(self.poblacion[idx1])
        fitness2 = self.calcular_fitness(self.poblacion[idx2])

        return self.poblacion[idx1] if fitness1 > fitness2 else self.poblacion[idx2]

    def cruzar_cromosomas(self, padre1, padre2):
        longitud = min(len(padre1), len(padre2))
        hijo = []
        for i in range(longitud):
            hijo.append(random.choice([padre1[i], padre2[i]])) #selecion entre ambos padres
        return hijo

    
    def evolucionar(self):
        self.crear_poblacion_inicial()
        
        for generacion in range(self.generaciones):
            fitness_actual = [self.calcular_fitness(c) for c in self.poblacion]
            max_fitness = max(fitness_actual)
            
            # actualizar a la mejor version
            if max_fitness > self.mejor_fitness:
                self.mejor_fitness = max_fitness
                self.mejor_cromosoma = self.poblacion[fitness_actual.index(max_fitness)]

            self.fitness_por_generacion.append(max_fitness)
            
            nueva_poblacion = []

            while len(nueva_poblacion) < self.tam_poblacion:
                padre1 = self.seleccionar_por_torneo()
                padre2 = self.seleccionar_por_torneo()

                # cruce y mutacion
                hijo = self.cruzar_cromosomas(padre1, padre2)
                hijo = self.mutar_cromosoma(hijo)

                hijo = self.expandir_cromosoma(hijo)
                
                nueva_poblacion.append(hijo)

            self.poblacion = nueva_poblacion

        return self.mejor_cromosoma, self.mejor_fitness, self.fitness_por_generacion
