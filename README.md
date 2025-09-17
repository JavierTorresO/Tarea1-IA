# Tarea1-IA
Escape del laberinto mutante


1ero Definir y programar la representación del laberinto

Estructura de datos:
Usa una matriz N x N 

0 = celda libre

1 = muro

S = posición inicial del agente

E = salida(s)

Muros móviles:

Crear una lista de coordenadas de muros móviles.

En cada turno, para cada muro móvil, con probabilidad p mueve el muro a una celda adyacente libre o lo deja donde está.

Para simular el dinamismo del laberinto.

Salidas:

Colocar k salidas posibles en coordenadas distintas.

Marcar una como la “real”.

2do Algoritmo de búsqueda (clásico)

Elegir un algoritmo:

BFS (Breadth-First Search) → encuentra el camino más corto en un grafo no ponderado.

A* (si quieres algo más eficiente) → requiere heurística (por ejemplo, distancia Manhattan a la salida real).

Adaptación al entorno dinámico:

Después de cada “turno” o movimiento del agente, actualiza el laberinto (muros móviles) y vuelve a planificar desde la nueva posición.

Esto es parecido a un “replanning” cada paso.

3️ro Algoritmo Genético

Codificación de cromosomas:

Un cromosoma = secuencia de movimientos (ej. ["U", "U", "R", "D"]).

La longitud máxima puede ser un parámetro (por ejemplo, 2*N o 3*N pasos).

Fitness:

Inverso de la distancia Manhattan desde la última celda del camino a la salida real.

Penaliza chocar con muros (fitness muy bajo).

Recompensa llegar efectivamente a la salida real (fitness máximo).

Población inicial:

Genera caminos aleatorios de longitud fija.

Selección:

Por torneo o ruleta.

Crossover:

Une dos cromosomas en un punto aleatorio.

Mutación:

Con probabilidad pequeña, cambia un movimiento aleatorio en el cromosoma.

Ejecución:

Iterar generaciones hasta encontrar un camino que llegue a la salida real o hasta un número máximo de generaciones.

4️to Comparación y Pruebas

Probar varios escenarios:

Laberintos pequeños (5x5, 10x10).

Laberintos grandes (20x20, 30x30).

Baja y alta probabilidad de movimiento de muros.

Medir:

Calidad: ¿llegó a la salida real? ¿camino más corto?

Robustez: ¿funciona cuando cambian los muros?

Tiempo: mide time.perf_counter() antes y después de cada algoritmo.

Poner resultados en una tabla comparativa.
