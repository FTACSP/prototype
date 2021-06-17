# from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5 import QtGui, QtWidgets, QtCore, uic
from PyQt5 import Qt, QtWidgets
# from PyQt5.Qt import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QVBoxLayout, QMessageBox, QDateTimeEdit, QCalendarWidget
from PyQt5.QtWidgets import *
import os
import sys

import mysql.connector
from tela_login import Ui_tela_login
from tela_principal_avaliador import Ui_tela_principal_avaliador
from tela_principal_gestor import Ui_tela_principal_gestor
from tela_cadastros import Ui_tela_cadastros
from tela_cadastros_avaliador import Ui_tela_cadastros_avaliador
from tela_cadastros_provedor import Ui_tela_cadastros_provedor
from tela_cadastros_data import Ui_tela_cadastros_data

banco = mysql.connector.connect(host='localhost',
                                     user='hugo',
                                     password='885522',
                                     database='statusapidb')


class tela_login(QtWidgets.QWidget):
    def __init__(self, *args, **argvs):
        super(tela_login, self).__init__(*args, **argvs)
        self.ui = Ui_tela_login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.tela_login)
        # self.ui.pushButton_2.clicked.connect(self.tela_SAIR)
        #self.ui = Ui_tela_prin

    def tela_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        cursor = banco.cursor()
        cursor2 = banco.cursor()
        Comando_SQL = "select * from avaliadores where avaliadorusr=%s and avaliadorpw=%s and gestor=0"
        cursor.execute(Comando_SQL, (username, password))
        dados_lidos = cursor.fetchall()
        if(len(dados_lidos) > 0):
            # QMessageBox.about(tela_login, "ALERTA",
            #                   "Usuário encontrado")
            QMessageBox.information(
                QMessageBox(), "Usuário Encontrado!", "Entrou com Sucesso!")
            print(username)

            # self.ui.tela_principal_avaliador.comboBox.clear()
            # self.ui.tela_principal_avaliador.comboBox_2.clear()
            Comando_SQL = (
                "select avaliador from avaliadores where avaliadorusr=('%s')" % (username,))
            cursor.execute(Comando_SQL)
            dados_lidos = cursor.fetchall()
            for s in range(len(dados_lidos,)):
                print(dados_lidos[s])
                # self.ui.tela_principal_avaliador.comboBox.clearEditText()
                # self.ui.tela_cadastros.comboBox.addItem(str(dados_lidos[s][0]))
                # tela_login_cadastro.comboBox.addItem(str(dados_lidos[s][0]))
                # self.ui.tela_principal_avaliador.comboBox.addItem(
                #     str(dados_lidos[s][0]))
                banco.commit()
            self.window = tela_principal_avaliador()
            self.window.show()
            # cursor.close()
        Comando_SQL = "select * from avaliadores where avaliadorusr=%s and avaliadorpw=%s and gestor=1"
        cursor.execute(Comando_SQL, (username, password))
        dados_lidos = cursor.fetchall()
        if(len(dados_lidos) > 0):
            # QMessageBox.about(tela_login, "ALERTA",
            #                   "Gestor encontrado")
            QMessageBox.information(
                QMessageBox(), "Gestor encontrado!", "Entrou com Sucesso!")
            cursor = banco.cursor()
            cursor2 = banco.cursor()
            username = self.ui.lineEdit.text()
            print(username)
            self.tela_principal_gestor.comboBox.clear()
            #super(tela_principal_gestor, self).__init__(*args, **argvs)
            # self.ui = tela_principal_gestor()
            # self.ui.setupUi(self)
            # self.tela_principal_gestor.comboBox.clear()
            # self.tela_principal_gestor.comboBox_2.clear()
            Comando_SQL = (
                "select avaliador from avaliadores")
            # "select avaliador from avaliadores where avaliadorusr=('%s')" % (username,))
            cursor.execute(Comando_SQL)
            dados_lidos = cursor.fetchall()
            for s in range(len(dados_lidos,)):
                # if dados_lidos[s][0] != dados_lidos[s][0]:
                print(dados_lidos[s])
            # Comando_SQL2 = "update avaliadores set avaliador = replace(replace(avaliador, ',', ''), '"', '');"
            # cursor.execute(Comando_SQL2)
            # tela_login_cadastro.comboBox.addItem(cursor.execute(Comando_SQL))
                # self.ui.tela_principal_gestor.comboBox.clearEditText()
                # self.ui.tela_cadastros.comboBox.addItem(str(dados_lidos[s][0]))
                # self.ui.tela_principal_gestor.comboBox.addItem(
                #     str(dados_lidos[s][0]))
            # tela_login_cadastro.comboBox.
                banco.commit()
            self.window = tela_principal_gestor()
            self.window.show()
        Comando_SQL = "select * from avaliadores where avaliadorusr=%s and avaliadorpw=%s"
        cursor.execute(Comando_SQL, (username, password))
        dados_lidos = cursor.fetchall()
        if(len(dados_lidos) == 0):  # ==0 NÃO TEM USUÁRIO
            QMessageBox.information(
                QMessageBox(), "Usuário NÃO encontrado!", "Falha ao entrar!")

            # tela_login.show()
            return

        Comando_SQL2 = "select provedor from provedores"
        cursor2.execute(Comando_SQL2)
        dados_lidos2 = cursor2.fetchall()
        for s in range(len(dados_lidos2,)):

            print(dados_lidos2[s])

            # self.ui.tela_principal_gestor.comboBox_2.addItem(
            #     str(dados_lidos2[s][0]))

            banco.commit()
            # cursor.close()

        dados_lidos = ""
        cursor.close()

        # Tipo da avaliação### que define qual duração cadastrada será utilizada
        cursor3 = banco.cursor()
        Comando_SQL3 = "select tempoid from tempos"
        cursor3.execute(Comando_SQL3)
        dados_lidos3 = cursor3.fetchall()
        for s in range(len(dados_lidos3,)):

            print(dados_lidos3[s])

            # self.ui.tela_principal_gestor.comboBox_3.addItem(
            #     str(dados_lidos3[s][0]))
            # self.ui.tela_principal_avaliador.comboBox_3.addItem(
            #     str(dados_lidos3[s][0]))

            banco.commit()

        cursor3.close()
        # StatusAPIUX.show()
        # tempo_calendario()


