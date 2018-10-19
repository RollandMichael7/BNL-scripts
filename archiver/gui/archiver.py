# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtTest
from arvpyf import mgmt, cf
from arvpyf.mgmt import ArchiverConfig
from arvpyf.cf import PVFinder
import json

class TextStream(QtCore.QObject):
    text = QtCore.pyqtSignal(str)
    def write(self, s):
        self.text.emit(str(s))

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 60, 601, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 190, 601, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 240, 601, 311))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        sys.stdout = TextStream(text=self.outputText)
        self.pushButton.clicked.connect(self.listPVs)
        self.pushButton_2.clicked.connect(self.validate)
        self.textEdit.setReadOnly(True)
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PV Archiver"))
        self.label.setText(_translate("MainWindow", "Archiver URL"))
        self.label_2.setText(_translate("MainWindow", "PV Regex"))
        self.pushButton.setText(_translate("MainWindow", "List PVs"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete PVs"))
        self.lineEdit.setText(_translate("MainWindow", "http://xf10id-ca1.cs.nsls2.local:17665/mgmt/bpl"))

        
    def outputText(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()


    def validate(self):
        msg = QtWidgets.QMessageBox
        resp = msg.question(self, '', 'Are you sure you wish to delete these PVs from the archive??', msg.Yes | msg.No)
        if resp == msg.Yes:
            self.deletePVs()
        
    def listPVs(self):
        self.textEdit.setPlainText("")
        url = self.lineEdit.text()
        reg = self.lineEdit_2.text()
        if url == "" or reg == "":
            print("Arguments required: (1) URL for webapp and (2) regex for PVs to list")
            return
        print("webapp URL: " + url)
        print("PV regex: " + reg + "\n")
       
        arvconf = ArchiverConfig(url)
        pvs = arvconf.get_all_pvs(regex=reg, limit=30000)
        if len(pvs) == 0:
            print("No PVs matched the regex.")
            return
        for pv in pvs:
            print(pv)
        print("\n" + str(len(pvs)) + " PVs matched.")

    def deletePVs(self):
        self.textEdit.setPlainText("")
        print("\t\t-----DELETING PVs-----\n")
        url = self.lineEdit.text()
        reg = self.lineEdit_2.text()
        if url == "" or reg == "":
            print("Arguments required: (1) URL for webapp and (2) regex for PVs to list")
            return
        print("webapp URL: " + url)
        print("PV regex: " + reg + "\n")
        
        arvconf = ArchiverConfig(url)
        pvs = arvconf.get_all_pvs(regex=reg, limit=30000)
        if len(pvs) == 0:
            print("No PVs matched the regex.")
            return
        for pv in pvs:
            print(pv)
        paused_pvs = arvconf.pause_archiving_pvs(pvs)
        print(str(len(pvs)) + " PVs paused.")
        print("waiting 30 seconds before deleting...")

        QtTest.QTest.qWait(30000)

        for i, pv in enumerate(pvs):
            resp = arvconf.delete_pv(pv, deleteData=True)
            print(json.dumps(resp))

        print("\nOperation complete.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

