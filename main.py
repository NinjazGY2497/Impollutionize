from PySide6.QtWidgets import QApplication
from widgets import Widget

app = QApplication()

window = Widget()
window.show()

app.exec()