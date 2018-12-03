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
import requests
        
class TextStream(QtCore.QObject):
    text = QtCore.pyqtSignal(str)
    def write(self, s):
        self.text.emit(str(s))

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 1043)
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
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 540, 1031, 361))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 910, 111, 16))
        self.label_3.setObjectName("label_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 930, 1031, 24))
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
        self.saveButton.setGeometry(QtCore.QRect(410, 970, 211, 22))
        self.saveButton.setObjectName("saveButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 151, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 120, 121, 31))
        self.label_5.setObjectName("label_5")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(330, 120, 171, 31))
        self.doubleSpinBox.setMaximum(10000.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(700, 120, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(630, 120, 59, 31))
        self.label_6.setObjectName("label_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 160, 1031, 371))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(10, 0, 1001, 341))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listButton = QtWidgets.QPushButton(self.widget)
        self.listButton.setObjectName("listButton")
        self.horizontalLayout.addWidget(self.listButton)
        self.archiveButton = QtWidgets.QPushButton(self.widget)
        self.archiveButton.setObjectName("archiveButton")
        self.horizontalLayout.addWidget(self.archiveButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.detailsButton = QtWidgets.QPushButton(self.widget)
        self.detailsButton.setObjectName("detailsButton")
        self.horizontalLayout_3.addWidget(self.detailsButton)
        self.typeButton = QtWidgets.QPushButton(self.widget)
        self.typeButton.setObjectName("typeButton")
        self.horizontalLayout_3.addWidget(self.typeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.statusButton = QtWidgets.QPushButton(self.widget)
        self.statusButton.setObjectName("statusButton")
        self.horizontalLayout_4.addWidget(self.statusButton)
        self.abortButon = QtWidgets.QPushButton(self.widget)
        self.abortButon.setObjectName("abortButon")
        self.horizontalLayout_4.addWidget(self.abortButon)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pauseButton = QtWidgets.QPushButton(self.widget)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_5.addWidget(self.pauseButton)
        self.resumeButton = QtWidgets.QPushButton(self.widget)
        self.resumeButton.setObjectName("resumeButton")
        self.horizontalLayout_5.addWidget(self.resumeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.getpauseButton = QtWidgets.QPushButton(self.widget)
        self.getpauseButton.setObjectName("getpauseButton")
        self.horizontalLayout_2.addWidget(self.getpauseButton)
        self.neverconnectedButton = QtWidgets.QPushButton(self.widget)
        self.neverconnectedButton.setObjectName("neverconnectedButton")
        self.horizontalLayout_2.addWidget(self.neverconnectedButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 0, 1001, 341))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(503, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.dataStoreButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.dataStoreButton.setObjectName("dataStoreButton")
        self.horizontalLayout_7.addWidget(self.dataStoreButton)
        self.applianceInfoButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.applianceInfoButton.setObjectName("applianceInfoButton")
        self.horizontalLayout_7.addWidget(self.applianceInfoButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.activeAppliancesButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.activeAppliancesButton.setObjectName("activeAppliancesButton")
        self.horizontalLayout_8.addWidget(self.activeAppliancesButton)
        self.moveButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.moveButton.setObjectName("moveButton")
        self.horizontalLayout_8.addWidget(self.moveButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.addAliasButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.addAliasButton.setObjectName("addAliasButton")
        self.horizontalLayout_9.addWidget(self.addAliasButton)
        self.removeAliasButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.removeAliasButton.setObjectName("removeAliasButton")
        self.horizontalLayout_9.addWidget(self.removeAliasButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.applianceVersionButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.applianceVersionButton.setObjectName("applianceVersionButton")
        self.horizontalLayout_10.addWidget(self.applianceVersionButton)
        self.getAppliancePVsButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.getAppliancePVsButton.setObjectName("getAppliancePVsButton")
        self.horizontalLayout_10.addWidget(self.getAppliancePVsButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
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

        self.dataStoreButton.clicked.connect(self.getDataStores)
        self.applianceInfoButton.clicked.connect(self.getApplianceInfo)
        self.activeAppliancesButton.clicked.connect(self.getActiveAppliances)

        self.hlFormat = QtGui.QTextCharFormat()
        self.hlFormat.setBackground(QtGui.QBrush(QtGui.QColor("yellow")))

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PV Archiver Appliance"))
        self.label.setText(_translate("MainWindow", "Archiver URL"))
        self.label_2.setText(_translate("MainWindow", "PV Regex"))
        self.label_3.setText(_translate("MainWindow", "Search output"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.saveButton.setText(_translate("MainWindow", "Save output to file"))
        self.label_4.setText(_translate("MainWindow", "Archiving Paramters"))
        self.label_5.setText(_translate("MainWindow", "Period (seconds)"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MONITOR"))
        self.comboBox.setItemText(1, _translate("MainWindow", "SCAN"))
        self.label_6.setText(_translate("MainWindow", "Method"))
        self.listButton.setText(_translate("MainWindow", "List PVs"))
        self.archiveButton.setText(_translate("MainWindow", "Archive PVs"))
        self.detailsButton.setText(_translate("MainWindow", "Get PV Details"))
        self.typeButton.setText(_translate("MainWindow", "Get PV Type Info"))
        self.statusButton.setText(_translate("MainWindow", "Get Archiving Status"))
        self.abortButon.setText(_translate("MainWindow", "Abort Archiving PVs"))
        self.pauseButton.setText(_translate("MainWindow", "Pause Archiving PVs"))
        self.resumeButton.setText(_translate("MainWindow", "Resume Archiving PVs"))
        self.getpauseButton.setText(_translate("MainWindow", "Get Paused PVs"))
        self.neverconnectedButton.setText(_translate("MainWindow", "Get Never Connected PVs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "arvpyf functions"))
        self.label_7.setText(_translate("MainWindow", "Appliance "))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Short Term Storage"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Medium Term Storage"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Long Term Storage"))
        self.dataStoreButton.setText(_translate("MainWindow", "Get Data Store Names"))
        self.applianceInfoButton.setText(_translate("MainWindow", "Get Appliance Information"))
        self.activeAppliancesButton.setText(_translate("MainWindow", "Get Active Appliances in Cluster"))
        self.moveButton.setText(_translate("MainWindow", "Move PV to Another Appliance"))
        self.addAliasButton.setText(_translate("MainWindow", "Add Alias to PV"))
        self.removeAliasButton.setText(_translate("MainWindow", "Remove Alias from PV"))
        self.applianceVersionButton.setText(_translate("MainWindow", "Get Appliance Versions"))
        self.getAppliancePVsButton.setText(_translate("MainWindow", "Get PVs for Appliance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "additional functions"))
        self.urlLine.setText(_translate("MainWindow", "http://xf10id-ca1.cs.nsls2.local:17665/mgmt/bpl"))
        self.doubleSpinBox.setValue(1)

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
            return None, None
        print("webapp URL: " + url)
        arvconf = ArchiverConfig(url)
        if needsRegex:
            print("PV regex: " + reg + "\n")
            pvs = arvconf.get_all_pvs(regex=reg, limit=30000)
        else:
            pvs = [0]
        if len(pvs) == 0 and needsRegex:
            print("No PVs matched the regex.")
            return arvconf, None
        return arvconf, pvs

    
    def printJSON(self, json):
        for key in json.keys():
            print(key + " : " + str(json[key]))
        print("\n", end="")


    def listPVs(self):
        arvconf, pvs = self.validate(True)
        if arvconf is None or pvs is None:
            return
        for pv in pvs:
            print(pv)
        print("\n" + str(len(pvs)) + " PVs matched.")


    def statPVs(self):
        arvconf, pvs = self.validate(True)
        if arvconf is None or pvs is None:
            return
        results = arvconf.get_pv_status(pvs=pvs)
        for json in results:
            self.printJSON(json)
        print("\n" + str(len(pvs)) + " PVs matched.")

    
    def typeInfoPVs(self):
        arvconf, pvs = self.validate(True)
        if arvconf is None or pvs is None:
            return
        for pv in pvs:
            json = arvconf.get_pv_type_info(pv)
            print(pv)
            self.printJSON(json)
        print(str(len(pvs)) + " PVs matched.")
            

    def neverConnectedPVs(self):
        arvconf, pvs = self.validate(False)
        if arvconf is None or pvs is None:
            return
        results = arvconf.get_never_connected_pvs()
        for json in results:
            self.printJSON(json)
        print("\n", end="")
        print(str(len(results)) + " PVs never connected.")

        
    def detailPVs(self):
        arvconf, pvs = self.validate(True)
        if arvconf is None or pvs is None:
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
        if arvconf is None or pvs is None:
            return
        paused = arvconf.get_paused_pvs_report()
        for pv in paused:
            print(pv)
        print("\n", end="")
        print(str(len(paused)) + " PVs currently paused.")


    def archivePVs(self):
        arvconf, pvs = self.validate(True)
        noMatch = False
        if arvconf is None:
        	return 
        if pvs is None:
            pvs = self.regexLine.text()
            print("Attempting to archive " + pvs + "\n")
            noMatch = True
        method = str(self.comboBox.currentText())
        period = self.doubleSpinBox.value()
        msg = QtWidgets.QMessageBox
        if noMatch:
        	length = 1
        else:
        	length = len(pvs)
        resp = msg.question(self, 'Archive PVs', 'You are attempting to archive ' + str(length) + ' PVs.\n\n' +
                'The archive parameters are:\n PERIOD: ' + str(period) + ' second(s) \n ' +
                'METHOD: ' + method + ' \n POLICY: "Default" \n\n Use these parameters?', msg.Yes | msg.No)
        if resp == msg.No:
            print("Operation aborted.")
            return
        if noMatch:
        	params = {'pv' : pvs, 'samplingperiod' : period, 'samplingmethod' : method}
        	result = self.getRespJSON('/archivePV', params)
        	print(result)
        else:
	        results = arvconf.archive_pvs(pvnames=pvs, method=method, period=period)
	        for j in results:
	            self.printJSON(j)

            
    def pausePVs(self):
        arvconf, pvs = self.validate(True)
        if arvconf is None or pvs is None:
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
        if arvconf is None or pvs is None:
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
        if arvconf is None or pvs is None:
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

    ############################
    ### non-arvpyf functions ###
    ############################

    def getRespJSON(self, service, params):
        url = self.urlLine.text()
        if url == '':
            return None
        req_url = url + service
        if params is not None:
            req = requests.get(req_url, params=params, stream=True)
        else:
            req = requests.get(req_url, stream=True)
        return req.json()
    
    def getDataStores(self):
        arvconf, pvs = self.validate(True)
        if arvconf is None or pvs is None:
            return
        url = self.urlLine.text()
        pv = pvs[0]
        req_url = url + "/getStoresForPV"
        params = {'pv' : pv}
        req = requests.get(req_url, params=params, stream=True)
        result = req.json()
        print(json.dumps(result))


    def getApplianceInfo(self):
        self.textEdit.setPlainText("")
        text = self.comboBox_2.currentText()
        '''
        if "Long" in text:
            appl = "LTS"
        if "Medium" in text:
            appl = "MTS"
        else:
            appl = "STS"
        params = {'id' : appl}
        '''
        result = self.getRespJSON('/getApplianceInfo', None)
        if result is None:
            return
        #self.textEdit.setPlainText("")
        #self.textEdit.setHtml(result)
        print("appliance ID: " + result['identity'] + "\n")
        self.printJSON(result)


    def getActiveAppliances(self):
        self.textEdit.setPlainText("")
        result = self.getRespJSON('/getAppliancesInCluster', None)
        if result is None:
            return
        for json in result:
            print("appliance ID: " + json['identity'] + "\n")
            self.printJSON(json)
            
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

