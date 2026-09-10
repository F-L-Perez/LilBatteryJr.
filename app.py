from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

#testing pythonguis.com
#command line  import below
import sys

class fullMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lil Battery Jr")
        button = QPushButton("Check Battery Level!")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)

        self.setMinimumSize(QSize(426,240))
        self.setMaximumSize(QSize(1920, 1080))
        #set central widget of window
        self.setCentralWidget(button)
    def button_clicked(self):
        print("clicked!")

#one Qapplication per app instance, below calls command line
app = QApplication(sys.argv)

# the window widget
window = fullMainWindow()
window.show() #why are windows hidden by default tho?

app.exec()

