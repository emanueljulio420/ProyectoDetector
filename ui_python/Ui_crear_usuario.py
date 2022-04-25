# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crear_usuario.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Crae_usuario(object):
    def setupUi(self, Crae_usuario):
        if not Crae_usuario.objectName():
            Crae_usuario.setObjectName(u"Crae_usuario")
        Crae_usuario.resize(500, 606)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Crae_usuario.sizePolicy().hasHeightForWidth())
        Crae_usuario.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(Crae_usuario)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Crae_usuario)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamily(u"SansSerif")
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"SansSerif")
        font1.setPointSize(14)
        self.label_2.setFont(font1)
        self.label_2.setLineWidth(1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.nombreEdit = QTextEdit(self.frame_2)
        self.nombreEdit.setObjectName(u"nombreEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.nombreEdit.sizePolicy().hasHeightForWidth())
        self.nombreEdit.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nombreEdit)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"SansSerif")
        font2.setPointSize(16)
        self.label.setFont(font2)
        self.label.setLayoutDirection(Qt.RightToLeft)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.correoEdit_2 = QTextEdit(self.frame_2)
        self.correoEdit_2.setObjectName(u"correoEdit_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.correoEdit_2.sizePolicy().hasHeightForWidth())
        self.correoEdit_2.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.correoEdit_2)

        self.spacer = QSpacerItem(80, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.formLayout.setItem(1, QFormLayout.SpanningRole, self.spacer)


        self.verticalLayout.addWidget(self.frame_2)

        self.Crear_usuario = QFrame(self.frame)
        self.Crear_usuario.setObjectName(u"Crear_usuario")
        sizePolicy2.setHeightForWidth(self.Crear_usuario.sizePolicy().hasHeightForWidth())
        self.Crear_usuario.setSizePolicy(sizePolicy2)
        self.Crear_usuario.setFrameShape(QFrame.StyledPanel)
        self.Crear_usuario.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Crear_usuario)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.crearButton = QPushButton(self.Crear_usuario)
        self.crearButton.setObjectName(u"crearButton")
        sizePolicy.setHeightForWidth(self.crearButton.sizePolicy().hasHeightForWidth())
        self.crearButton.setSizePolicy(sizePolicy)
        self.crearButton.setFont(font2)
        self.crearButton.setStyleSheet(u"background-color: rgb(0, 0, 255);")

        self.horizontalLayout_4.addWidget(self.crearButton)

        self.iniciarButton = QPushButton(self.Crear_usuario)
        self.iniciarButton.setObjectName(u"iniciarButton")
        sizePolicy.setHeightForWidth(self.iniciarButton.sizePolicy().hasHeightForWidth())
        self.iniciarButton.setSizePolicy(sizePolicy)
        self.iniciarButton.setFont(font2)
        self.iniciarButton.setStyleSheet(u"background-color: rgb(0, 255, 0);")

        self.horizontalLayout_4.addWidget(self.iniciarButton)


        self.verticalLayout.addWidget(self.Crear_usuario)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Crae_usuario)

        QMetaObject.connectSlotsByName(Crae_usuario)
    # setupUi

    def retranslateUi(self, Crae_usuario):
        Crae_usuario.setWindowTitle(QCoreApplication.translate("Crae_usuario", u"Inicio", None))
        self.label_3.setText(QCoreApplication.translate("Crae_usuario", u"Usuario", None))
        self.label_2.setText(QCoreApplication.translate("Crae_usuario", u"Nombre", None))
        self.label.setText(QCoreApplication.translate("Crae_usuario", u"<html><head/><body><p align=\"center\">Correo</p></body></html>", None))
        self.crearButton.setText(QCoreApplication.translate("Crae_usuario", u"Crear Usuario", None))
        self.iniciarButton.setText(QCoreApplication.translate("Crae_usuario", u"Iniciar secion", None))
    # retranslateUi

