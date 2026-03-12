from PySide6.QtWidgets import QApplication
from widgets import HomeWidget, Widget

app = QApplication()

waterWindow = Widget("water")
airWindow = Widget("air")
lightWindow = Widget("light")
homeWindow = HomeWidget(waterWindow, airWindow, lightWindow)
homeWindow.show()

app.exec()