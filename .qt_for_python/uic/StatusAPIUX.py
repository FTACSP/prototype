# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\hugob\PycharmProjects\statusapiux_inc\ui\StatusAPIUX.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(760, 483)
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.WheelFocus)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(240, 0, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.botao_10 = QtWidgets.QPushButton(self.centralwidget)
        self.botao_10.setGeometry(QtCore.QRect(570, 330, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.botao_10.setFont(font)
        self.botao_10.setStyleSheet("")
        self.botao_10.setObjectName("botao_10")
        self.botao_1 = QtWidgets.QPushButton(self.centralwidget)
        self.botao_1.setEnabled(True)
        self.botao_1.setGeometry(QtCore.QRect(130, 360, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.botao_1.setFont(font)
        self.botao_1.setStyleSheet("")
        self.botao_1.setCheckable(False)
        self.botao_1.setChecked(False)
        self.botao_1.setDefault(False)
        self.botao_1.setObjectName("botao_1")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(70, 10, 91, 21))
        self.label_1.setStyleSheet("")
        self.label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 10, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.botao_2 = QtWidgets.QPushButton(self.centralwidget)
        self.botao_2.setEnabled(True)
        self.botao_2.setGeometry(QtCore.QRect(420, 360, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.botao_2.setFont(font)
        self.botao_2.setStyleSheet("")
        self.botao_2.setCheckable(False)
        self.botao_2.setChecked(False)
        self.botao_2.setDefault(False)
        self.botao_2.setObjectName("botao_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(110, 100, 541, 231))
        self.tableWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.botao_4 = QtWidgets.QPushButton(self.centralwidget)
        self.botao_4.setGeometry(QtCore.QRect(560, 420, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.botao_4.setFont(font)
        self.botao_4.setStyleSheet("")
        self.botao_4.setObjectName("botao_4")
        self.botao_5 = QtWidgets.QPushButton(self.centralwidget)
        self.botao_5.setGeometry(QtCore.QRect(660, 420, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.botao_5.setFont(font)
        self.botao_5.setStyleSheet("")
        self.botao_5.setObjectName("botao_5")
        self.label_title.raise_()
        self.botao_1.raise_()
        self.label_1.raise_()
        self.label_4.raise_()
        self.botao_2.raise_()
        self.tableWidget.raise_()
        self.botao_4.raise_()
        self.botao_10.raise_()
        self.botao_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestão de Avaliação"))
        self.label_title.setText(_translate("MainWindow", "Gestão de avaliação de CSPs"))
        self.botao_10.setText(_translate("MainWindow", "Detalhes"))
        self.botao_1.setText(_translate("MainWindow", "Gerir avaliador"))
        self.botao_2.setText(_translate("MainWindow", "Gerir provedor"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID (Auto)"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Avaliador"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Provedor"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Mês"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Ano"))
        self.botao_4.setText(_translate("MainWindow", "Voltar"))
        self.botao_5.setText(_translate("MainWindow", "Sair"))