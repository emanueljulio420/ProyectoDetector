from PySide2.QtWidgets import QWidget,QMessageBox
from ui_python.Ui_crear_usuario import Ui_Crae_usuario
from db.usuarios import new_usuario, buscar_nombre, buscar_correo, buscar_id

class Crear_usuario(QWidget, Ui_Crae_usuario):

    def __init__(self,parent = None):
        super().__init__()

        self.setupUi(self)

        self.crearButton.clicked.connect(self.crear_usuario)
        self.iniciarButton.clicked.connect(self.iniciar_secion)

    def verificar_espacios(self):
        nombre = self.nombreEdit.toPlainText()
        correo = self.correoEdit_2.toPlainText()

        errores = 0

        if nombre == "":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Nombre obligatorio")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            errores += 1
        if correo == "":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Correo obligatorio")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            errores += 1

        if correo:
            if '@' in correo:
                print('Correo valido')
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Correo invalido")
                msgBox.setWindowTitle("Error")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                errores += 1

        if errores == 0 :
            return True


    def limpiar_espacios(self):
        self.nombreEdit.clear()
        self.correoEdit_2.clear()

    # ------------------ Iniciar sesion -------------------

    def iniciar_secion(self):
        nombre = self.nombreEdit.toPlainText()
        correo = self.correoEdit_2.toPlainText()

        dato1 = buscar_nombre(nombre)
        dato2 = buscar_correo(correo)

        fila1 = dato1
        fila2 = dato2

    
        if self.verificar_espacios():

            if fila1 == fila2:	
                if dato1 == [] and dato2 ==[]:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setText("Nombre o correo incorrectos")
                    msgBox.setWindowTitle("Error")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()

                else:

                    if dato1 ==[]:
                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Warning)
                        msgBox.setText("Nombre incorrectos")
                        msgBox.setWindowTitle("Error")
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec_()
                    else:
                        dato1 = dato1[0][1]
                    if dato2 ==[]:
                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Warning)
                        msgBox.setText("Correo incorrectos")
                        msgBox.setWindowTitle("Error")
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec_()
                    else:
                        dato2 = dato2[0][2]

                    if dato1 != [] and dato2 != []:
                        id = buscar_id(correo)
                        from controles.camara import Camara
                        window = Camara(id,self)
                        window.show()
                        self.hide()
            else:                        
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Nombre o correo incorrectos")
                msgBox.setWindowTitle("Error")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()

    # ------------------ Crear usuario nuevo -------------------

    def crear_usuario(self):
        nombre = self.nombreEdit.toPlainText()
        correo = self.correoEdit_2.toPlainText()

        if self.verificar_espacios():
            if buscar_correo(correo) != []:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Usuario ya existente")
                msgBox.setWindowTitle("Error")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
            else:
                data = (nombre,correo)
                if new_usuario(data):
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setText("Usuario creado correctamente")
                    msgBox.setWindowTitle("Informacion")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
