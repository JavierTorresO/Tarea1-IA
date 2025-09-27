#Juego del Laberinto con Agente

Este proyecto implementa un juego/laberinto donde un agente debe encontrar la salida sorteando muros y recogiendo llaves. Incluye distintos modos: control manual, búsqueda A* y búsqueda mediante algoritmo genético.

🎮 Elementos del juego
Emoji	Significado
🟩	Casilla libre
⬛	Muro
🚶	Agente
🔑	Llave
🚪	Salida verdadera
🚫	Salida falsa

(Los emojis pueden variar según tu consola, pero la idea es esa).

📂 Archivos principales

prueba_agente.py
Permite jugar manualmente con el agente usando las teclas W, A, S, D para moverte, recoger llaves y probar puertas.

prueba_algoritmo_a.py
Crea un ejemplo donde el agente se mueve automáticamente usando el algoritmo A*.

test_visual_genetico.py
Crea un ejemplo donde el agente se mueve automáticamente usando el algoritmo genético.

Modos Benchmark
Scripts para automatizar y correr varias pruebas de cada algoritmo con un tamaño de laberinto y una probabilidad de muro configurables. Ideales para medir rendimiento y pasos.

⚙️ Instrucciones de uso en Windows

Clona este repositorio o descárgalo:

git clone https://github.com/tuusuario/turepo.git
cd turepo


Instala dependencias (si tienes un requirements.txt):

pip install -r requirements.txt


Ejecuta el modo que quieras:

Modo manual (mover agente)

python prueba_agente.py


Ejemplo con A*

python prueba_algoritmo_a.py


Ejemplo con algoritmo genético

python test_visual_genetico.py


Benchmark A* (varias pruebas)

python benchmark_a.py


Benchmark Genético

python benchmark_genetico.py


En los benchmarks puedes editar dentro del archivo los parámetros prob_muro, tam y repeticiones para ajustar tus pruebas.

📝 Notas

El inicio del agente siempre está en la posición (0,0).

El número de salidas falsas y verdaderas, así como la colocación de la llave, se generan automáticamente.

El delay se puede poner en 0.0 para acelerar las simulaciones en los benchmarks.
