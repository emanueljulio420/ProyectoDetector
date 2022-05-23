import time
import cv2
import mediapipe as mp
import numpy as np
from PySide2.QtWidgets import * 
from PySide2 import QtCore, QtGui 
from PySide2.QtGui import * 
from PySide2.QtCore import * 
from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2 import QtCore
from numpy import append
from ui_python.Ui_camara import Ui_Camara
from db.usuarios import eliminar_usuario, nombre_id
import os

class Camara(QWidget, Ui_Camara):

    def __init__(self,id, parent=None):
        self.id = id[0][0]
        print(self.id)
        super().__init__(parent)
        self.setupUi(self)
        self.nombre = nombre_id(self.id)[0][0]
    
        direccion = 'C:/Users/Emanuel Julio Lemos/Desktop/ProyectoDetector/fotos'
        carpeta = direccion + '/' + self.nombre

        if not os.path.exists(carpeta):
            print('carpeta creada')
            os.makedirs(carpeta)

        self.setWindowFlag(Qt.Window)
        self.count = 0
        self.flag = False
        self.horaslabel.setGeometry(75, 100, 250, 70) 
        self.horaslabel.setStyleSheet("border : 4px solid black;")       
        self.horaslabel.setText(str(self.count)) 
        self.horaslabel.setFont(QFont('Arial', 25)) 
        self.horaslabel.setAlignment(Qt.AlignCenter)

        timer = QTimer(self) 
  
        timer.timeout.connect(self.showtime) 
  
        timer.start(100)

        self.flag = True

        self.reiniciarButton.clicked.connect(self.reiniciar_cronometro)
        self.iniciarButton.clicked.connect(self.identificar)
        self.entrenarButton.clicked.connect(self.entrenar_inteligencia)
        self.eliminarButton.clicked.connect(self.eliminar)
        self.actualizarButton.clicked.connect(self.actualizar)
        self.cerrarButton.clicked.connect(self.cerrar_secion)

    def showtime(self):
        if self.flag: 
      
            self.count+= 1
        
        text = str(self.count / 10) 
        
        self.horaslabel.setText(text)

    def reiniciar_cronometro(self):
        self.count = 0
  
        self.label.setText(str(self.count))
 
    def entrenar_inteligencia(self):
        print('Pongase el tapabocas')

        time.sleep(10)
        self.tomar_fotos_tapabocas()

        print('Sin tapabocas')

        time.sleep(10)

        self.tomar_fotos_sintapabocas()

        time.sleep(10)

        self.entenar()
    
    def identificar(self):
        direccion = f'C:/Users/Emanuel Julio Lemos/Desktop/ProyectoDetector/fotos/{self.nombre}'
        etiquetas = os.listdir(direccion)

        print('Nombres', etiquetas)

        modelo = cv2.face.LBPHFaceRecognizer_create()

        # leer modelo

        modelo.read('Modelo.xml')

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

                        al, an, c = frame.shape

                        xi = rostro.location_data.relative_bounding_box.xmin
                        yi = rostro.location_data.relative_bounding_box.ymin

                        ancho = rostro.location_data.relative_bounding_box.width
                        alto = rostro.location_data.relative_bounding_box.height

                        xi = int(xi*an)
                        yi = int(yi*al)
                        ancho = int(ancho*an)
                        alto = int(alto*al)

                        xf = xi + ancho
                        yf = yi + alto

                        # Estrraccion de pixelesp y establecer tamaño de foto
                        cara = frame[yi:yf, xi:xf]
                        cara = cv2.resize(cara, (150,200), interpolation=cv2.INTER_CUBIC)
                        cara = cv2.cvtColor(cara, cv2.COLOR_BGR2GRAY)
                        # predicir
                        prediccion = modelo.predict(cara)

                        if prediccion[0] == 0:
                            cv2.putText(frame, '{}'.format(etiquetas[0]), (xi, yi - 5), 1, 1.3, (0,0,255), 1, cv2.LINE_AA)
                            cv2.rectangle(frame, (xi, yi), (yi, yf), (0, 0, 255), 2)
                        elif prediccion[0] == 1:
                            cv2.putText(frame, '{}'.format(etiquetas[0]), (xi, yi - 5), 1, 1.3, (255, 0,0), 1, cv2.LINE_AA)
                            cv2.rectangle(frame, (xi, yi), (yi, yf), (255, 0, 0), 2)
                        

                cv2.imshow('monda', frame)

                tecla = cv2.waitKey(1)
                if tecla == 112:
                    break 

        cap.release()

    def entenar(self):

        direccion = f'C:/Users/Emanuel Julio Lemos/Desktop/ProyectoDetector/fotos/{self.nombre}'

        lista = os.listdir(direccion)

        etiquetas = []
        rostros = []
        cont = 0

        for nameDir in lista:
            nombre = direccion + '/' + nameDir
            
            for fileName in os.listdir(nombre):
                etiquetas.append(cont)
                rostros.append(cv2.imread(nombre + '/' + fileName, 0))

            cont = cont + 1

        # -------- Creacion del modelo ------

        modelo = cv2.face.LBPHFaceRecognizer_create()

        # --------- Entrenando --------

        modelo.train(rostros, np.array(etiquetas))

        # ----------- guardar madelo

        modelo.write('Modelo.xml')
        print('modelo entrenado')

    def tomar_fotos_tapabocas(self):

        #------- Declaranos el detector -------
        nombre = f'{self.nombre}_tapabocas'
        direccion = f'C:/Users/Emanuel Julio Lemos/Desktop/ProyectoDetector/fotos/{self.nombre}'
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

                        al, an, c = frame.shape

                        xi = rostro.location_data.relative_bounding_box.xmin
                        yi = rostro.location_data.relative_bounding_box.ymin

                        ancho = rostro.location_data.relative_bounding_box.width
                        alto = rostro.location_data.relative_bounding_box.height

                        xi = int(xi*an)
                        yi = int(yi*al)
                        ancho = int(ancho*an)
                        alto = int(alto*al)

                        xf = xi + ancho
                        yf = yi + alto

                        # Estrraccion de pixelesp y establecer tamaño de foto
                        cara = frame[yi:yf, xi:xf]
                        cara = cv2.resize(cara, (150,200), interpolation=cv2.INTER_CUBIC)

                        # guardar fotos
                        
                        cv2.imwrite(carpeta + '/rostro_{}.jpg'.format(count), cara)
                        count = count + 1

                cv2.imshow('monda', frame)

                tecla = cv2.waitKey(1)
                if tecla == 112 or count > 300:
                    break 

        cap.release()
        cv2.destroyAllWindows()

    def tomar_fotos_sintapabocas(self):

        #------- Declaranos el detector -------
        nombre = f'{self.nombre}_Sintapabocas'
        direccion = f'C:/Users/Emanuel Julio Lemos/Desktop/ProyectoDetector/fotos/{self.nombre}'
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

                        al, an, c = frame.shape

                        xi = rostro.location_data.relative_bounding_box.xmin
                        yi = rostro.location_data.relative_bounding_box.ymin

                        ancho = rostro.location_data.relative_bounding_box.width
                        alto = rostro.location_data.relative_bounding_box.height

                        xi = int(xi*an)
                        yi = int(yi*al)
                        ancho = int(ancho*an)
                        alto = int(alto*al)

                        xf = xi + ancho
                        yf = yi + alto

                        # Estrraccion de pixelesp y establecer tamaño de foto
                        cara = frame[yi:yf, xi:xf]
                        cara = cv2.resize(cara, (150,200), interpolation=cv2.INTER_CUBIC)

                        # guardar fotos
                        
                        cv2.imwrite(carpeta + '/rostro_{}.jpg'.format(count), cara)
                        count = count + 1

                cv2.imshow('monda', frame)

                tecla = cv2.waitKey(1)
                if tecla == 112 or count > 300:
                    break 

        cap.release()
        cv2.destroyAllWindows()

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

