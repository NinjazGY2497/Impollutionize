# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_homeWidget(object):
    def setupUi(self, homeWidget):
        if not homeWidget.objectName():
            homeWidget.setObjectName(u"homeWidget")
        homeWidget.resize(530, 232)
        self.verticalLayout_2 = QVBoxLayout(homeWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(homeWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"DejaVu Serif"])
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.waterButton = QPushButton(homeWidget)
        self.waterButton.setObjectName(u"waterButton")
        icon = QIcon()
        icon.addFile(u":/Images/water banner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.waterButton.setIcon(icon)
        self.waterButton.setIconSize(QSize(500, 50))

        self.verticalLayout_2.addWidget(self.waterButton)

        self.airButton = QPushButton(homeWidget)
        self.airButton.setObjectName(u"airButton")
        icon1 = QIcon()
        icon1.addFile(u":/Images/air banner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.airButton.setIcon(icon1)
        self.airButton.setIconSize(QSize(500, 50))

        self.verticalLayout_2.addWidget(self.airButton)

        self.lightButton = QPushButton(homeWidget)
        self.lightButton.setObjectName(u"lightButton")
        icon2 = QIcon()
        icon2.addFile(u":/Images/light banner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lightButton.setIcon(icon2)
        self.lightButton.setIconSize(QSize(500, 50))

        self.verticalLayout_2.addWidget(self.lightButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(homeWidget)

        QMetaObject.connectSlotsByName(homeWidget)
    # setupUi

    def retranslateUi(self, homeWidget):
        homeWidget.setWindowTitle(QCoreApplication.translate("homeWidget", u"Impollutionize", None))
        self.label.setText(QCoreApplication.translate("homeWidget", u"Choose a gamemode to test/learn about a topic!", None))
        self.waterButton.setText("")
        self.airButton.setText("")
        self.lightButton.setText("")
    # retranslateUi

