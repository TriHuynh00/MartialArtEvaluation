# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName(_fromUtf8("Main"))
        Main.resize(443, 324)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtGui.QWidget(Main)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 441, 323))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_10.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.lblDuration_6 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(31)
        sizePolicy.setVerticalStretch(31)
        sizePolicy.setHeightForWidth(self.lblDuration_6.sizePolicy().hasHeightForWidth())
        self.lblDuration_6.setSizePolicy(sizePolicy)
        self.lblDuration_6.setText(_fromUtf8(""))
        self.lblDuration_6.setPixmap(QtGui.QPixmap(_fromUtf8("icons/batman.png")))
        self.lblDuration_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDuration_6.setObjectName(_fromUtf8("lblDuration_6"))
        self.horizontalLayout_6.addWidget(self.lblDuration_6)
        self.lbl_NameP2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.lbl_NameP2.setObjectName(_fromUtf8("lbl_NameP2"))
        self.horizontalLayout_6.addWidget(self.lbl_NameP2)
        self.txtName_P1 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.txtName_P1.setObjectName(_fromUtf8("txtName_P1"))
        self.horizontalLayout_6.addWidget(self.txtName_P1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lblDuration_5 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(31)
        sizePolicy.setVerticalStretch(31)
        sizePolicy.setHeightForWidth(self.lblDuration_5.sizePolicy().hasHeightForWidth())
        self.lblDuration_5.setSizePolicy(sizePolicy)
        self.lblDuration_5.setText(_fromUtf8(""))
        self.lblDuration_5.setPixmap(QtGui.QPixmap(_fromUtf8("icons/superman.png")))
        self.lblDuration_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDuration_5.setObjectName(_fromUtf8("lblDuration_5"))
        self.horizontalLayout_5.addWidget(self.lblDuration_5)
        self.lbl_Name = QtGui.QLabel(self.verticalLayoutWidget)
        self.lbl_Name.setObjectName(_fromUtf8("lbl_Name"))
        self.horizontalLayout_5.addWidget(self.lbl_Name)
        self.txtName_P2 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.txtName_P2.setObjectName(_fromUtf8("txtName_P2"))
        self.horizontalLayout_5.addWidget(self.txtName_P2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_11.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.btnEasy = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnEasy.setObjectName(_fromUtf8("btnEasy"))
        self.horizontalLayout_9.addWidget(self.btnEasy)
        self.btnMedium = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnMedium.setObjectName(_fromUtf8("btnMedium"))
        self.horizontalLayout_9.addWidget(self.btnMedium)
        self.btnHard = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnHard.setObjectName(_fromUtf8("btnHard"))
        self.horizontalLayout_9.addWidget(self.btnHard)
        self.btnCustom = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnCustom.setObjectName(_fromUtf8("btnCustom"))
        self.horizontalLayout_9.addWidget(self.btnCustom)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_14.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblDuration_2 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(31)
        sizePolicy.setVerticalStretch(31)
        sizePolicy.setHeightForWidth(self.lblDuration_2.sizePolicy().hasHeightForWidth())
        self.lblDuration_2.setSizePolicy(sizePolicy)
        self.lblDuration_2.setText(_fromUtf8(""))
        self.lblDuration_2.setPixmap(QtGui.QPixmap(_fromUtf8("icons/clock.png")))
        self.lblDuration_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDuration_2.setObjectName(_fromUtf8("lblDuration_2"))
        self.horizontalLayout.addWidget(self.lblDuration_2)
        self.lblDuration = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblDuration.setObjectName(_fromUtf8("lblDuration"))
        self.horizontalLayout.addWidget(self.lblDuration)
        self.sbDuration = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.sbDuration.setMinimum(1)
        self.sbDuration.setMaximum(3600)
        self.sbDuration.setProperty("value", 60)
        self.sbDuration.setObjectName(_fromUtf8("sbDuration"))
        self.horizontalLayout.addWidget(self.sbDuration)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lblDuration_3 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(31)
        sizePolicy.setVerticalStretch(31)
        sizePolicy.setHeightForWidth(self.lblDuration_3.sizePolicy().hasHeightForWidth())
        self.lblDuration_3.setSizePolicy(sizePolicy)
        self.lblDuration_3.setText(_fromUtf8(""))
        self.lblDuration_3.setPixmap(QtGui.QPixmap(_fromUtf8("icons/weight.png")))
        self.lblDuration_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDuration_3.setObjectName(_fromUtf8("lblDuration_3"))
        self.horizontalLayout_3.addWidget(self.lblDuration_3)
        self.lblForce = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblForce.setObjectName(_fromUtf8("lblForce"))
        self.horizontalLayout_3.addWidget(self.lblForce)
        self.sbForce = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.sbForce.setMinimum(1)
        self.sbForce.setMaximum(1000)
        self.sbForce.setProperty("value", 10)
        self.sbForce.setObjectName(_fromUtf8("sbForce"))
        self.horizontalLayout_3.addWidget(self.sbForce)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblDuration_4 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(31)
        sizePolicy.setVerticalStretch(31)
        sizePolicy.setHeightForWidth(self.lblDuration_4.sizePolicy().hasHeightForWidth())
        self.lblDuration_4.setSizePolicy(sizePolicy)
        self.lblDuration_4.setText(_fromUtf8(""))
        self.lblDuration_4.setPixmap(QtGui.QPixmap(_fromUtf8("icons/boxing_glove.png")))
        self.lblDuration_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDuration_4.setObjectName(_fromUtf8("lblDuration_4"))
        self.horizontalLayout_2.addWidget(self.lblDuration_4)
        self.lblNrOfHits = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblNrOfHits.setObjectName(_fromUtf8("lblNrOfHits"))
        self.horizontalLayout_2.addWidget(self.lblNrOfHits)
        self.sbNrOfHits = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.sbNrOfHits.setMaximum(360000)
        self.sbNrOfHits.setObjectName(_fromUtf8("sbNrOfHits"))
        self.horizontalLayout_2.addWidget(self.sbNrOfHits)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.btnRanking = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnRanking.setObjectName(_fromUtf8("btnRanking"))
        self.horizontalLayout_4.addWidget(self.btnRanking)
        self.btnStart = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.horizontalLayout_4.addWidget(self.btnStart)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayoutWidget.raise_()

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(_translate("Main", "Punch competition", None))
        self.label.setText(_translate("Main", "Players", None))
        self.lbl_NameP2.setText(_translate("Main", "Name:", None))
        self.lbl_Name.setText(_translate("Main", "Name:", None))
        self.label_2.setText(_translate("Main", "Difficulty", None))
        self.btnEasy.setText(_translate("Main", "Easy", None))
        self.btnMedium.setText(_translate("Main", "Medium", None))
        self.btnHard.setText(_translate("Main", "Hard", None))
        self.btnCustom.setText(_translate("Main", "Custom", None))
        self.label_3.setText(_translate("Main", "Parameters", None))
        self.lblDuration.setText(_translate("Main", "Duration (s):", None))
        self.lblForce.setText(_translate("Main", "Minimum force (kg):", None))
        self.lblNrOfHits.setText(_translate("Main", "Nr. of hits", None))
        self.btnRanking.setText(_translate("Main", "Ranking", None))
        self.btnStart.setText(_translate("Main", "Start", None))

