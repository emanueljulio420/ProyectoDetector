<<<<<<< HEAD
from PySide2.QtWidgets import * 
from PySide2 import QtCore, QtGui 
from PySide2.QtGui import * 
from PySide2.QtCore import * 
import sys 
  
  
class Window(QMainWindow): 
  
    def __init__(self): 
        super().__init__() 
  
        
        self.setWindowTitle("Python Stop watch") 
  
        
        self.setGeometry(100, 100, 400, 500) 
  
        
        self.UiComponents() 
  
        
        self.show() 
  
    
    def UiComponents(self): 
  
        
        self.count = 0
  
        
        self.flag = False
  
        
        self.label = QLabel(self) 
  
        
        self.label.setGeometry(75, 100, 250, 70) 
  
        
        self.label.setStyleSheet("border : 4px solid black;") 
  
        
        self.label.setText(str(self.count)) 
  
        
        self.label.setFont(QFont('Arial', 25)) 
  
        
        self.label.setAlignment(Qt.AlignCenter) 
  
        
        start = QPushButton("Start", self) 
  
        
        start.setGeometry(125, 250, 150, 40) 
  
        
        start.pressed.connect(self.Start) 
  
        
        pause = QPushButton("Pause", self) 
  
        
        pause.setGeometry(125, 300, 150, 40) 
  
        
        pause.pressed.connect(self.Pause) 
  
        
        re_set = QPushButton("Re-set", self) 
  
        
        re_set.setGeometry(125, 350, 150, 40) 
  
        
        re_set.pressed.connect(self.Re_set) 
  
        
        timer = QTimer(self) 
  
        
        timer.timeout.connect(self.showTime) 
  
        
        timer.start(100) 
  
    
    def showTime(self): 
  
        
        if self.flag: 
  
            
            self.count+= 1
  
        
        text = str(self.count / 10) 
  
        
        self.label.setText(text) 
  
  
    def Start(self): 
  
        
        self.flag = True
  
    def Pause(self): 
  
        
        self.flag = False
  
    def Re_set(self): 
  
        
        self.flag = False
  
        
        self.count = 0
  
        
        self.label.setText(str(self.count)) 
  
  
App = QApplication(sys.argv) 
  
window = Window()
window.show() 
  
App.exec_()
=======
import cv2
import mediapipe as mp
import os

#------- Declaranos el detector -------
nombre = 'Ema_Sintapabocas'
direccion = 'C:/Users/Jorge Andres Julio L/DesktopProyectoDetector'
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
>>>>>>> 9d2232e185bf209aab7c0ac3e03d3b24616d3d0a
