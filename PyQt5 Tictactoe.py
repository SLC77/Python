##############
### IMPORT ###
##############

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

app = QApplication(sys,argv)
window = QWidget()
window.setWindowTitle('Hello world')
window.setGeometry(100, 100, 640, 480)
window.show()
sys.exit(app.exec_())
