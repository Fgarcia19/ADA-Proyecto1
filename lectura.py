import numpy as np
from PIL import Image

def leer_imagen(name):
    img = Image.open(name)
    img = img.convert('1)
    arr = np.asarray(img)
    print(arr)
    
if __name__ == "__main__":
    leer_imagen('prueba.jpeg')
