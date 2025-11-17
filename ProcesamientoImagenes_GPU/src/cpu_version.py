import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen
imagen = cv2.imread("imagenes/entrada.jpg")

if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta.")
else:
    print("Imagen cargada correctamente")

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

#Mostrar las dos imagenes
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Escala de grises (CPU)")
plt.imshow(gris, cmap="gray")
plt.axis("off")

import time

inicio = time.time()
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
fin = time.time()
print(f"Tiempo de ejecucion secuencial (CPU): {fin - inicio: .4f} segundos")

plt.show()