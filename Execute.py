import GUI
import MainMonitor
import sys

if __name__ == '__main__':
    app = GUI.QApplication(sys.argv)
    ex = GUI.App()
    sys.exit(app.exec_())