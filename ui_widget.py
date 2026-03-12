# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(821, 317)
        self.verticalLayout_2 = QVBoxLayout(widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.headerImg = QLabel(widget)
        self.headerImg.setObjectName(u"headerImg")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerImg.sizePolicy().hasHeightForWidth())
        self.headerImg.setSizePolicy(sizePolicy)
        self.headerImg.setMinimumSize(QSize(1, 1))
        self.headerImg.setMaximumSize(QSize(1000, 1000))
        self.headerImg.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.headerImg)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.item_4 = QPushButton(widget)
        self.item_4.setObjectName(u"item_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.item_4.sizePolicy().hasHeightForWidth())
        self.item_4.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.item_4.setFont(font)

        self.gridLayout_2.addWidget(self.item_4, 0, 3, 1, 1)

        self.item_9 = QPushButton(widget)
        self.item_9.setObjectName(u"item_9")
        sizePolicy1.setHeightForWidth(self.item_9.sizePolicy().hasHeightForWidth())
        self.item_9.setSizePolicy(sizePolicy1)
        self.item_9.setFont(font)

        self.gridLayout_2.addWidget(self.item_9, 2, 0, 1, 1)

        self.item_7 = QPushButton(widget)
        self.item_7.setObjectName(u"item_7")
        sizePolicy1.setHeightForWidth(self.item_7.sizePolicy().hasHeightForWidth())
        self.item_7.setSizePolicy(sizePolicy1)
        self.item_7.setFont(font)

        self.gridLayout_2.addWidget(self.item_7, 1, 2, 1, 1)

        self.item_1 = QPushButton(widget)
        self.item_1.setObjectName(u"item_1")
        sizePolicy1.setHeightForWidth(self.item_1.sizePolicy().hasHeightForWidth())
        self.item_1.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.item_1.setFont(font1)

        self.gridLayout_2.addWidget(self.item_1, 0, 0, 1, 1)

        self.item_8 = QPushButton(widget)
        self.item_8.setObjectName(u"item_8")
        sizePolicy1.setHeightForWidth(self.item_8.sizePolicy().hasHeightForWidth())
        self.item_8.setSizePolicy(sizePolicy1)
        self.item_8.setFont(font)

        self.gridLayout_2.addWidget(self.item_8, 1, 3, 1, 1)

        self.item_6 = QPushButton(widget)
        self.item_6.setObjectName(u"item_6")
        sizePolicy1.setHeightForWidth(self.item_6.sizePolicy().hasHeightForWidth())
        self.item_6.setSizePolicy(sizePolicy1)
        self.item_6.setFont(font)

        self.gridLayout_2.addWidget(self.item_6, 1, 1, 1, 1)

        self.item_12 = QPushButton(widget)
        self.item_12.setObjectName(u"item_12")
        sizePolicy1.setHeightForWidth(self.item_12.sizePolicy().hasHeightForWidth())
        self.item_12.setSizePolicy(sizePolicy1)
        self.item_12.setFont(font)

        self.gridLayout_2.addWidget(self.item_12, 2, 3, 1, 1)

        self.item_5 = QPushButton(widget)
        self.item_5.setObjectName(u"item_5")
        sizePolicy1.setHeightForWidth(self.item_5.sizePolicy().hasHeightForWidth())
        self.item_5.setSizePolicy(sizePolicy1)
        self.item_5.setFont(font)

        self.gridLayout_2.addWidget(self.item_5, 1, 0, 1, 1)

        self.item_2 = QPushButton(widget)
        self.item_2.setObjectName(u"item_2")
        sizePolicy1.setHeightForWidth(self.item_2.sizePolicy().hasHeightForWidth())
        self.item_2.setSizePolicy(sizePolicy1)
        self.item_2.setFont(font)

        self.gridLayout_2.addWidget(self.item_2, 0, 1, 1, 1)

        self.item_10 = QPushButton(widget)
        self.item_10.setObjectName(u"item_10")
        sizePolicy1.setHeightForWidth(self.item_10.sizePolicy().hasHeightForWidth())
        self.item_10.setSizePolicy(sizePolicy1)
        self.item_10.setFont(font)

        self.gridLayout_2.addWidget(self.item_10, 2, 1, 1, 1)

        self.item_3 = QPushButton(widget)
        self.item_3.setObjectName(u"item_3")
        sizePolicy1.setHeightForWidth(self.item_3.sizePolicy().hasHeightForWidth())
        self.item_3.setSizePolicy(sizePolicy1)
        self.item_3.setFont(font)

        self.gridLayout_2.addWidget(self.item_3, 0, 2, 1, 1)

        self.item_11 = QPushButton(widget)
        self.item_11.setObjectName(u"item_11")
        sizePolicy1.setHeightForWidth(self.item_11.sizePolicy().hasHeightForWidth())
        self.item_11.setSizePolicy(sizePolicy1)
        self.item_11.setFont(font)

        self.gridLayout_2.addWidget(self.item_11, 2, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Impollutionize", None))
        self.headerImg.setText("")
        self.item_4.setText("")
        self.item_9.setText("")
        self.item_7.setText("")
        self.item_1.setText("")
        self.item_8.setText("")
        self.item_6.setText("")
        self.item_12.setText("")
        self.item_5.setText("")
        self.item_2.setText("")
        self.item_10.setText("")
        self.item_3.setText("")
        self.item_11.setText("")
    # retranslateUi

