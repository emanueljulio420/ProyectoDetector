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

        self.eliminarButton.clicked.connect(self.eliminar)
        self.actualizarButton.clicked.connect(self.actualizar)
        self.cerrarButton.clicked.connect(self.cerrar_secion)

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

