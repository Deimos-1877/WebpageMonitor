import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QComboBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Webpage Monitor Alert'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 800
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        labelTitle = QLabel('Webpage Monitor pre-Alpha', self)
        labelTitle.move(20, 2)
        labelTitle.resize(400, 40)
        labelTitle.setFont(QFont("Times", 20, QFont.Bold))

        #Part A
        y_coordinateA = 40
        labelA = QLabel('URL to monitor', self)
        labelA.move(20, y_coordinateA)
        labelA.resize(280, 40)

        self.textboxURL = QLineEdit(self)
        self.textboxURL.move(20, y_coordinateA + 30)
        self.textboxURL.resize(300, 30)


        #Part B
        y_coordinateB = y_coordinateA + 65
        labelB = QLabel('Email to alert', self)
        labelB.move(20, y_coordinateB)
        labelB.resize(280, 40)

        self.textboxMailReci = QLineEdit(self)
        self.textboxMailReci.move(20, y_coordinateB + 30)
        self.textboxMailReci.resize(300, 30)


        #Part C
        y_coordinateC = y_coordinateB + 65
        labelC = QLabel('Email to send alert', self)
        labelC.move(20, y_coordinateC)
        labelC.resize(280, 40)

        self.textboxMailSend = QLineEdit(self)
        self.textboxMailSend.move(20, y_coordinateC + 30)
        self.textboxMailSend.resize(300, 30)


        #Part D
        y_coordinateD = y_coordinateC + 65
        labelD = QLabel('Password to email', self)
        labelD.move(20, y_coordinateD)
        labelD.resize(280, 40)

        self.textboxMailSendPw = QLineEdit(self)
        self.textboxMailSendPw.move(20, y_coordinateD + 30)
        self.textboxMailSendPw.resize(300, 30)


        #Part E
        y_coordinateE = y_coordinateD + 65
        labelE = QLabel('Dealy time', self)
        labelE.move(20, y_coordinateE)
        labelE.resize(280, 40)

        self.textboxDelay = QLineEdit(self)
        self.textboxDelay.move(20, y_coordinateE + 30)
        self.textboxDelay.resize(300, 30)


        #Part F
        y_coordinateF = y_coordinateE +65
        labelF = QLabel('With start and stop time', self)
        labelF.move(20, y_coordinateF)
        labelF.resize(280, 40)
        self.TimeBox = QComboBox(self)
        self.TimeBox.addItem("False")
        self.TimeBox.addItem("True")
        self.TimeBox.move(20, y_coordinateF + 30)

        #Part G
        y_coordinateG = y_coordinateF + 65
        labelG = QLabel('Start time ', self)
        labelG.move(20, y_coordinateG)
        labelG.resize(280, 40)

        self.textboxStartTime = QLineEdit(self)
        self.textboxStartTime.move(20, y_coordinateG + 30)
        self.textboxStartTime.resize(300, 30)


        #Part H
        y_coordinateH = y_coordinateG + 65
        labelH = QLabel('Stop time', self)
        labelH.move(20, y_coordinateH)
        labelH.resize(280, 40)

        self.textboxStopTime = QLineEdit(self)
        self.textboxStopTime.move(20, y_coordinateH + 30)
        self.textboxStopTime.resize(300, 30)


        #Part I
        y_coordinateI = y_coordinateH + 65
        labelI = QLabel('With LED (for raspberry Pi)', self)
        labelI.move(20, y_coordinateI)
        labelI.resize(280, 40)
        self.LEDBox = QComboBox(self)
        self.LEDBox.addItem("False")
        self.LEDBox.addItem("True")
        self.LEDBox.move(20, y_coordinateI + 30)

        #Change settings button
        self.button = QPushButton('Start monitor', self)
        self.button.move(20, y_coordinateI + 85)
        self.button.resize(120, 20)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    def settings_enter_error(self, error_code):
        error_messages = ["Please enter a URL", "Please enter a Recipient Mail", "Please enter an Email to send the alerts from", "Please enter the password for the Email to send the alerts from", "Please enter an integer into Delay time", "Please enter if you have a start/stop time", "Please enter a valid start time", "Please enter a valid stop time"]
        string_error_code = str(error_code)
        QMessageBox.question(self, 'Error' + string_error_code, error_messages[error_code], QMessageBox.Ok,
                             QMessageBox.Ok)

    @pyqtSlot()
    def on_click(self):
        #Try URL
        try:
            URL_to_monitor = str(self.textboxURL.text())
        except:
            self.settings_enter_error(0)
            self.textboxURL.setText("")
        #Try Recipient Mail
        try:
            Recipient_Email = str(self.textboxMailReci.text())
        except:
            self.settings_enter_error(1)
            self.textboxMailReci.setText("")

        #Try Sending Email
        try:
            Send_Email = str(self.textboxMailSend.text())
        except:
            self.settings_enter_error(2)
            self.textboxMailSend.setText("")

        #Try Sending Email Password
        try:
            Send_Email_Password = str(self.textboxMailSendPw.text())
        except:
            self.settings_enter_error(3)
            self.textboxMailSendPw.setText("")

        #Try Delay Time
        try:
            Delay = int(self.textboxDelay.text())
        except:
            self.settings_enter_error(4)
            self.textboxDelay.setText("")

        #Try Start and Stop time
        Start_Stop_time = bool(self.TimeBox.currentIndex())
        print(Start_Stop_time)
        print(self.TimeBox.currentIndex())
        if Start_Stop_time:
            try:
                Start_time = float(self.textboxStartTime.text())
            except:
                self.settings_enter_error(6)
            try:
                Stop_time = float(self.textboxStopTime.text())
            except:
                self.settings_enter_error(7)

        #Try LED status
        try:
            LED_status = bool(self.LEDBox.currentText())
        except:
            LED_status = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