# class botaoiniciar(self):
#     def __init__(self, *args, **argvs):
#         super(botaoiniciar, self).__init__(*args, **argvs)


class tela_principal_avaliador(QMainWindow):
    def __init__(self, *args, **argvs):
        super(tela_principal_avaliador, self).__init__(*args, **argvs)
        self.ui = Ui_tela_principal_avaliador()
        self.ui.setupUi(self)
        self.ui.comboBox = QtWidgets.QComboBox()


class tela_principal_gestor(QMainWindow):
    def __init__(self, *args, **argvs):
        super(tela_principal_gestor, self).__init__(*args, **argvs)
        self.ui = Ui_tela_principal_gestor()
        self.ui.setupUi(self)
        # o botao btn_cadastros chama funcao btn_cadastros
        self.ui.btn_cadastros.clicked.connect(self.btn_cadastros)
        self.ui.comboBox = QtWidgets.QComboBox()
        self.ui.comboBox_2 = QtWidgets.QComboBox()

    def btn_cadastros(self):  # classe do botao
        self.window = tela_cadastros()  # tem que fazer a funcao
        self.window.show()

    # def comboBox(self):
    #     self.ui.comboBox =


class tela_cadastros(QtWidgets.QWidget):
    def __init__(self, *args, **argvs):
        super(tela_cadastros, self).__init__(*args, **argvs)
        self.ui = Ui_tela_cadastros()
        self.ui.setupUi(self)
        self.ui.btn_avaliador.clicked.connect(self.btn_avaliador)
        self.ui.btn_provedor.clicked.connect(self.btn_provedor)
        self.ui.btn_data.clicked.connect(self.btn_duracao)
        self.ui.btn_data.excluir.connect(self.excluir)

    def btn_avaliador(self):
        self.window = tela_cadastros_avaliador()
        self.window.show()

    def btn_provedor(self):
        self.window = tela_cadastros_provedor()
        self.window.show()

    def btn_data(self):
        self.window = tela_cadastros_data()
        self.window.show()


class tela_cadastros_avaliador(QtWidgets.QWidget):
    def __init__(self, *args, **argvs):
        super(tela_cadastros_avaliador, self).__init__(*args, **argvs)
        self.ui = Ui_tela_cadastros_avaliador()
        self.ui.setupUi(self)
        self.ui.btn_novo_avaliador.clicked.connect(self.btn_novo_avaliador)

    def btn_novo_avaliador(self):
        name = self.ui.inputnome.text()


class tela_cadastros_provedor(QtWidgets.QWidget):
    def __init__(self, *args, **argvs):
        super(tela_cadastros_provedor, self).__init__(*args, **argvs)
        self.ui = Ui_tela_cadastros_provedor()
        self.ui.setupUi(self)
        self.ui.btn_novo_provedor.clicked.connect(self.btn_novo_provedor)

    def btn_novo_provedor(self):
        print("ok")


class tela_cadastros_data(QtWidgets.QWidget):
    def __init__(self, *args, **argvs):
        super(tela_cadastros_data, self).__init__(*args, **argvs)
        self.ui = Ui_tela_cadastros_data()
        self.ui.setupUi(self)
        self.ui.btn_novo_data.clicked.connect(self.btn_novo_data)

    def btn_novo_data(self):
        print("ok")
# passe dentro que ela é, se foi criado tela_login como widget, mainwindow, qdialog


app = QApplication(sys.argv)
# if(QDialog.Accepted == True):
# if(QWidget.isEnabled == True):
window = tela_login()  # janela quer que eu chame primeiro
window.show()
sys.exit(app.exec_())
