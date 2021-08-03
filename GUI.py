import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QComboBox, QVBoxLayout, QTabWidget, QFileDialog
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
import MainMonitor

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Webpage Monitor Alert Alpha 0.2'
        self.left = 10
        self.top = 10
        self.width = 380
        self.height = 740
        self.initUI()
        self.table_widget = Tabs_Widget(self)
        self.setCentralWidget(self.table_widget)
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)




class Tabs_Widget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Run Monitor")
        self.tabs.addTab(self.tab2,"Settings")
        
        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.run_monitor_widget = Run_Monitor(self)
        self.tab1.layout.addWidget(self.run_monitor_widget)
        self.tab1.setLayout(self.tab1.layout)

        # Create second tab
        self.tab2.layout = QVBoxLayout(self)
        self.settings_widget = Settings_Widget(self)
        self.tab2.layout.addWidget(self.settings_widget)
        self.tab2.setLayout(self.tab2.layout)
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class Run_Monitor(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        #Part select settings
        y_coordinate = 10
        selected_settings = QLabel('Selected settings:', self)
        selected_settings.move(20, y_coordinate)
        selected_settings.resize(300, 40)
        selected_settings.setFont(QFont('Arial', 14))

        self.textbox_selected_settings = QLineEdit(self)
        self.textbox_selected_settings.move(20, y_coordinate + 30)
        self.textbox_selected_settings.resize(300, 30)
        self.textbox_selected_settings.setText("Select a settings file")
        self.textbox_selected_settings.setReadOnly(True)
        select_settings_button = QPushButton(self)
        select_settings_button.setText("Select settings file")
        select_settings_button.move(20, y_coordinate + 65)
        select_settings_button.resize(140, 20)
        select_settings_button.clicked.connect(self.select_settings_file)

        #Part show selected settings
        show_settings_button = QPushButton(self)
        show_settings_button.setText("Show current settings")
        show_settings_button.move(165, y_coordinate + 65)
        show_settings_button.resize(155, 20)

    def select_settings_file(self):
        self.openFileNameDialog()
        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            global selected_file_name 
            selected_file_name = fileName
            print(selected_file_name)
        self.textbox_selected_settings.setText(selected_file_name)





class Settings_Widget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        #Part A
        y_coordinateA = 10
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
        labelE = QLabel('Delay time', self)
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
        self.button = QPushButton('Save Settings', self)
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
        errors_num = 0

        #Try URL
        try:
            URL_to_monitor = str(self.textboxURL.text())
        except:
            self.settings_enter_error(0)
            self.textboxURL.setText("")
            errors_num += 1

        #Try Recipient Mail
        try:
            Recipient_Emails = []
            Recipient_Emails.append(str(self.textboxMailReci.text()))
        except:
            self.settings_enter_error(1)
            self.textboxMailReci.setText("")
            errors_num += 1

        #Try Sending Email
        try:
            Send_Email = str(self.textboxMailSend.text())
        except:
            self.settings_enter_error(2)
            self.textboxMailSend.setText("")
            errors_num += 1

        #Try Sending Email Password
        try:
            Send_Email_Password = str(self.textboxMailSendPw.text())
        except:
            self.settings_enter_error(3)
            self.textboxMailSendPw.setText("")
            errors_num += 1

        #Try Delay Time
        try:
            Delay = int(self.textboxDelay.text())
        except:
            self.settings_enter_error(4)
            self.textboxDelay.setText("")
            errors_num += 1

        #Try Start and Stop time
        Start_Stop_time = bool(self.TimeBox.currentIndex())
        print(Start_Stop_time)
        print(self.TimeBox.currentIndex())
        if Start_Stop_time:
            try:
                Start_time_int = float(self.textboxStartTime.text())
            except:
                self.settings_enter_error(6)
                errors_num += 1
            try:
                Stop_time_int = float(self.textboxStopTime.text())
            except:
                self.settings_enter_error(7)
                errors_num += 1
        else:
            Start_time_int = 0
            Stop_time_int = 0

        #Try LED status
        try:
            LED_status = bool(self.LEDBox.currentText())
        except:
            LED_status = False

        if bool(errors_num) != True:
            MainMonitor.main(URL_to_monitor, Recipient_Emails, Send_Email, Send_Email_Password, Start_Stop_time, Start_time_int, Stop_time_int, Delay, LED_status)
        else:
            return 0



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
