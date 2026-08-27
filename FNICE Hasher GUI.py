# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FNICE Hasher GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QDesktopServices)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget, QGridLayout)
from random import randint

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(561, 316)
        MainWindow.setWindowIcon(QIcon(u"C:/Users/MSI/Downloads/logo.png"))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(801, 601))
        self.EncodeTab = QWidget()
        self.EncodeTab.setObjectName(u"EncodeTab")
        self.label = QLabel(self.EncodeTab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 421, 20))
        self.pushButton = QPushButton(self.EncodeTab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(450, 20, 75, 23))
        self.lineEdit = QLineEdit(self.EncodeTab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 50, 511, 20))
        self.pushButton_2 = QPushButton(self.EncodeTab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(450, 100, 75, 23))
        self.lineEdit_2 = QLineEdit(self.EncodeTab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 130, 511, 20))
        self.label_2 = QLabel(self.EncodeTab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 100, 421, 20))
        self.pushButton_3 = QPushButton(self.EncodeTab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 192, 511, 31))
        self.label_5 = QLabel(self.EncodeTab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 170, 491, 20))
        self.tabWidget.addTab(self.EncodeTab, "")
        self.DecodeTab = QWidget()
        self.DecodeTab.setObjectName(u"DecodeTab")
        self.pushButton_4 = QPushButton(self.DecodeTab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(450, 20, 75, 23))
        self.pushButton_5 = QPushButton(self.DecodeTab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 192, 511, 31))
        self.label_3 = QLabel(self.DecodeTab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 100, 421, 20))
        self.lineEdit_3 = QLineEdit(self.DecodeTab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 130, 511, 20))
        self.lineEdit_4 = QLineEdit(self.DecodeTab)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(20, 50, 511, 20))
        self.pushButton_6 = QPushButton(self.DecodeTab)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(450, 100, 75, 23))
        self.label_4 = QLabel(self.DecodeTab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 20, 421, 20))
        self.label_6 = QLabel(self.DecodeTab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 170, 491, 16))
        self.tabWidget.addTab(self.DecodeTab, "")
        self.CharMapTab = QWidget()
        self.CharMapTab.setObjectName(u"CharMapTab")
        self.pushButton_7 = QPushButton(self.CharMapTab)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 70, 531, 91))
        self.label_7 = QLabel(self.CharMapTab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 170, 511, 16))
        self.tabWidget.addTab(self.CharMapTab, "")
        self.AboutTab = QWidget()
        self.AboutTab.setObjectName(u"AboutTab")
        self.label_8 = QLabel(self.AboutTab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 20, 111, 41))
        self.label_8.setFrameShape(QFrame.NoFrame)
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.AboutTab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 70, 531, 51))
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.AboutTab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(80, 140, 231, 16))
        self.label_10.setAlignment(Qt.AlignCenter)
        self.pushButton_8 = QPushButton(self.AboutTab)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(330, 140, 141, 23))
        self.label_11 = QLabel(self.AboutTab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(120, 190, 191, 16))
        self.label_11.setAlignment(Qt.AlignCenter)
        self.pushButton_9 = QPushButton(self.AboutTab)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(310, 190, 141, 23))
        self.tabWidget.addTab(self.AboutTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FNICE Hasher", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"[File] The file that is giong to be encoded", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"[CharMap] The key that is going to encode the file", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Encode", None))
        self.label_5.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EncodeTab), QCoreApplication.translate("MainWindow", u"Encode", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Decode", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"[CharMap] The key that is going to encode the file", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"[File] The file that is giong to be encoded", None))
        self.label_6.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DecodeTab), QCoreApplication.translate("MainWindow", u"Decode", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Generate New CharMap File", None))
        self.label_7.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CharMapTab), QCoreApplication.translate("MainWindow", u"CharMap Generator", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"FNICE Hasher", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"This tool is made by darkstarshine2011 & it's completely FREE & OpenSource, Check it out on Github", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"darkstarshine2011/FNICE-Hasher", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Open In Browser", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"fnice.ir", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Open In Browser", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AboutTab), QCoreApplication.translate("MainWindow", u"About FNICE Hasher", None))
    # retranslateUi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(lambda: self.browse_file(self.ui.lineEdit))
        self.ui.pushButton_2.clicked.connect(lambda: self.browse_file(self.ui.lineEdit_2))
        self.ui.pushButton_4.clicked.connect(lambda: self.browse_file(self.ui.lineEdit_4))
        self.ui.pushButton_6.clicked.connect(lambda: self.browse_file(self.ui.lineEdit_3))

        self.ui.pushButton_3.clicked.connect(self.encode_files)
        self.ui.pushButton_5.clicked.connect(self.decode_files)
        self.ui.pushButton_7.clicked.connect(self.generate_charmap)

        self.ui.pushButton_8.clicked.connect(lambda: self.open_link("https://github.com/darkstarshine2011/FNICE-Hasher"))
        self.ui.pushButton_9.clicked.connect(lambda: self.open_link("https://fnice.ir"))

    def browse_file(self, line_edit):
        from PySide6.QtWidgets import QFileDialog
        path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*.*)")
        if path:
            line_edit.setText(path)

    def open_link(self, url):
        QDesktopServices.openUrl(QUrl(url))

    def encode_files(self):
        file_path = self.ui.lineEdit.text()
        charmap_path = self.ui.lineEdit_2.text()
        
        if not file_path or not charmap_path:
            self.ui.label_5.setText("ERROR: Select both files!")
            return

        try:
            with open(charmap_path, "rt") as f:
                charmap = f.read()
            
            with open(file_path, "rt") as f:
                content = f.read()
            
            encrypted = ""
            for char in content:
                if char in charmap:
                    idx = charmap.find(char)
                    encrypted += charmap[-(idx + 1)] if idx >= 0 else char
                else:
                    encrypted += char
            
            with open("Encrypted.FNICE.MK", "wt") as f:
                f.write(encrypted)
            
            self.ui.label_5.setText("✅ Encoded successfully!")
        except Exception as e:
            self.ui.label_5.setText(f"❌ Error: {str(e)}")

    def decode_files(self):
        file_path = self.ui.lineEdit_4.text()
        charmap_path = self.ui.lineEdit_3.text()
        
        if not file_path or not charmap_path:
            self.ui.label_6.setText("ERROR: Select both files!")
            return

        try:
            with open(charmap_path, "rt") as f:
                charmap = f.read()
            
            with open(file_path, "rt") as f:
                content = f.read()
            
            decrypted = ""
            for char in content:
                if char in charmap:
                    idx = charmap.find(char)
                    decrypted += charmap[-(idx + 1)] if idx >= 0 else char
                else:
                    decrypted += char
            
            with open("Decrypted.FNICE.MK", "wt") as f:
                f.write(decrypted)
            
            self.ui.label_6.setText("✅ Decoded successfully!")
        except Exception as e:
            self.ui.label_6.setText(f"❌ Error: {str(e)}")

    def generate_charmap(self):
        source = """ `1234567890-=qwertyuiop[]\\asdfghjkl;;'zxcvbbnmm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?
"""
        
        remaining = list(source)
        generated = ""
        
        while remaining:
            idx = randint(0, len(remaining) - 1)
            generated += remaining.pop(idx)
        
        try:
            with open("CharMap", "wt") as f:
                f.write(generated)
            self.ui.label_7.setText("✅ CharMap generated successfully!")
        except Exception as e:
            self.ui.label_7.setText(f"❌ Error: {str(e)}")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()