import cv2
import numpy as np
import matplotlib.pyplot as plt
from numba import jit, prange
import time

#--- Funcion paralela ( usa todos los nucleos de la CPU) ---
@jit(nopython=True, parallel=True)
def convertir_a_grises_paralelo(img_color):
    alto, ancho, _ = img_color.shape
    img_gris = np.zeros((alto, ancho), dtype=np.uint8)

    for x in prange(alto): # prange permite paralelismo
        for y in prange(ancho):
            b = img_color[x, y, 0]
            g = img_color[x, y, 1]
            r = img_color[x, y, 2]
            gris = 0.114 * b + 0.587 * g + 0.299 * r
            img_gris[x, y] = gris
            
    return img_gris


# ---Codigo principal---
imagen = cv2.imread("imagenes/entrada.jpg")
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta.")
else:
    print("Imagen cargada correctamente")


    # Medir tiempo de ejecucion
    inicio = time.time()
    gris = convertir_a_grises_paralelo(imagen)
    fin = time.time()

    print(f"Tiempo de ejecucion paralelo (CPU): {fin - inicio: .4f} segundos")

    # Mostrar las dos imagenes
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Escala de grises (paralelo CPU)")
    plt.imshow(gris, cmap="gray")
    plt.axis("off")

    plt.show()
