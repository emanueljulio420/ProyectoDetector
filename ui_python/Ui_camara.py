# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camara.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Camara(object):
    def setupUi(self, Camara):
        if not Camara.objectName():
            Camara.setObjectName(u"Camara")
        Camara.resize(853, 733)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Camara.sizePolicy().hasHeightForWidth())
        Camara.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Camara)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.frame_4 = QFrame(Camara)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_4.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.usuarioButton = QPushButton(self.frame_2)
        self.usuarioButton.setObjectName(u"usuarioButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.usuarioButton.sizePolicy().hasHeightForWidth())
        self.usuarioButton.setSizePolicy(sizePolicy1)
        self.usuarioButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"../imagenes/mascarilla-medica (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.usuarioButton.setIcon(icon)
        self.usuarioButton.setIconSize(QSize(80, 80))

        self.horizontalLayout_3.addWidget(self.usuarioButton)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setLayoutDirection(Qt.RightToLeft)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.reiniciarButton = QPushButton(self.frame_5)
        self.reiniciarButton.setObjectName(u"reiniciarButton")
        sizePolicy1.setHeightForWidth(self.reiniciarButton.sizePolicy().hasHeightForWidth())
        self.reiniciarButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.reiniciarButton)

        self.horaslabel = QLabel(self.frame_5)
        self.horaslabel.setObjectName(u"horaslabel")
        sizePolicy1.setHeightForWidth(self.horaslabel.sizePolicy().hasHeightForWidth())
        self.horaslabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.horaslabel)

        self.minutoslabel = QLabel(self.frame_5)
        self.minutoslabel.setObjectName(u"minutoslabel")
        sizePolicy1.setHeightForWidth(self.minutoslabel.sizePolicy().hasHeightForWidth())
        self.minutoslabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.minutoslabel)

        self.segundoslabel = QLabel(self.frame_5)
        self.segundoslabel.setObjectName(u"segundoslabel")
        sizePolicy1.setHeightForWidth(self.segundoslabel.sizePolicy().hasHeightForWidth())
        self.segundoslabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.segundoslabel)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame = QFrame(Camara)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_lateral = QFrame(self.frame)
        self.frame_lateral.setObjectName(u"frame_lateral")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_lateral.sizePolicy().hasHeightForWidth())
        self.frame_lateral.setSizePolicy(sizePolicy2)
        self.frame_lateral.setMinimumSize(QSize(30, 0))
        self.frame_lateral.setMaximumSize(QSize(200, 1000))
        self.frame_lateral.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.frame_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_lateral)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.eliminarButton = QPushButton(self.frame_lateral)
        self.eliminarButton.setObjectName(u"eliminarButton")
        self.eliminarButton.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.eliminarButton.sizePolicy().hasHeightForWidth())
        self.eliminarButton.setSizePolicy(sizePolicy2)
        self.eliminarButton.setMinimumSize(QSize(170, 60))
        icon1 = QIcon()
        icon1.addFile(u"../imagenes/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eliminarButton.setIcon(icon1)
        self.eliminarButton.setIconSize(QSize(50, 50))

        self.verticalLayout_4.addWidget(self.eliminarButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.actualizarButton = QPushButton(self.frame_lateral)
        self.actualizarButton.setObjectName(u"actualizarButton")
        sizePolicy2.setHeightForWidth(self.actualizarButton.sizePolicy().hasHeightForWidth())
        self.actualizarButton.setSizePolicy(sizePolicy2)
        self.actualizarButton.setMinimumSize(QSize(170, 60))
        icon2 = QIcon()
        icon2.addFile(u"../imagenes/recargar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actualizarButton.setIcon(icon2)
        self.actualizarButton.setIconSize(QSize(50, 50))

        self.verticalLayout_4.addWidget(self.actualizarButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.iniciarButton = QPushButton(self.frame_lateral)
        self.iniciarButton.setObjectName(u"iniciarButton")
        sizePolicy1.setHeightForWidth(self.iniciarButton.sizePolicy().hasHeightForWidth())
        self.iniciarButton.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.iniciarButton)

        self.cerrarButton = QPushButton(self.frame_lateral)
        self.cerrarButton.setObjectName(u"cerrarButton")
        sizePolicy2.setHeightForWidth(self.cerrarButton.sizePolicy().hasHeightForWidth())
        self.cerrarButton.setSizePolicy(sizePolicy2)
        self.cerrarButton.setMinimumSize(QSize(170, 60))
        icon3 = QIcon()
        icon3.addFile(u"../imagenes/cerrar-sesion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cerrarButton.setIcon(icon3)
        self.cerrarButton.setIconSize(QSize(50, 50))

        self.verticalLayout_4.addWidget(self.cerrarButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.frame_lateral)

        self.camaraframe = QFrame(self.frame)
        self.camaraframe.setObjectName(u"camaraframe")
        self.camaraframe.setFrameShape(QFrame.StyledPanel)
        self.camaraframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.camaraframe)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mondagraphicsView = QGraphicsView(self.camaraframe)
        self.mondagraphicsView.setObjectName(u"mondagraphicsView")

        self.verticalLayout_2.addWidget(self.mondagraphicsView)


        self.horizontalLayout.addWidget(self.camaraframe)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Camara)

        QMetaObject.connectSlotsByName(Camara)
    # setupUi

    def retranslateUi(self, Camara):
        Camara.setWindowTitle(QCoreApplication.translate("Camara", u"Form", None))
#if QT_CONFIG(tooltip)
        self.frame_4.setToolTip(QCoreApplication.translate("Camara", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.usuarioButton.setText(QCoreApplication.translate("Camara", u"Usuario", None))
        self.reiniciarButton.setText(QCoreApplication.translate("Camara", u"Reiniciar", None))
        self.horaslabel.setText("")
        self.minutoslabel.setText("")
        self.segundoslabel.setText("")
#if QT_CONFIG(tooltip)
        self.eliminarButton.setToolTip(QCoreApplication.translate("Camara", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.eliminarButton.setText(QCoreApplication.translate("Camara", u"  Eliminar usuario", None))
#if QT_CONFIG(shortcut)
        self.eliminarButton.setShortcut("")
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(whatsthis)
        self.actualizarButton.setWhatsThis(QCoreApplication.translate("Camara", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.actualizarButton.setText(QCoreApplication.translate("Camara", u"  Actualizar usuario", None))
        self.iniciarButton.setText(QCoreApplication.translate("Camara", u"Inicirar", None))
        self.cerrarButton.setText(QCoreApplication.translate("Camara", u"  Cerrar secion", None))
    # retranslateUi

