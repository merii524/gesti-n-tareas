Procesamiento de Imágenes y Game of Life con GPU
Proyecto para la materia de Programación Concurrente

Este proyecto implementa distintas optimizaciones para ejecutar el Juego de la Vida (Conway’s Game of Life) y procesamiento de imágenes, utilizando:

CPU (versión estándar en Python)

CPU optimizada con Numba (parallel=True)

GPU con Numba CUDA

El objetivo principal es comparar el rendimiento entre CPU y GPU, midiendo tiempos de ejecución sobre el mismo input.

Características del Proyecto
 Versión CPU (pura)

Implementación base del Game of Life / procesamiento de imágenes usando bucles tradicionales en Python.

 Versión CPU optimizada con Numba

Se utiliza:

@jit(nopython=True)


y

@jit(nopython=True, parallel=True)


para paralelizar y optimizar la ejecución en CPU.

Incluye medición de tiempos:

start = time.time()
...
end = time.time()
print("Tiempo CPU paralela:", end - start)

 Versión GPU con CUDA (Numba)

Implementación del kernel GPU usando:

@cuda.jit
def actualizar_gpu(...):


Configuración de hilos y bloques:

threadsperblock = (16, 16)
blockspergrid = (ceil(n/16), ceil(m/16))


Copia de memoria CPU → GPU y GPU → CPU.

Comparación de Rendimiento

El programa imprime los tiempos:

Tiempo CPU normal

Tiempo CPU paralelizado

Tiempo GPU CUDA

Speedup general

Ejemplo esperado:

Tiempo CPU: 4.8s
Tiempo CPU paralela: 1.9s
Tiempo GPU: 0.15s
Speedup GPU respecto CPU: x32


(Valores de ejemplo)

 Archivos del Proyecto

game_of_life.py → versión CPU

game_of_life_numba.py → versión CPU optimizada

game_of_life_gpu.py → versión CUDA

utils.py → funciones auxiliares

README.md → este documento

imagenes/entrada.jpg → imagen utilizada

resultados/ → tiempos guardados

Requisitos

Python 3.10+

Numba

Numpy

Matplotlib

CUDA Toolkit (si se usa GPU)

Drivers NVIDIA compatibles

 Alumna

Jesica Lencina
Universidad Nacional Guillermo Brown (UNaB)
Materia: Programación Concurrente
Docente: (Agustin Ambrocio)

