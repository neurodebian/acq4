# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AOChannelTemplate.ui'
#
# Created: Sun Jul 26 17:33:37 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(529, 353)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(Form)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.preSetCheck = QtGui.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.preSetCheck.setFont(font)
        self.preSetCheck.setObjectName("preSetCheck")
        self.gridLayout.addWidget(self.preSetCheck, 0, 0, 1, 1)
        self.preSetSpin = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.preSetSpin.setFont(font)
        self.preSetSpin.setObjectName("preSetSpin")
        self.gridLayout.addWidget(self.preSetSpin, 0, 1, 1, 1)
        self.holdingCheck = QtGui.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.holdingCheck.setFont(font)
        self.holdingCheck.setObjectName("holdingCheck")
        self.gridLayout.addWidget(self.holdingCheck, 1, 0, 1, 1)
        self.holdingSpin = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.holdingSpin.setFont(font)
        self.holdingSpin.setObjectName("holdingSpin")
        self.gridLayout.addWidget(self.holdingSpin, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.frame = QtGui.QFrame(self.groupBox)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.functionCheck = QtGui.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.functionCheck.setFont(font)
        self.functionCheck.setObjectName("functionCheck")
        self.horizontalLayout.addWidget(self.functionCheck)
        self.displayCheck = QtGui.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.displayCheck.setFont(font)
        self.displayCheck.setChecked(True)
        self.displayCheck.setObjectName("displayCheck")
        self.horizontalLayout.addWidget(self.displayCheck)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.waveGeneratorWidget = StimGenerator(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waveGeneratorWidget.sizePolicy().hasHeightForWidth())
        self.waveGeneratorWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.waveGeneratorWidget.setFont(font)
        self.waveGeneratorWidget.setObjectName("waveGeneratorWidget")
        self.verticalLayout.addWidget(self.waveGeneratorWidget)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout_3.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.preSetCheck.setText(QtGui.QApplication.translate("Form", "Pre-set", None, QtGui.QApplication.UnicodeUTF8))
        self.holdingCheck.setText(QtGui.QApplication.translate("Form", "Holding", None, QtGui.QApplication.UnicodeUTF8))
        self.functionCheck.setText(QtGui.QApplication.translate("Form", "Enable Function", None, QtGui.QApplication.UnicodeUTF8))
        self.displayCheck.setText(QtGui.QApplication.translate("Form", "Display", None, QtGui.QApplication.UnicodeUTF8))

from lib.util.generator.StimGenerator import StimGenerator
