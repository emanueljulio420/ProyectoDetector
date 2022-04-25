from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PySide2 import QtCore
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
        self.usuarioButton.clicked.connect(self.abrir_menu)

    def abrir_menu(self):
        if True:
            width = self.frame_lateral.width()
            normal = 0
            if width == 0:
                extender = 200
            else:
                extender = normal
            
            animacion = QPropertyAnimation(self.frame_lateral, b'minimunWidth')
            animacion.setDirection(350)
            animacion.setStartValue(width)
            animacion.setEndValue(extender)
            animacion.setEasingCurve(QtCore, QEasingCurve.InOutQuart)
            animacion.start()
        print('monda')

    def actualizar(self):
        from controles.actualizar import Actualizar
        window = Actualizar(self._id,self)
        window.show()

    def eliminar(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Usuario actualizado correctamente")
        msgBox.setWindowTitle("Informacion")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        res = msgBox.exec_()

        if res == True:
            eliminar_usuario(self._id)
            from controles.inicio import Crear_usuario
            window = Crear_usuario(self)
            window.show()
            self.hide()

