import os
from time import sleep
import tkinter.messagebox
import tkinter

import sato

if __name__ == '__main__':
    ct = sato.ComThread()
    print(f"检查串口{ct.check_com()}")
    print(f"选择串口{ct.open_com()}")
    barcode = "11234"
    barcodeBytes = barcode.encode("utf-8")  # 转换为字节格式
    # b'\x1bH520\x1bV109\x1bL0202\x1bS' + barcodeBytes +
    #satoString = b'\x1bA\x1bN\x1bR\x1bR\x1bH070\x1bV00002\x1bL0202\x1bS\x1bB103080*' + barcodeBytes + b'*\x1bH0200\x1bV00009\x1bL0202\x1bS' + barcodeBytes + b'\x1bQ1\x1bZ'
    data = b'[)>\x1E06\x1D' + \
                 b'VH2TM\x1D' + \
                 b'P1234567890\x1D' + \
                 b'SALC1\x1D' + \
                 b'EOptional\x1D' + \
                 b'T201210132NA1234567\x1D' + \
                 b'COptional\x1D' + \
                 b'\x1E\x04'
    # satoString = b'\x1bA\x1bN\x1bH420\x1bV00002\x1bL0202\x1bS\x1b2D50,10,10,000,000\x1bDN%04d,' % len(data) + \
    #             data + \
    #             b'\x1bQ1\x1bZ'
    satoString = b'\x1bA\x1bN\x1bH420\x1bV00016\x1b2D50,04,04,032,032\x1bDN%04d,' % len(data) + \
                 data + \
                 b'\x1bH560\x1bV00016\x1bL0202\x1bS' + b'H2TM' + \
                 b'\x1bH560\x1bV00062\x1bL0202\x1bS' + b'BBBB' + \
                 b'\x1bH560\x1bV00108\x1bL0202\x1bS' + b'0001' + \
                 b'\x1bQ1\x1bZ'
    print(satoString)
    print(len(b'[)>\x1E06\x1D'))
    ct.send_data(satoString)
