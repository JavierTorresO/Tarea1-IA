# Juego: Escapa del laberinto mutante

Se mplementó un laberinto donde un agente inteligente debe encontrar la salida sorteando muros y recogiendo una llave. 
Incluye distintos modos: control manual, búsqueda A* y búsqueda mediante algoritmo genético.  

## 🎮 Elementos del juego  

| Emoji | Significado |
|-------|-------------|
| ⬜ | Casilla libre |
| 🟥 | Muro |
| 🤖 | Agente |
| 🔑 | Llave |
| 🚪 | Salidas |

*(a lo mejor los emojis varian o no se ven según la consola, pero la idea es esa).*  

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
   git clone https://github.com/tuusuario/turepo.git
   cd turepo
2. **Ejecuta el modo que quieras:**  

   ```bash
   python prueba_agente.py
   python prueba_algoritmo_a.py
   python test_visual_genetico.py
   python benchmark_a.py
   python benchmark_genetico.py
3. **Parámetros configurables en benchmarks:**  

   Edita dentro del archivo los valores de "prob_muro"(densidad de muros que se generan), "tam"(tamaño del laberinto) y "repeticiones" para ajustar las pruebas que se quieran hacer.
   El delay está en 0.0 por defecto para que fueran más rapidas las simulaciones.

4. **Otros parámetros configurables:**

   Aunque en nuestras pruebas estos parametros se mantuvieron en los valores por defecto, si se quiere se pueden modificar dentro del codigo:
   
    Punto de inicio del agente en celda (0, 0). ->

    Número mínimo y máximo de salidas generadas en el laberinto (2 y 5). ->
    
    Probabilidad de que se muevan los muros en el laberinto está en 0.2. ->
    
    Un radio seguro en la generación inicial del laberinto fue 1 (garantiza un área libre alrededor del inicio). ->
    
    La generación de llaves y salidas siempre fue aleatoria. 
   
