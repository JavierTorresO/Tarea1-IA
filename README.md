# Tarea1-IA
Escape del laberinto mutante


1️⃣ Laberinto y Agente


2️⃣Algoritmo de búsqueda (clásico)

Elegir un algoritmo:

!!Leer tablero kanban, deje algunas opciones posibles 


3️⃣Algoritmo Genético

Aquí el agente intenta evolucionar caminos posibles:
Cada camino se representa como un cromosoma: una secuencia de movimientos (arriba, abajo, izquierda, derecha).
Se define una función de fitness que evalúa qué tan cerca está de la salida real y cuántos muros evita.
Luego aplicas selección, cruce y mutación para generar caminos mejores generación tras generación.

*Ventaja: puede adaptarse a laberintos dinámicos y encontrar soluciones incluso si las rutas cambian.
*Contras: no siempre garantiza la ruta más corta y puede tardar más tiempo en converger.

4️⃣Comparación y Pruebas

Probar varios escenarios:

Laberintos pequeños 
Laberintos grandes 
Baja y alta probabilidad de movimiento de muros.

Medir:

Calidad: ¿llegó a la salida real? ¿camino más corto?
Robustez: ¿funciona cuando cambian los muros?
Tiempo: mide time.perf_counter() antes y después de cada algoritmo.

Poner resultados en una tabla comparativa.
