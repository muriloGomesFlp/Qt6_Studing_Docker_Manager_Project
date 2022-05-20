import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

from src.view.template.windowTemplate import WindowTemplate

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowTemplate()
    win.show()
    sys.exit(app.exec())
