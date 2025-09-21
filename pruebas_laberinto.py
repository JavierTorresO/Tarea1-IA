from laberinto import Laberinto

lab = Laberinto(15, prob_muro=0.2)
lab.colocar_inicio(0, 0)
lab.generar_salidas_aleatorias(min_salidas=2,max_salidas=5)
lab.colocar_llave()

print("Laberinto inicial:")
lab.mostrar()
print("Cantidad de salidas generadas:", len(lab.salidas))
print("Coordenadas de las salidas:", lab.salidas)
print("Salida real:", lab.salida_real)

lab.mover_muros(prob_mover=0.3)
print("mover muros")
lab.mostrar()
lab.mover_muros(prob_mover=0.3)
print("mover muros otra vez")
lab.mostrar()
lab.mover_muros(prob_mover=0.3)
print("mover muros otra vez")
lab.mostrar()