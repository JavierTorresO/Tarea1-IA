import time
from laberinto import Laberinto
from agente import Agente
from algoritmo_a_estrella import a_estrella_con_llave  

# Crear laberinto y agente
lab = Laberinto(10, prob_muro=0.2)
lab.colocar_inicio(0, 0)
lab.generar_salidas_aleatorias(min_salidas=2, max_salidas=5)
lab.colocar_llave()  
agente = Agente(lab)

print("Laberinto inicial:")
agente.mostrar_laberinto()

# Ejecutar A* considerando la llave
camino = a_estrella_con_llave(lab)  

if camino:
    print("Camino calculado por A* con llave:")
    print(camino)
    
    # Simular el movimiento del agente paso a paso
    for pos in camino:
        agente.posicion = pos
        agente.verificar_llave_y_salida()  
        agente.mostrar_laberinto()
        time.sleep(0.5)  # retardo para hacer el movimiento del agente mas visual
else:
    print("No se encontró un camino válido al objetivo.")

