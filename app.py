from PySide2.QtWidgets import QApplication
from controles.inicio import Crear_usuario

if __name__ == '__main__':

    app = QApplication()
    window = Crear_usuario()
    window.show()
    app.exec_()

