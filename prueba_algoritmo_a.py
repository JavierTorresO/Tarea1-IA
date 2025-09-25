from laberinto import Laberinto
from agente import Agente
from algoritmo_a_estrella import a_estrella_con_llave  
import time

# Crear laberinto y agente
lab = Laberinto(12, prob_muro=0.4)
lab.colocar_inicio(0, 0)
lab.generar_salidas_aleatorias(min_salidas=2, max_salidas=5)
lab.colocar_llave()  
agente = Agente(lab)

print("Laberinto inicial:")
agente.mostrar_laberinto()

inicio=time.time()
pasos = a_estrella_con_llave(lab, agente, delay=0.5)
fin=time.time()
if pasos is not None:
    print(f"\nJuego completado en {pasos} pasos.")
else:
    print("\nEl agente no pudo completar el laberinto (bloqueado).")

print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
# si está demorando mucho cortar la terminal a la fuerza: ctrl+c