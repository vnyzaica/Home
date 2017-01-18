from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.label.setText(_translate("MainWindow", "Программа которая...."))
    def myFunction(self):
        sait = (self.lineEdit.text)
        self.label.setText(sait())
		
#Создать папку
os.mkdir(name)	
	
#открыть cmd
import os
os.system(r'C:\WINDOWS\system32\cmd.exe')

#Зайти на сайт 
svn list (sait)

#Cкачать 
svn update

#переместить
svn move "рипозиторий" "x"
x=x+1

#архивы
import zipfile
import os
import time
time = datetime.datetime.now() # Время и дата
#как записать в название файла дату и время
z = zipfile.ZipFile('spam,"x".zip', 'w')        # Создание нового архива
for root, dirs, files in os.walk('folder'): # Список всех файлов и папок в директории folder
for file in files:
   z.write(os.path.join(root,file))         # Создание относительных путей и запись файлов в архив
z.close()

#Удалить папку
import os
import shutil
path = 'C://qq/'#Путь
shutil.rmtree(path)#процесс удаления


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
	