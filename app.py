from PyQt6.QtWidgets import QApplication, QWidget

#testing pythonguis.com
#command line  import below
import sys


#one Qapplication per app instance, below calls command line
app = QApplication(sys.argv)

# the window widget
window = QWidget()
window.show() #why are windows hidden by default tho?

app.exec()

