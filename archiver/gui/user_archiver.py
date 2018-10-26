# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'archiver.ui'
#
# Created: Fri Oct 19 16:31:40 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from arvpyf import mgmt, cf
from arvpyf.mgmt import ArchiverConfig
from arvpyf.cf import PVFinder
import json
import os
        
class TextStream(QtCore.QObject):
    text = QtCore.pyqtSignal(str)
    def write(self, s):
        self.text.emit(str(s))

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 963)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 1031, 92))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.urlLine = QtWidgets.QLineEdit(self.layoutWidget)
        self.urlLine.setObjectName("urlLine")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.urlLine)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.regexLine = QtWidgets.QLineEdit(self.layoutWidget)
        self.regexLine.setObjectName("regexLine")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.regexLine)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 170, 1031, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.listButton.setObjectName("listButton")
        self.horizontalLayout.addWidget(self.listButton)
        self.archiveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.archiveButton.setObjectName("archiveButton")
        self.horizontalLayout.addWidget(self.archiveButton)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 450, 1031, 371))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 220, 1031, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.detailsButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.detailsButton.setObjectName("detailsButton")
        self.horizontalLayout_3.addWidget(self.detailsButton)
        self.typeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.typeButton.setObjectName("typeButton")
        self.horizontalLayout_3.addWidget(self.typeButton)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 390, 1031, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.getpauseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.getpauseButton.setObjectName("getpauseButton")
        self.horizontalLayout_2.addWidget(self.getpauseButton)
        self.neverconnectedButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.neverconnectedButton.setObjectName("neverconnectedButton")
        self.horizontalLayout_2.addWidget(self.neverconnectedButton)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 270, 1031, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.statusButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.statusButton.setObjectName("statusButton")
        self.horizontalLayout_4.addWidget(self.statusButton)
        self.abortButon = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.abortButon.setObjectName("abortButon")
        self.horizontalLayout_4.addWidget(self.abortButon)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 320, 1031, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pauseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_5.addWidget(self.pauseButton)
        self.resumeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.resumeButton.setObjectName("resumeButton")
        self.horizontalLayout_5.addWidget(self.resumeButton)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 830, 111, 16))
        self.label_3.setObjectName("label_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 850, 1031, 24))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.searchEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout_6.addWidget(self.searchEdit)
        self.searchButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_6.addWidget(self.searchButton)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(410, 890, 211, 22))
        self.saveButton.setObjectName("saveButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 151, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 130, 121, 31))
        self.label_5.setObjectName("label_5")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(230, 130, 171, 31))
        self.doubleSpinBox.setMinimum(.100000)
        self.doubleSpinBox.setMaximum(10000.0)
        self.doubleSpinBox.setValue(1.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(530, 130, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(460, 130, 59, 31))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        sys.stdout = TextStream(text=self.outputText)
        self.textEdit.setReadOnly(True)
        self.searchButton.clicked.connect(self.searchOutput)
        self.saveButton.clicked.connect(self.saveOutput)
        self.listButton.clicked.connect(self.listPVs)
        self.statusButton.clicked.connect(self.statPVs)
        self.typeButton.clicked.connect(self.typeInfoPVs)
        self.neverconnectedButton.clicked.connect(self.neverConnectedPVs)
        self.detailsButton.clicked.connect(self.detailPVs)
        self.getpauseButton.clicked.connect(self.getPausedPVs)
        self.archiveButton.clicked.connect(self.archivePVs)
        self.pauseButton.clicked.connect(self.pausePVs)
        self.resumeButton.clicked.connect(self.resumePVs)
        self.abortButon.clicked.connect(self.abortPVs)

        self.hlFormat = QtGui.QTextCharFormat()
        self.hlFormat.setBackground(QtGui.QBrush(QtGui.QColor("yellow")))

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PV Archiver Appliance"))
        self.label.setText(_translate("MainWindow", "Archiver URL"))
        self.label_2.setText(_translate("MainWindow", "PV Regex"))
        self.listButton.setText(_translate("MainWindow", "List PVs"))
        self.archiveButton.setText(_translate("MainWindow", "Archive PVs"))
        self.detailsButton.setText(_translate("MainWindow", "Get PV Details"))
        self.typeButton.setText(_translate("MainWindow", "Get PV Type Info"))
        self.getpauseButton.setText(_translate("MainWindow", "Get Paused PVs"))
        self.neverconnectedButton.setText(_translate("MainWindow", "Get Never Connected PVs"))
        self.statusButton.setText(_translate("MainWindow", "Get Archiving Status"))
        self.abortButon.setText(_translate("MainWindow", "Abort Archiving PVs"))
        self.pauseButton.setText(_translate("MainWindow", "Pause Archiving PVs"))
        self.resumeButton.setText(_translate("MainWindow", "Resume Archiving PVs"))
        self.label_3.setText(_translate("MainWindow", "Search output"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.saveButton.setText(_translate("MainWindow", "Save output to file"))
        self.label_4.setText(_translate("MainWindow", "Archiving Parameters"))
        self.label_5.setText(_translate("MainWindow", "Period (seconds)"))
        self.comboBox.setItemText(0, _translate("MainWindow", "SCAN"))
        self.comboBox.setItemText(1, _translate("MainWindow", "MONITOR"))
        self.label_6.setText(_translate("MainWindow", "Method"))
        self.urlLine.setText(_translate("MainWindow", "http://xf10id-ca1.cs.nsls2.local:17665/mgmt/bpl"))


    def outputText(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()


    def searchOutput(self):
        cursor = self.textEdit.textCursor()
        cursor.select(QtGui.QTextCursor.Document)
        cursor.setCharFormat(QtGui.QTextCharFormat())
        pattern = self.searchEdit.text()
        if pattern == "":
            return
        regex = QtCore.QRegExp(pattern)
        # regex.setPatternSyntax(QtCore.QRegExp.FixedString)
        pos = 0
        index = regex.indexIn(self.textEdit.toPlainText(), pos)
        while (index != -1):
            pos = index + regex.matchedLength()
            cursor.setPosition(index)
            #sys.stderr.write("old index: " + str(cursor.position()) + "\n")
            #sys.stderr.write("pos: " + str(pos) + "\n")
            while (cursor.position() != pos):
                    cursor.movePosition(QtGui.QTextCursor.Right, 1)
            #sys.stderr.write("new index: " + str(cursor.position()) + "\n")
            cursor.mergeCharFormat(self.hlFormat)
            index = regex.indexIn(self.textEdit.toPlainText(), pos)


    def saveOutput(self):
        filename, ok = QtWidgets.QInputDialog.getText(self, 'File name', 'Enter name of file to be created:')
        if not ok:
            return
        path = os.path.join(os.getcwd(), filename)
        if (os.path.isfile(filename)):
            msg = QtWidgets.QMessageBox
            resp = msg.question(self, '', 'That file already exists. Overwrite?', msg.Yes | msg.No)
            if resp == msg.No:
                return
        f = open(path, "w")
        for line in self.textEdit.toPlainText():
            f.write(line)
        print("\nSaved to " + path)
            
        
    def validate(self, needsRegex):
        self.textEdit.setPlainText("")
        url = self.urlLine.text()
        reg = self.regexLine.text()
        if url == "" or (reg == "" and needsRegex):
            if needsRegex:
                print("Arguments required: (1) URL for webapp and (2) regular expression for matching PV names")
            else:
                print("Argument required: (1) URL for webapp")
            return None
        print("webapp URL: " + url)
        arvconf = ArchiverConfig(url)
        if needsRegex:
            print("PV regex: " + reg + "\n")
            pvs = arvconf.get_all_pvs(regex=reg, limit=30000)
        else:
            pvs = [0]
        if len(pvs) == 0 and needsRegex:
            print("No PVs matched the regex.")
            return None
        return arvconf, pvs

    
    def printJSON(self, json):
        for key in json.keys():
            print(key + " : " + str(json[key]))
        print("\n", end="")


    def listPVs(self):
        arvconf, pvs = self.validate(True)
        if arvconf is None:
            return
        for pv in pvs:
            print(pv)
        print("\n" + str(len(pvs)) + " PVs matched.")


    def statPVs(self):
        arvconf, pvs = self.validate(True)
        if arvconf is None:
            return
        results = arvconf.get_pv_status(pvs=pvs)
        for json in results:
            self.printJSON(json)
        print("\n" + str(len(pvs)) + " PVs matched.")

    
    def typeInfoPVs(self):
        arvconf, pvs = self.validate(True)
        if arvconf is None:
            return
        for pv in pvs:
            json = arvconf.get_pv_type_info(pv)
            print(pv)
            self.printJSON(json)
        print(str(len(pvs)) + " PVs matched.")
            

    def neverConnectedPVs(self):
        arvconf, pvs = self.validate(False)
        if arvconf is None:
            return
        results = arvconf.get_never_connected_pvs()
        for json in results:
            self.printJSON(json)
        print("\n", end="")
        print(str(len(results)) + " PVs never connected.")

        
    def detailPVs(self):
        arvconf, pvs = self.validate(True)
        if arvconf is None:
            return
        for pv in pvs:
            jsons = arvconf.get_pv_details(pv)
            #self.printJSON(json)
            #print(pv)
            for json in jsons:
                #self.printJSON(i)
                print(json["name"] + ": " + str(json["value"]) + " (source: " + json["source"] + ")")
            print("\n", end="")
        print(str(len(pvs)) + " PVs matched.")


    def getPausedPVs(self):
        arvconf, pvs = self.validate(False)
        if arvconf is None:
            return
        paused = arvconf.get_paused_pvs_report()
        for pv in paused:
            print(pv)
        print("\n", end="")
        print(str(len(paused)) + " PVs currently paused.")


    def archivePVs(self):
        arvconf, pvs = self.validate(True)
        if arvconf is None:
            return
        method = str(self.comboBox.currentText())
        period = self.doubleSpinBox.value()
        msg = QtWidgets.QMessageBox
        resp = msg.question(self, 'Archive PVs', 'You are attempting to archive ' + str(len(pvs)) + ' PVs.\n\n' +
                'The archive parameters are:\n PERIOD: ' + str(period) + ' second(s) \n ' +
                'METHOD: ' + method + ' \n POLICY: "Default" \n\n Use these parameters?', msg.Yes | msg.No)
        if resp == msg.No:
            print("Operation aborted.")
            return
        results = arvconf.archive_pvs(pvnames=pvs, method=method, period=period)
        for json in results:
            self.printJSON(json)

            
    def pausePVs(self):
        arvconf, pvs = self.validate(True)
        if arvconf is None:
            return
        msg = QtWidgets.QMessageBox
        resp = msg.question(self, 'Pause PVs', "You are attempting to pause " + str(len(pvs)) + "PVs. Continue?")
        if resp == msg.No:
            print("Operation aborted.")
            return
        paused = arvconf.pause_archiving_pvs(pvs)
        for pv in paused:
            print(pv + " paused.")
        print("\n", end="")
        print(str(len(paused)) + " PVs paused.")


    def resumePVs(self):
        arvconf, pvs = self.validate(True)
        if arvconf is None:
            return
        results = arvconf.resume_archiving_pvs(pvs)
        n = len(results)
        for json in results:
            if 'not paused' in json['validation']:
                n = n - 1
            self.printJSON(json)
        print(str(n) + " PVs resumed.")


    def abortPVs(self):
        arvconf, pvs = self.validate(True)
        if arvconf is None:
            return
        msg = QtWidgets.QMessageBox
        resp = msg.question(self, 'Abort PVs', "You are attempting to abort archiving " + str(len(pvs)) + "PVs. Continue?")
        if resp == msg.No:
            print("Operation aborted.")
            return
        for pv in pvs:
            json = arvconf.abort_archiving_pv(pv)
            self.printJSON(json)
        print(str(len(pvs)) + " PVs aborted.")
            
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

