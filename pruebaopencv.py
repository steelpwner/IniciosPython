import cv2, time

# 1. Creación de un objeto. El código de la cámara del computador es 0
video=cv2.VideoCapture(0)

# 3. Crear un objeto ventana
check, frame= video.read()

print (check)
print (frame)

# 4. Mostrar el frame
cv2.imshow("Captura", frame)
# 2. Apagar la cámara
video.release()

