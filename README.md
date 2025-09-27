# Juego: Escapa del laberinto mutante

Se mplementó un laberinto donde un agente inteligente debe encontrar la salida sorteando muros y recogiendo una llave. 
Incluye distintos modos: control manual, búsqueda A* y búsqueda mediante algoritmo genético.  

## Elementos del juego  

| Emoji | Significado |
|-------|-------------|
| ⬜ | Casillas libres |
| 🟥 | Muros |
| 🤖 | Agente |
| 🔑 | Llave |
| 🚪 | Salidas |

*(a lo mejor los emojis se ven algo distintos o no se ven según la consola, pero la idea es la de esta tabla).*  

## 📂 Archivos principales  

- **`prueba_agente.py`**  
  Para jugar manualmente con el agente usando las teclas `W`, `A`, `S`, `D` para moverte, recoger llaves y probar puertas.  

- **`prueba_algoritmo_a.py`**  
  Crea un ejemplo donde el agente se mueve automáticamente usando el algoritmo A*.  

- **`test_visual_genetico.py`**  
  Crea un ejemplo donde el agente se mueve automáticamente usando el algoritmo genético.  

- **Modos Benchmark**  
  Scripts para automatizar y correr varias pruebas de cada algoritmo con un tamaño de laberinto y una probabilidad de muro configurables.  
  Ideales para medir rendimiento y pasos.  

## Instrucciones (Windows)  

1. **Clonar el repositorio o descárgalo:**  

   ```bash
   git clone https://github.com/JavierTorresO/Tarea1-IA.git
   cd Tarea1-IA
2. **Ejecuta el modo que quieras:**  

   ```bash
   python prueba_agente.py
   python prueba_algoritmo_a.py
   python test_visual_genetico.py
   python benchmark_a_estrella.py
   python benchmark_a_genetico.py
3. **Parámetros configurables en benchmarks:**  

   Edita dentro del archivo los valores de "prob_muro"(densidad de muros que se generan), "tam"(tamaño del laberinto) y "repeticiones" para ajustar las pruebas que se quieran hacer.
   El delay está en 0.0 por defecto para que fueran más rapidas las simulaciones.

4. **Otros parámetros configurables:**

   Aunque en nuestras pruebas estos parametros se mantuvieron en los valores por defecto, si se quiere se pueden modificar dentro del codigo:
   
    -*Punto de inicio del agente en celda (0, 0).* -> según el modo que se eligió hay que identificar el comando "lab.colocar_inicio(0, 0)" y poner otras coordenadas

    -*Número mínimo y máximo de salidas generadas en el laberinto (2 y 5).* -> según el modo que se eligió hay que identificar el comando "lab.generar_salidas_aleatorias(min_salidas=2, max_salidas=5)" y poner otros valores para esa prueba


    -*Probabilidad de que se muevan los muros en el laberinto está en 0.2.* -> en el archivo "laberinto.py" ir a la función "mover_muros(self, prob_mover)" y cambiar el valor de 'prob_mover'

    -*Radio seguro en la generación inicial del laberinto fue 1 (garantiza un área libre alrededor del inicio).* ->en el archivo "laberinto.py" ir a la función "generar_muros_aleatorios(self,probabilidad,radio_seguro)" y cambiar el valor de 'radio_seguro'
       
    -*La generación de llaves y salidas siempre fue aleatoria.*
   
