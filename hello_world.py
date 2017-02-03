#coding:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
import zipfile
import os
import time
import shutil
import sqlite3
import datetime
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 180)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(5, 20, 230, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 120, 181, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.myFunction)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Work"))
        self.pushButton.setText(_translate("MainWindow", "Download"))
        self.label.setText(_translate("MainWindow", "Введите адрес"))
    def myFunction(self):
        site = (self.lineEdit.text)
        self.label.setText(site())
        if os.path.exists("/home/py/qq1") == True :#??????
            pass
        else:
            os.mkdir("/home/py/qq1") 


        if os.path.exists("/home/py/download") == True :
            pass
        else:
            os.mkdir("/home/py/download") 
            os.system("/home/py/qq1")
            os.system("git clone {}".format(site))#Команда
#os.system("svn update")
#os.system("svn move "рипозиторий" "x"")

        time = datetime.time() # Время и дата
#как записать в название файла дату и время
#z = zipfile.ZipFile('time{}.zip'.format(time)) # Создание нового архива
        z = zipfile.ZipFile('file.zip')
        for root, dirs, files in os.walk('folder'): # Список всех файлов и папок в директории folder
            for file in files:
                z.write(os.path.join(root,file)) # Создание относительных путей и запись файлов в архив
                z.close()
                connection=sqlite3.connect('database')#создаём соединение с базой данных
                connection.cursor()#создаём курсор - основной инструмент работы с БД


        cursor.execute('create table pupils (name char(30),mark integer(1))')#создаём таблицу
        cursor.execute('insert into pupils values (?,?)',(time,sait))#заносим в таблицу значения
        connection.commit()#сохраняем изменения
        connection.close()


#Удалить папку
        path = '/home/py/qq1'#Путь
        shutil.rmtree(path)#процесс удаления



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())