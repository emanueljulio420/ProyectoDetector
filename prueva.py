import cv2
import mediapipe as mp
import os

#------- Declaranos el detector -------
nombre = 'Ema_Sintapabocas'
direccion = 'C:/Users/Jorge Andres Julio L/Desktop/ProyectoDetector'
carpeta = direccion + '/' + nombre

if not os.path.exists(carpeta):
    print('carpeta creada')
    os.makedirs(carpeta)

# ------- Detector -------
detector = mp.solutions.face_detection
dibujo = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with detector.FaceDetection(min_detection_confidence=0.75)as rostros:

    while True:
        ret , frame = cap.read()

        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        resutado = rostros.process(rgb)

        if resutado.detections is not None:
            for rostro in resutado.detections:
                dibujo.draw_detection(frame, rostro)

        cv2.imshow('', frame)

        tecla = cv2.waitKey(1)
        if tecla == 112:
            break 

cap.release()
