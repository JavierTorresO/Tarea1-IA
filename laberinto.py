import random

class Laberinto:
    LIBRE = 0 
    MURO = 1
    PARTIDA = 2
    SALIDA = 3

    def __init__(self, n):
        self.n = n
        self.grid = [[self.LIBRE for _ in range(n)] for _ in range(n)]

    def colocar_inicio(self, fila, col):
        """Indica la posición inicial del agente"""
        if 0 <= fila < self.n and 0 <= col < self.n:
            self.grid[fila][col] = self.PARTIDA
        else:
            raise ValueError("Coordenadas fuera del laberinto")

    def colocar_salida(self, fila, col):
        """Indica la salida"""
        if 0 <= fila < self.n and 0 <= col < self.n:
            self.grid[fila][col] = self.SALIDA
        else:
            raise ValueError("Coordenadas fuera del laberinto")

