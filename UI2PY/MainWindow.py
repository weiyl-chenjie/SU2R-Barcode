# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(410, 470, 131, 51))
        font = QFont()
        font.setFamily(u"\u534e\u6587\u6977\u4f53")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        icon = QIcon()
        iconThemeName = u"print"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u":/\u6253\u5370/print.png", QSize(), QIcon.Normal, QIcon.Off)
        
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(50, 50))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(142, 22, 258, 415))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(256, 32))
        self.label_4.setMaximumSize(QSize(256, 32))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(256, 32))
        self.label_7.setMaximumSize(QSize(256, 32))
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_7, 8, 0, 1, 1)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(256, 0))
        self.line.setMaximumSize(QSize(256, 16777215))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(256, 32))
        self.label_5.setMaximumSize(QSize(256, 32))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(256, 32))
        self.label_6.setMaximumSize(QSize(256, 32))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 7, 0, 1, 1)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(256, 0))
        self.line_2.setMaximumSize(QSize(256, 16777215))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 6, 0, 1, 1)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(256, 32))
        self.label_9.setMaximumSize(QSize(256, 32))
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_9, 10, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(256, 32))
        self.label_2.setMaximumSize(QSize(256, 32))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(256, 32))
        self.label_8.setMaximumSize(QSize(256, 32))
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_8, 9, 0, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(256, 32))
        self.label_10.setMaximumSize(QSize(256, 32))
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_10, 12, 0, 1, 1)

        self.line_3 = QFrame(self.layoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(256, 0))
        self.line_3.setMaximumSize(QSize(256, 16777215))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 11, 0, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(256, 32))
        self.label.setMaximumSize(QSize(256, 32))
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(256, 32))
        self.label_3.setMaximumSize(QSize(256, 32))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(412, 22, 322, 415))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_Header = QLineEdit(self.widget)
        self.lineEdit_Header.setObjectName(u"lineEdit_Header")
        sizePolicy.setHeightForWidth(self.lineEdit_Header.sizePolicy().hasHeightForWidth())
        self.lineEdit_Header.setSizePolicy(sizePolicy)
        self.lineEdit_Header.setMinimumSize(QSize(320, 32))
        self.lineEdit_Header.setMaximumSize(QSize(320, 32))
        font2 = QFont()
        font2.setPointSize(16)
        self.lineEdit_Header.setFont(font2)
        self.lineEdit_Header.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_Header, 0, 0, 1, 3)

        self.line_4 = QFrame(self.widget)
        self.line_4.setObjectName(u"line_4")
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setMinimumSize(QSize(320, 0))
        self.line_4.setMaximumSize(QSize(320, 16777215))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 1, 0, 1, 3)

        self.comboBox_Supplier_Code = QComboBox(self.widget)
        self.comboBox_Supplier_Code.setObjectName(u"comboBox_Supplier_Code")
        sizePolicy.setHeightForWidth(self.comboBox_Supplier_Code.sizePolicy().hasHeightForWidth())
        self.comboBox_Supplier_Code.setSizePolicy(sizePolicy)
        self.comboBox_Supplier_Code.setMinimumSize(QSize(320, 32))
        self.comboBox_Supplier_Code.setMaximumSize(QSize(320, 32))
        self.comboBox_Supplier_Code.setFont(font2)

        self.gridLayout.addWidget(self.comboBox_Supplier_Code, 2, 0, 1, 3)

        self.comboBox_PartNumber = QComboBox(self.widget)
        self.comboBox_PartNumber.setObjectName(u"comboBox_PartNumber")
        sizePolicy.setHeightForWidth(self.comboBox_PartNumber.sizePolicy().hasHeightForWidth())
        self.comboBox_PartNumber.setSizePolicy(sizePolicy)
        self.comboBox_PartNumber.setMinimumSize(QSize(320, 32))
        self.comboBox_PartNumber.setMaximumSize(QSize(320, 32))
        self.comboBox_PartNumber.setFont(font2)

        self.gridLayout.addWidget(self.comboBox_PartNumber, 3, 0, 1, 3)

        self.lineEdit_Sequence_Code = QLineEdit(self.widget)
        self.lineEdit_Sequence_Code.setObjectName(u"lineEdit_Sequence_Code")
        sizePolicy.setHeightForWidth(self.lineEdit_Sequence_Code.sizePolicy().hasHeightForWidth())
        self.lineEdit_Sequence_Code.setSizePolicy(sizePolicy)
        self.lineEdit_Sequence_Code.setMinimumSize(QSize(320, 32))
        self.lineEdit_Sequence_Code.setMaximumSize(QSize(320, 32))
        self.lineEdit_Sequence_Code.setFont(font2)
        self.lineEdit_Sequence_Code.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_Sequence_Code, 4, 0, 1, 3)

        self.comboBox_Engineering_Order_Number = QComboBox(self.widget)
        self.comboBox_Engineering_Order_Number.setObjectName(u"comboBox_Engineering_Order_Number")
        sizePolicy.setHeightForWidth(self.comboBox_Engineering_Order_Number.sizePolicy().hasHeightForWidth())
        self.comboBox_Engineering_Order_Number.setSizePolicy(sizePolicy)
        self.comboBox_Engineering_Order_Number.setMinimumSize(QSize(320, 32))
        self.comboBox_Engineering_Order_Number.setMaximumSize(QSize(320, 32))
        self.comboBox_Engineering_Order_Number.setFont(font2)

        self.gridLayout.addWidget(self.comboBox_Engineering_Order_Number, 5, 0, 1, 3)

        self.line_5 = QFrame(self.widget)
        self.line_5.setObjectName(u"line_5")
        sizePolicy.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy)
        self.line_5.setMinimumSize(QSize(320, 0))
        self.line_5.setMaximumSize(QSize(320, 16777215))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 6, 0, 1, 3)

        self.dateEdit_Production_Date = QDateEdit(self.widget)
        self.dateEdit_Production_Date.setObjectName(u"dateEdit_Production_Date")
        sizePolicy.setHeightForWidth(self.dateEdit_Production_Date.sizePolicy().hasHeightForWidth())
        self.dateEdit_Production_Date.setSizePolicy(sizePolicy)
        self.dateEdit_Production_Date.setMinimumSize(QSize(320, 32))
        self.dateEdit_Production_Date.setMaximumSize(QSize(320, 32))
        self.dateEdit_Production_Date.setFont(font2)
        self.dateEdit_Production_Date.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEdit_Production_Date.setCalendarPopup(True)
        self.dateEdit_Production_Date.setCurrentSectionIndex(0)
        self.dateEdit_Production_Date.setDate(QDate(2020, 12, 1))

        self.gridLayout.addWidget(self.dateEdit_Production_Date, 7, 0, 1, 3)

        self.lineEdit_4M_info = QLineEdit(self.widget)
        self.lineEdit_4M_info.setObjectName(u"lineEdit_4M_info")
        sizePolicy.setHeightForWidth(self.lineEdit_4M_info.sizePolicy().hasHeightForWidth())
        self.lineEdit_4M_info.setSizePolicy(sizePolicy)
        self.lineEdit_4M_info.setMinimumSize(QSize(320, 32))
        self.lineEdit_4M_info.setMaximumSize(QSize(320, 32))
        self.lineEdit_4M_info.setFont(font2)

        self.gridLayout.addWidget(self.lineEdit_4M_info, 8, 0, 1, 3)

        self.comboBox_Serial_or_Lot_delimiter = QComboBox(self.widget)
        self.comboBox_Serial_or_Lot_delimiter.setObjectName(u"comboBox_Serial_or_Lot_delimiter")
        sizePolicy.setHeightForWidth(self.comboBox_Serial_or_Lot_delimiter.sizePolicy().hasHeightForWidth())
        self.comboBox_Serial_or_Lot_delimiter.setSizePolicy(sizePolicy)
        self.comboBox_Serial_or_Lot_delimiter.setMinimumSize(QSize(320, 32))
        self.comboBox_Serial_or_Lot_delimiter.setMaximumSize(QSize(320, 32))
        self.comboBox_Serial_or_Lot_delimiter.setFont(font2)

        self.gridLayout.addWidget(self.comboBox_Serial_or_Lot_delimiter, 9, 0, 1, 3)

        self.spinBox_Min = QSpinBox(self.widget)
        self.spinBox_Min.setObjectName(u"spinBox_Min")
        sizePolicy.setHeightForWidth(self.spinBox_Min.sizePolicy().hasHeightForWidth())
        self.spinBox_Min.setSizePolicy(sizePolicy)
        self.spinBox_Min.setMinimumSize(QSize(136, 32))
        self.spinBox_Min.setMaximumSize(QSize(136, 32))
        self.spinBox_Min.setFont(font2)
        self.spinBox_Min.setMinimum(1)
        self.spinBox_Min.setMaximum(999999999)

        self.gridLayout.addWidget(self.spinBox_Min, 10, 0, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(26, 21))
        self.label_11.setMaximumSize(QSize(26, 21))
        font3 = QFont()
        font3.setFamily(u"\u534e\u6587\u6977\u4f53")
        font3.setPointSize(16)
        self.label_11.setFont(font3)

        self.gridLayout.addWidget(self.label_11, 10, 1, 1, 1)

        self.spinBox_Max = QSpinBox(self.widget)
        self.spinBox_Max.setObjectName(u"spinBox_Max")
        sizePolicy.setHeightForWidth(self.spinBox_Max.sizePolicy().hasHeightForWidth())
        self.spinBox_Max.setSizePolicy(sizePolicy)
        self.spinBox_Max.setMinimumSize(QSize(136, 32))
        self.spinBox_Max.setMaximumSize(QSize(136, 32))
        self.spinBox_Max.setFont(font2)
        self.spinBox_Max.setMinimum(1)
        self.spinBox_Max.setMaximum(999999999)

        self.gridLayout.addWidget(self.spinBox_Max, 10, 2, 1, 1)

        self.line_6 = QFrame(self.widget)
        self.line_6.setObjectName(u"line_6")
        sizePolicy.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy)
        self.line_6.setMinimumSize(QSize(320, 0))
        self.line_6.setMaximumSize(QSize(320, 16777215))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_6, 11, 0, 1, 3)

        self.comboBox_free_space_for_Supplier_itself = QComboBox(self.widget)
        self.comboBox_free_space_for_Supplier_itself.setObjectName(u"comboBox_free_space_for_Supplier_itself")
        sizePolicy.setHeightForWidth(self.comboBox_free_space_for_Supplier_itself.sizePolicy().hasHeightForWidth())
        self.comboBox_free_space_for_Supplier_itself.setSizePolicy(sizePolicy)
        self.comboBox_free_space_for_Supplier_itself.setMinimumSize(QSize(320, 32))
        self.comboBox_free_space_for_Supplier_itself.setMaximumSize(QSize(320, 32))
        self.comboBox_free_space_for_Supplier_itself.setFont(font2)

        self.gridLayout.addWidget(self.comboBox_free_space_for_Supplier_itself, 12, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_PartNumber.activated.connect(MainWindow.set_part_number)
        self.pushButton.clicked.connect(MainWindow.barcode_print)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5370", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Sequence Code\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"4M Info.\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Engineering Order Number(O)\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Production Date\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Serial or Lot number info.\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Supplier Code\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Serial or Lot delimiter\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Free space for Supplier itself(O)\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Header\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PartNumber\uff1a", None))
        self.lineEdit_Header.setText(QCoreApplication.translate("MainWindow", u"[)>06", None))
        self.lineEdit_Sequence_Code.setText("")
        self.dateEdit_Production_Date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.lineEdit_4M_info.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5230", None))
    # retranslateUi

