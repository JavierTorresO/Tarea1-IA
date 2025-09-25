from laberinto import Laberinto
from agente import Agente
from algoritmo_a_estrella import a_estrella_con_llave  

# Crear laberinto y agente
lab = Laberinto(10, prob_muro=0.5)
lab.colocar_inicio(0, 0)
lab.generar_salidas_aleatorias(min_salidas=2, max_salidas=5)
lab.colocar_llave()  
agente = Agente(lab)

print("Laberinto inicial:")
agente.mostrar_laberinto()

# Ejecutar A* considerando la llave y las salidas falsas
a_estrella_con_llave(lab, agente, delay=0.5)

# si está demorando mucho cortar la terminal a la fuerza: ctrl+c