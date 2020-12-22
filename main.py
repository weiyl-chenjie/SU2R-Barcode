# 系统自带的库
import sys
import sqlite3

# 第三方库
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide2.QtCore import QDate

# 自己的包
from UI2PY.MainWindow import Ui_MainWindow
import sato
from config import Config

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.Ui_MainWindow = Ui_MainWindow()
        self.Ui_MainWindow.setupUi(self)

        # 串口设置
        # self.com = ComThread()
        # 打开指定串口
        # self.open_com()

        self.conf = Config()

        # USB设置
        self.usb = sato.USB()
        if self.usb.open_usb() == None:
            QMessageBox.critical(self, '错误', '未找到指定USB设备')

        # 初始化
        try:
            with sqlite3.connect('code.db') as conn:
                c = conn.cursor()
                self.supplier_code = [x[0] for x in c.execute("SELECT data FROM supplier_code ORDER BY data").fetchall()]
                self.part_number = {x[0] : x[1] for x in c.execute("SELECT partNumber, sequenceCode FROM part_number ORDER BY partNumber").fetchall()}
                self.engineering_order_number = [x[0] for x in c.execute("SELECT data FROM engineering_order_number").fetchall()]
                self.serial_or_lot_delimiter = [x[0] for x in c.execute("SELECT data FROM serial_or_lot_delimiter").fetchall()]
                self.free_space_for_supplier_itself = [x[0] for x in c.execute("SELECT data FROM free_space_for_supplier_itself").fetchall()]
        except Exception as e:
            QMessageBox.critical(self, '错误', str(e))
        self.init_widgets()

    # # 检查并打开指定串口
    # def open_com(self):
    #     if self.com.check_com():  # 如果存在串口，则打开指定串口
    #         if self.com.open_com(): # 如果串口打开成功
    #             pass
    #         else:
    #             QMessageBox.critical(self, '错误！', '串口打开失败！')
    #     else:
    #         QMessageBox.critical(self, '错误！', '未发现串口！')

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

        # 读取配置文件值
        # 二维码以及第一行文字的垂直高度（两列共用）
        vdis = int(self.conf.read_config(product='config', section='printer', name='vdis'))
        # 二维码水平位置（两列各自独有）
        hdis1 = int(self.conf.read_config(product='config', section='printer', name='hdis1'))
        hdis2 = int(self.conf.read_config(product='config', section='printer', name='hdis2'))
        # 二维码与文字之间的水平间距（两列共用）
        barcode_to_text_dis = int(self.conf.read_config(product='config', section='printer', name='barcode_to_text_dis'))
        # 外侧一列标签的文字的水平位置
        hdis1_text = hdis1 + barcode_to_text_dis
        # 内测一列标签的文字的水平位置
        hdis2_text = hdis2 + barcode_to_text_dis
        # 第二行文字的垂直高度（两列共用）
        vdis_text2 = int(self.conf.read_config(product='config', section='printer', name='vdis_text2'))
        # 第三行文字的垂直高度（两列共用）
        vdis_text3 = int(self.conf.read_config(product='config', section='printer', name='vdis_text3'))

        if is_print:
            for i in range(start_print, end_print + 1, 2):
                serial_or_lot_number_info1 = b'%07d\x1D' % i
                serial_or_lot_number_info2 = b'%07d\x1D' % (i + 1)
                data1 = header + \
                       supplier_code + \
                       part_number + \
                       sequence_code + \
                       engineering_order_number + \
                       product_date + \
                       FourM_info + \
                       serial_or_lot_delimiter + \
                       serial_or_lot_number_info1 + \
                       free_space_for_supplier_itself + \
                       trailer

                data2 = header + \
                        supplier_code + \
                        part_number + \
                        sequence_code + \
                        engineering_order_number + \
                        product_date + \
                        FourM_info + \
                        serial_or_lot_delimiter + \
                        serial_or_lot_number_info2 + \
                        free_space_for_supplier_itself + \
                        trailer

                if (i+1) > end_print:  #双排打印，判断第二个标签是否超出数量限制，如果超出则该次只打印一列
                    satoString_add = b''
                else:
                    satoString_add = f'\x1bH{hdis2}\x1bV{vdis}\x1b2D50,06,06,032,032\x1bDN{len(data2)},'.encode("utf-8") + \
                                     data2 + \
                                     (f'\x1bH{hdis2_text}\x1bV{vdis}\x1bL0202\x1bS\x1b$A,80,80,0\x1b$=' + self.Ui_MainWindow.lineEdit_Sequence_Code.text()).encode("utf-8") + \
                                     (f'\x1bH{hdis2_text}\x1bV{vdis_text2}\x1bL0202\x1bS' + self.Ui_MainWindow.comboBox_PartNumber.currentText()).encode("utf-8") + \
                                     f'\x1bH{hdis2_text}\x1bV{vdis_text3}\x1bL0202\x1bS'.encode("utf-8") + serial_or_lot_number_info2[-6:-1]
                satoString = f'\x1bA\x1bH{hdis1}\x1bV{vdis}\x1b2D50,06,06,032,032\x1bDN{len(data1)},'.encode("utf-8") + \
                             data1 + \
                             (f'\x1bH{hdis1_text}\x1bV{vdis}\x1bL0202\x1bS\x1b$A,80,80,0\x1b$=' + self.Ui_MainWindow.lineEdit_Sequence_Code.text()).encode("utf-8") + \
                             (f'\x1bH{hdis1_text}\x1bV{vdis_text2}\x1bL0202\x1bS' + self.Ui_MainWindow.comboBox_PartNumber.currentText()).encode("utf-8") + \
                             f'\x1bH{hdis1_text}\x1bV{vdis_text3}\x1bL0202\x1bS'.encode("utf-8") + serial_or_lot_number_info1[-6:-1] + \
                             satoString_add + \
                             b'\x1bQ1\x1bZ'
                print(satoString)
                # self.com.send_data(satoString)
                self.usb.write_data(1, satoString)

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