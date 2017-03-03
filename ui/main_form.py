from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QWidget, QVBoxLayout, QLabel
import sys


class MainForm(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        v_box_layout = QVBoxLayout()
        v_box_layout.addWidget(QLabel("Hello World"))
        self.setLayout(v_box_layout)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(application.exec_())
