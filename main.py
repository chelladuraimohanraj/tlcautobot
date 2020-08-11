from PyQt5 import QtCore, QtGui, QtWidgets
import bot
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(596, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 10, 171, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.college = QtWidgets.QComboBox(self.centralwidget)
        self.college.setGeometry(QtCore.QRect(30, 80, 86, 25))
        self.college.setEditable(False)
        self.college.setObjectName("college")
        self.college.addItem("")
        self.college.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 67, 17))
        self.label_3.setObjectName("label_3")
        self.year = QtWidgets.QComboBox(self.centralwidget)
        self.year.setGeometry(QtCore.QRect(30, 160, 86, 25))
        self.year.setObjectName("year")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 111, 17))
        self.label_4.setObjectName("label_4")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(30, 240, 181, 31))
        self.username.setText("")
        self.username.setObjectName("username")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 290, 111, 17))
        self.label_5.setObjectName("label_5")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(30, 320, 181, 31))
        self.password.setText("")
        self.password.setObjectName("password")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(60, 380, 89, 25))
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.checkid)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(250, 50, 20, 361))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.displayuser = QtWidgets.QLabel(self.centralwidget)
        self.displayuser.setGeometry(QtCore.QRect(280, 60, 251, 20))
        self.displayuser.setObjectName("displayuser")
        self.courses = QtWidgets.QLabel(self.centralwidget)
        self.courses.setGeometry(QtCore.QRect(280, 100, 241, 17))
        self.courses.setObjectName("courses")
        self.selectedcoarse = QtWidgets.QComboBox(self.centralwidget)
        self.selectedcoarse.setGeometry(QtCore.QRect(280, 140, 191, 25))
        self.selectedcoarse.setObjectName("selectedcoarse")
        self.selectedcoarse.addItem("")
        self.solve = QtWidgets.QPushButton(self.centralwidget)
        self.solve.setGeometry(QtCore.QRect(280, 190, 89, 25))
        self.solve.setObjectName("solve")
        self.solve.clicked.connect(self.solving)
        self.terminal = QtWidgets.QTextBrowser(self.centralwidget)
        self.terminal.setGeometry(QtCore.QRect(280, 241, 301, 171))
        self.terminal.setObjectName("terminal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TLC AUTO BOT"))
        self.college.setCurrentText(_translate("MainWindow", "krct"))
        self.college.setItemText(0, _translate("MainWindow", "krct"))
        self.college.setItemText(1, _translate("MainWindow", "krce"))
        self.label_2.setText(_translate("MainWindow", "College:"))
        self.label_3.setText(_translate("MainWindow", "Year:"))
        self.year.setItemText(0, _translate("MainWindow", "1"))
        self.year.setItemText(1, _translate("MainWindow", "2"))
        self.year.setItemText(2, _translate("MainWindow", "3"))
        self.year.setItemText(3, _translate("MainWindow", "4"))
        self.year.setItemText(4, _translate("MainWindow", "faculty"))
        self.label_4.setText(_translate("MainWindow", "TLC Username:"))
        self.label_5.setText(_translate("MainWindow", "TLC Password:"))
        self.submit.setText(_translate("MainWindow", "SUBMIT"))
        self.displayuser.setText(_translate("MainWindow", "Account name:"))
        self.courses.setText(_translate("MainWindow", "Select coarse to solve:"))
        self.selectedcoarse.setItemText(0, _translate("MainWindow", "None"))
        self.solve.setText(_translate("MainWindow", "Solve"))


    def checkid(self):
        self.c=str(self.college.currentText())
        self.y=str(self.year.currentText())
        self.u=str(self.username.text())
        self.p=str(self.password.text())
        
        if self.u=='' or self.p=='':
            self.terminal.setText('Please enter all the details')
        
        else:
            
            self.autobot=bot.solveproblems()
            self.autobot.setyear(self.c,self.y)
            found,result=self.autobot.checkuser(self.u,self.p)
            if found:
                self.terminal.setText(result)
                self.courses=self.autobot.getcourses()
                self.displayuser.setText(result)
                for i in self.courses:
                    self.selectedcoarse.addItem(str(i.text))
                if len(self.courses)>1:
                    self.selectedcoarse.addItem('All')
                
                self.terminal.setText('Please select coarse and enter solve')
                   
            else:
                self.terminal.setText(result)
                self.autobot.driver.quit()
            

    def solving(self):
        
        self.current=(self.selectedcoarse.currentText())
        if self.current=='All':
            self.autobot.solveall()
        else:
            out=self.autobot.solvecourse(self.current)
            self.terminal.setText(f'{out}\nThank you')
               
            

        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
