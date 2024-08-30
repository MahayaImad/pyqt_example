from PyQt6.QtWidgets import QApplication, QMainWindow
from index import Ui_MainWindow  # Replace Ui_MainWindow with the class name from your .ui file

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
