from laberinto import Laberinto

lab = Laberinto(5)
lab.colocar_inicio(0, 0)   # esquina superior izquierda
lab.colocar_salida(4, 4)   # esquina inferior derecha

for fila in lab.grid:
    print(fila)



