# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.job_title_box = QtWidgets.QLineEdit(self.centralwidget)
        self.job_title_box.setGeometry(QtCore.QRect(260, 140, 201, 21))
        self.job_title_box.setObjectName("job_title_box")
        self.job_title_label = QtWidgets.QLabel(self.centralwidget)
        self.job_title_label.setGeometry(QtCore.QRect(110, 140, 111, 21))
        self.job_title_label.setObjectName("job_title_label")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(200, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet('font: 18pt ".AppleSystemUIFont";')
        self.title.setObjectName("title")
        self.disclaimer_label = QtWidgets.QLabel(self.centralwidget)
        self.disclaimer_label.setGeometry(QtCore.QRect(200, 40, 211, 21))
        self.disclaimer_label.setObjectName("disclaimer_label")
        self.company_box = QtWidgets.QLineEdit(self.centralwidget)
        self.company_box.setGeometry(QtCore.QRect(260, 180, 201, 21))
        self.company_box.setObjectName("company_box")
        self.company_label = QtWidgets.QLabel(self.centralwidget)
        self.company_label.setGeometry(QtCore.QRect(110, 180, 111, 21))
        self.company_label.setObjectName("company_label")
        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setGeometry(QtCore.QRect(100, 560, 113, 32))
        self.generate_button.setObjectName("generate_button")
        self.application_url_box = QtWidgets.QLineEdit(self.centralwidget)
        self.application_url_box.setGeometry(QtCore.QRect(260, 220, 201, 21))
        self.application_url_box.setObjectName("application_url_box")
        self.application_url_label = QtWidgets.QLabel(self.centralwidget)
        self.application_url_label.setGeometry(QtCore.QRect(110, 220, 111, 21))
        self.application_url_label.setObjectName("application_url_label")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(230, 560, 113, 32))
        self.cancel_button.setObjectName("cancel_button")
        self.skills_label = QtWidgets.QLabel(self.centralwidget)
        self.skills_label.setGeometry(QtCore.QRect(110, 260, 111, 21))
        self.skills_label.setObjectName("skills_label")
        self.skills_table = QtWidgets.QTableWidget(self.centralwidget)
        self.skills_table.setGeometry(QtCore.QRect(260, 260, 201, 261))
        self.skills_table.setRowCount(25)
        self.skills_table.setColumnCount(1)
        self.skills_table.setObjectName("skills_table")
        self.skills_table.horizontalHeader().setVisible(False)
        self.skills_table.horizontalHeader().setDefaultSectionSize(200)
        self.skills_table.verticalHeader().setVisible(False)
        self.skills_table.verticalHeader().setDefaultSectionSize(24)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Optimizer"))
        self.job_title_label.setText(_translate("MainWindow", "Job Title:"))
        self.title.setText(_translate("MainWindow", "Job Application Helper"))
        self.disclaimer_label.setText(
            _translate("MainWindow", "Make your life less of a nightmare")
        )
        self.company_label.setText(_translate("MainWindow", "Company:"))
        self.generate_button.setText(_translate("MainWindow", "Generate"))
        self.application_url_label.setText(_translate("MainWindow", "Application URL:"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.skills_label.setText(_translate("MainWindow", "Desired skills:"))
