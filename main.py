# 系统自带的库
import sys
import sqlite3

# 第三方库
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide2.QtCore import QDate

# 自己的包
from UI2PY.MainWindow import Ui_MainWindow
from sato import ComThread


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.Ui_MainWindow = Ui_MainWindow()
        self.Ui_MainWindow.setupUi(self)

        # 串口设置
        self.com = ComThread()
        # 打开指定串口
        self.open_com()

        # 初始化
        try:
            with sqlite3.connect('code.db') as conn:
                c = conn.cursor()
                self.supplier_code = [x[0] for x in c.execute("SELECT data FROM supplier_code").fetchall()]
                self.part_number = {x[0] : x[1] for x in c.execute("SELECT partNumber, sequenceCode FROM part_number").fetchall()}
                self.engineering_order_number = [x[0] for x in c.execute("SELECT data FROM engineering_order_number").fetchall()]
                self.serial_or_lot_delimiter = [x[0] for x in c.execute("SELECT data FROM serial_or_lot_delimiter").fetchall()]
                self.free_space_for_supplier_itself = [x[0] for x in c.execute("SELECT data FROM free_space_for_supplier_itself").fetchall()]
        except Exception as e:
            QMessageBox.critical(self, '错误', str(e))
        self.init_widgets()

    # 检查并打开指定串口
    def open_com(self):
        if self.com.check_com():  # 如果存在串口，则打开指定串口
            if self.com.open_com(): # 如果串口打开成功
                pass
            else:
                QMessageBox.critical(self, '错误！', '串口打开失败！')
        else:
            QMessageBox.critical(self, '错误！', '未发现串口！')

    # 初始化控件值：
    def init_widgets(self):
        self.Ui_MainWindow.comboBox_Supplier_Code.addItem('')
        self.Ui_MainWindow.comboBox_PartNumber.addItem('')
        self.Ui_MainWindow.lineEdit_Sequence_Code.clear()
        self.Ui_MainWindow.comboBox_Engineering_Order_Number.addItem('')
        self.Ui_MainWindow.comboBox_Serial_or_Lot_delimiter.addItem('')
        self.Ui_MainWindow.comboBox_free_space_for_Supplier_itself.addItem('')

        for item in self.supplier_code:
            self.Ui_MainWindow.comboBox_Supplier_Code.addItem(item)
        for key in self.part_number.keys():
            self.Ui_MainWindow.comboBox_PartNumber.addItem(key)
        for item in self.engineering_order_number:
            self.Ui_MainWindow.comboBox_Engineering_Order_Number.addItem(item)
        for item in self.serial_or_lot_delimiter:
            self.Ui_MainWindow.comboBox_Serial_or_Lot_delimiter.addItem(item)
        for item in self.free_space_for_supplier_itself:
            self.Ui_MainWindow.comboBox_free_space_for_Supplier_itself.addItem(item)

        self.Ui_MainWindow.dateEdit_Production_Date.setDate(QDate.currentDate())

    # 槽函数
    def set_part_number(self):
        if self.Ui_MainWindow.comboBox_PartNumber.currentText():
            sequence_code = self.part_number[self.Ui_MainWindow.comboBox_PartNumber.currentText()]
            self.Ui_MainWindow.lineEdit_Sequence_Code.setText(sequence_code)
        else:
            self.Ui_MainWindow.lineEdit_Sequence_Code.clear()

    def barcode_print(self):
        is_print = True
        start_print = self.Ui_MainWindow.spinBox_Min.value()
        end_print = self.Ui_MainWindow.spinBox_Max.value()
        header = b'[)>\x1E06\x1D'
        supplier_code = b'V%s\x1D' % self.Ui_MainWindow.comboBox_Supplier_Code.currentText().encode("utf-8")
        is_print = self.is_null(supplier_code, 'supplier_code', is_print, 2)

        part_number = b'P%s\x1D' % self.Ui_MainWindow.comboBox_PartNumber.currentText().encode("utf-8")
        is_print = self.is_null(part_number, 'part_number', is_print, 2)

        sequence_code = b'S%s\x1D' % self.Ui_MainWindow.lineEdit_Sequence_Code.text().encode("utf-8")
        is_print = self.is_null(sequence_code, 'sequence_code', is_print, 2)

        engineering_order_number = (b'E%s\x1D' % self.Ui_MainWindow.comboBox_Engineering_Order_Number.currentText().encode("utf-8") \
                                    if self.Ui_MainWindow.comboBox_Engineering_Order_Number.currentText() else b'')

        product_date = b'T%s' % self.Ui_MainWindow.dateEdit_Production_Date.date().toString('yyMMdd').encode("utf-8")
        is_print = self.is_null(product_date, 'product_date', is_print, 1)

        FourM_info = b'%s' % self.Ui_MainWindow.lineEdit_4M_info.text().encode("utf-8")
        is_print = self.is_null(FourM_info, 'FourM_info', is_print, 0)

        serial_or_lot_delimiter = b'%s' % self.Ui_MainWindow.comboBox_Serial_or_Lot_delimiter.currentText().encode("utf-8")
        is_print = self.is_null(serial_or_lot_delimiter, 'serial_or_lot_delimiter', is_print, 0)

        if start_print > end_print:
            is_print = False

        free_space_for_supplier_itself = (b'C%s\x1D' % self.Ui_MainWindow.comboBox_free_space_for_Supplier_itself.currentText().encode("utf-8") \
                                          if self.Ui_MainWindow.comboBox_free_space_for_Supplier_itself.currentText() \
                                          else b'')
        trailer = b'\x1E\x04'

        if is_print:
            for i in range(start_print, end_print + 1):
                serial_or_lot_number_info = b'%07d\x1D' % i
                data = header + \
                       supplier_code + \
                       part_number + \
                       sequence_code + \
                       engineering_order_number + \
                       product_date + \
                       FourM_info + \
                       serial_or_lot_delimiter + \
                       serial_or_lot_number_info + \
                       free_space_for_supplier_itself + \
                       trailer

                satoString = b'\x1bA\x1bN\x1bH420\x1bV00016\x1b2D50,04,04,032,032\x1bDN%04d,' % len(data) + \
                             data + \
                             b'\x1bH560\x1bV00003\x1bL0101\x1bS' + b'\x1b$A,100,100,0\x1b$=' + self.Ui_MainWindow.lineEdit_Sequence_Code.text().encode("utf-8") + \
                             b'\x1bH560\x1bV00098\x1bL0101\x1bS' + self.Ui_MainWindow.comboBox_PartNumber.currentText().encode("utf-8") + \
                             b'\x1bH560\x1bV00128\x1bL0101\x1bS' + serial_or_lot_number_info[-6:-1] + \
                             b'\x1bQ1\x1bZ'
                print(data)
                print(satoString)
                self.com.send_data(satoString)

    # 功能函数
    def is_null(self, value, widget, is_print, length):  # 判断控件当前值是否为空
        if len(value) == length:
            QMessageBox.critical(self, '错误！', '%s不能为空！' % widget)
            is_print =  False
        return is_print


if __name__ == '__main__':
    # 创建一个应用程序对象
    app = QApplication(sys.argv)

    # 创建控件(容器)
    window = MyWindow()

    # 显示窗口
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())