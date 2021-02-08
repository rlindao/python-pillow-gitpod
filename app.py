from PIL import Image

#read the image
imagen = input("Ingrese nombre de la imagen: ")
im = Image.open("imagenes/" + imagen.upper() + ".png")

#show image
im.show()