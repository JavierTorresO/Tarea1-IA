from laberinto import Laberinto
from agente import Agente

# Crear laberinto y agente
lab = Laberinto(15, prob_muro=0.2)
lab.colocar_inicio(0, 0)
lab.generar_salidas_aleatorias(min_salidas=2, max_salidas=5)
agente = Agente(lab)


# Una prueba rapida interactiva para probar que el agente se puede mover y reconoce la salida real

print("Controla al agente con w(up), s(down), a(left), d(right). q para salir.")
print(f"Salidas generadas: {lab.salidas}")
print(f"Salida real: {lab.salida_real}\n")

while True:
    agente.mostrar_laberinto()

    if agente.en_salida():
        print("¡Llegaste a la salida real! 🎉")
        break

    comando = input("Mover: ").lower()

    if comando == 'q':
        print("Saliendo del juego...")
        break
    elif comando == 'w':
        agente.mover_arriba()
    elif comando == 's':
        agente.mover_abajo()
    elif comando == 'a':
        agente.mover_izquierda()
    elif comando == 'd':
        agente.mover_derecha()
    else:
        print("Comando no válido. Usa w/a/s/d o q para salir.")

print("\nMovimientos realizados:")
agente.mostrar_camino()

# Movimientos=Direcciones
direcciones = []
for i in range(1, len(agente.camino)):
    f0, c0 = agente.camino[i-1]
    f1, c1 = agente.camino[i]
    if f1 < f0:
        direcciones.append("arriba")
    elif f1 > f0:
        direcciones.append("abajo")
    elif c1 < c0:
        direcciones.append("izquierda")
    elif c1 > c0:
        direcciones.append("derecha")

print("Movimientos:", " -> ".join(direcciones))