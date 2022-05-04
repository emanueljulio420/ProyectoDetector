# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'actualizar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 438)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamily(u"SansSerif")
        font.setPointSize(24)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.nombreEdit = QLineEdit(self.frame_5)
        self.nombreEdit.setObjectName(u"nombreEdit")

        self.horizontalLayout_4.addWidget(self.nombreEdit)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label)

        self.correoEdit = QLineEdit(self.frame_4)
        self.correoEdit.setObjectName(u"correoEdit")

        self.horizontalLayout_3.addWidget(self.correoEdit)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setFamily(u"SansSerif")
        font2.setPointSize(12)
        self.label_4.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.pathEdit = QLineEdit(self.frame_6)
        self.pathEdit.setObjectName(u"pathEdit")

        self.horizontalLayout_5.addWidget(self.pathEdit)

        self.fotoButton = QPushButton(self.frame_6)
        self.fotoButton.setObjectName(u"fotoButton")
        icon = QIcon()
        icon.addFile(u"./imagenes/add-image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fotoButton.setIcon(icon)
        self.fotoButton.setIconSize(QSize(60, 60))

        self.horizontalLayout_5.addWidget(self.fotoButton)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.acepButton = QPushButton(self.frame_3)
        self.acepButton.setObjectName(u"acepButton")
        font3 = QFont()
        font3.setFamily(u"SansSerif")
        font3.setPointSize(10)
        self.acepButton.setFont(font3)

        self.horizontalLayout_2.addWidget(self.acepButton)

        self.cancelButton_2 = QPushButton(self.frame_3)
        self.cancelButton_2.setObjectName(u"cancelButton_2")
        self.cancelButton_2.setFont(font3)

        self.horizontalLayout_2.addWidget(self.cancelButton_2)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignRight)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Actualizar", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.label.setText(QCoreApplication.translate("Form", u"Correo", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Foto", None))
        self.fotoButton.setText("")
        self.acepButton.setText(QCoreApplication.translate("Form", u"Aceptar", None))
        self.cancelButton_2.setText(QCoreApplication.translate("Form", u"Cancelar", None))
    # retranslateUi

