import time
from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Qt 
from PySide2 import QtCore
from numpy import append
from ui_python.Ui_camara import Ui_Camara
from db.usuarios import eliminar_usuario

class Camara(QWidget, Ui_Camara):

    def __init__(self,id, parent=None):
        self.id = id[0][0]
        print(self.id)
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        self.iniciarButton.clicked.connect(self.comenzar_conometro)
        self.eliminarButton.clicked.connect(self.eliminar)
        self.actualizarButton.clicked.connect(self.actualizar)
        self.cerrarButton.clicked.connect(self.cerrar_secion)
    
    def comenzar_conometro(self):
        import cv2
        import mediapipe as mp
        import os

        #------- Declaranos el detector -------
        nombre = 'Ema_Sintapabocas'
        direccion = 'C:/Users/Emanuel Julio Lemos/Desktop/Detecror/fotos'
        carpeta = direccion + '/' + nombre

        if not os.path.exists(carpeta):
            print('carpeta creada')
            os.makedirs(carpeta)

        # ------- Detector -------
        count = 0
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
                
                
                # cv2.imshow('self.camaraframe', frame)

                tecla = cv2.waitKey(1)
                if tecla == 112 or count > 300:
                    break 

        cap.release()

    def actualizar(self):
        from controles.actualizar import Actualizar
        window = Actualizar(self.id,self)
        window.show()

    def eliminar(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("Seguro de eliminar el usuario")
        msgBox.setWindowTitle("Informacion")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        res = msgBox.exec_()

        if res == QMessageBox.Yes:
            eliminar_usuario(self.id)
            from PySide2.QtWidgets import QWidget
            from ui_python.Ui_crear_usuario import Ui_Crae_usuario
            from controles.inicio import Crear_usuario
            window = Crear_usuario()
            window.show()

            self.hide()
            
    def cerrar_secion(self):
        from controles.inicio import Crear_usuario
        print('entre')
        window = Crear_usuario(self)
        window.show()
        
        pass

