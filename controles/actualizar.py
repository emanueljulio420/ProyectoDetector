import shutil
from PySide2.QtWidgets import QWidget, QMessageBox, QFileDialog
from PySide2.QtCore import Qt
from ui_python.Ui_actualizar import Ui_Form
from db.usuarios import actualizar

class Actualizar(QWidget, Ui_Form):

    def __init__(self,id,parent=None):
        self._id = id
        super().__init__(parent)
        self.setupUi(self)
        
        self.setWindowFlag(Qt.Window)

        self.acepButton.clicked.connect(self.cambiar_datos)
        self.cancelButton_2.clicked.connect(self.cancelar)
        self.fotoButton.clicked.connect(self.seleccionar_foto)
    
    def cambiar_datos(self):
        nombre = self.nombreEdit.text()
        correo = self.correoEdit.text()
        path = self.pathEdit.text()

        if self.verificar_espacios():
            nueva_foto = shutil.copy(path, 'Fotos_usuarios')
            self.pathEdit.setText(nueva_foto)
    
    def cancelar(self):
        self.limpiar()
        self.hide()

    def verificar_espacios(self):
        nombre = self.nombreEdit.text()
        correo = self.correoEdit.text()
        path = self.pathEdit.text()

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

        if path == "":
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

    def limpiar(self):
        self.nombreEdit.clear()
        self.correoEdit.clear()

    def seleccionar_foto(self):
        file_path = QFileDialog.getOpenFileName()[0]
        print(file_path)
        self.pathEdit.setText(file_path)