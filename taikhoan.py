import sys
from PySide6 import QtGui,QtCore,QtWidgets

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://hoangthong:hoangthong16@onmyojibot.fgbvh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["QuanLyTaiKhoan"]
collection= db["TaiKhoan"]

class TaiKhoan(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.w = 1500
        self.h = 600
        self.setMinimumSize(self.w, self.h)
        self.r = 0
        self.label_title = ["Mã Tài Khoản", "Tên Tài Khoản","Mật Khẩu","Quyền"]
        self.itemcombobox= ["Admin","Member"]
        self.setContentsMargins(10, 0, 10, 10)

        # layout chính
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        # Bảng dữ liệu
        self.tableWidget = QtWidgets.QTableWidget(50, 4)
        self.tableWidget.setMinimumSize(600,300)
        self.tableWidget.setStyleSheet("font-size: 14px")
        #self.tableWidget.setSortingEnabled(True)
        # set tiêu đề cột
        self.tableWidget.setHorizontalHeaderLabels(self.label_title)
        # Kéo độ dài của cột đến cuối
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # Chia đều độ dài của cột
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Tiêu đề bảng
        self.lb_title = QtWidgets.QLabel("Tài Khoản")
        self.lb_title.setStyleSheet("color: blue;"
                                  "font: bold 24px;"
                                  "margin-bottom: 30px")
        self.lb_title.setAlignment(QtCore.Qt.AlignCenter)

        self.layout_thaotac = QtWidgets.QGridLayout()

        # Label Mã Tài Khoản
        self.lb_ma = QtWidgets.QLabel("Mã Tài Khoản")
        self.lb_ma.setStyleSheet("font-size: 14px")

        # Label Tên Tài Khoản
        self.lb_ten = QtWidgets.QLabel("Tên Tài Khoản")
        self.lb_ten.setStyleSheet("font-size: 14px")

        # Label Mật Khẩu
        self.lb_matkhau = QtWidgets.QLabel("Mật Khẩu")
        self.lb_ten.setStyleSheet("font-size: 14px")

        # Label Quyền
        self.lb_quyen = QtWidgets.QLabel("Quyền")
        self.lb_quyen.setStyleSheet("font-size: 14px")

        # LineEdit Mã Tài Khoản
        self.le_ma = QtWidgets.QLineEdit()
        self.le_ma.setEnabled(False)
        self.le_ma.setStyleSheet("width: 100px;"
                                 "height: 25px;"
                                 "font-size: 14px")

        # LineEdit Tên Tài Khoản
        self.le_ten = QtWidgets.QLineEdit()
        self.le_ten.setStyleSheet("width: 100px;"
                               "height: 25px;"
                                  "font-size: 14px")

        # LineEdit Mật Khẩu
        self.le_matkhau= QtWidgets.QLineEdit()
        self.le_matkhau.setStyleSheet("width: 100px;"
                                  "height: 25px;"
                                  "font-size: 14px")

        # ComboBox Quyền
        self.cbb_quyen = QtWidgets.QComboBox()
        self.cbb_quyen.addItems(self.itemcombobox)
        self.cbb_quyen.setCurrentIndex(0)
        self.cbb_quyen.setStyleSheet("width:20px;"
                                  "height: 25px;"
                                  "font-size: 14px")

        # button Thêm
        self.btn_them = QtWidgets.QPushButton("Thêm")
        self.btn_them.setIcon(QtGui.QIcon("image\\plus.png"))
        self.btn_them.setStyleSheet("width: 150px;"
                                    "height: 30px;"
                                    "margin-left: 100px;"
                                    "font-size: 14px")

        # button Sửa
        self.btn_sua = QtWidgets.QPushButton("Sửa")
        self.btn_sua.setIcon(QtGui.QIcon("image\\loop.png"))
        self.btn_sua.setStyleSheet("width: 150px;"
                                   "height: 30px;"
                                   "margin-left: 100px;"
                                   "font-size: 14px")

        # button Xoá
        self.btn_xoa = QtWidgets.QPushButton("Xoá")
        self.btn_xoa.setIcon(QtGui.QIcon("image\\remove.png"))
        self.btn_xoa.setStyleSheet("width: 150px;"
                                   "height: 30px;"
                                   "margin-left: 100px;"
                                   "font-size: 14px"
                                   )

        # chèn Label vào layout
        self.layout_thaotac.addWidget(self.lb_ma, 0, 0)
        self.layout_thaotac.addWidget(self.lb_ten, 1, 0)
        self.layout_thaotac.addWidget(self.lb_matkhau, 0, 2)
        self.layout_thaotac.addWidget(self.lb_quyen, 1, 2)

        # chèn LineEdit vào layout
        self.layout_thaotac.addWidget(self.le_ma, 0, 1)
        self.layout_thaotac.addWidget(self.le_ten, 1, 1)
        self.layout_thaotac.addWidget(self.le_matkhau, 0, 3)
        self.layout_thaotac.addWidget(self.cbb_quyen, 1, 3)

        # chèn Button vào layout
        self.layout_thaotac.addWidget(self.btn_them, 0, 4)
        self.layout_thaotac.addWidget(self.btn_sua, 1, 4)
        self.layout_thaotac.addWidget(self.btn_xoa, 2, 4)

        layout.addWidget(self.lb_title)
        layout.addWidget(self.tableWidget)
        layout.addLayout(self.layout_thaotac)

        self.hienThi()

        self.btn_them.clicked.connect(self.themTaiKhoan)
        self.btn_sua.clicked.connect(self.suaTaiKhoan)
        self.btn_xoa.clicked.connect(self.xoaTaiKhoan)
        self.tableWidget.clicked.connect(self.selectedItem)

    def selectedItem(self, event):
        """Hiện thị dữ liệu ở ô đang chọn trong LineEdit"""
        self.r = event.row()
        try:
            self.le_ma.setText(self.tableWidget.item(self.r, 0).text())
            self.le_ten.setText(self.tableWidget.item(self.r, 1).text())
            self.le_matkhau.setText(self.tableWidget.item(self.r, 2).text())
            self.cbb_quyen.setCurrentText(self.tableWidget.item(self.r,3).text())

        except:
            self.le_ma.setText("")
            self.le_ten.setText("")
            self.le_matkhau.setText("")
            self.cbb_quyen.setCurrentText("")



    def hienThi(self):
        """Hiện thị dữ liệu"""
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(self.label_title)
        loaddata = collection.find()
        item_count = loaddata.count()
        if item_count >50:
            self.tableWidget.setRowCount(item_count)

        i = 0
        for data in loaddata:
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data["_id"])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(data["taikhoan"]))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(data["matkhau"]))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(data["quyen"]))
            i = i + 1

    def themTaiKhoan(self):
        """Thêm Tài Khoản"""
        data = {"taikhoan": self.le_ten.text(),"matkhau":self.le_matkhau.text(),"quyen": self.cbb_quyen.currentText()}
        collection.insert_one(data)
        self.hienThi()

    def xoaTaiKhoan(self):
        """Xoá Tài Khoản"""
        collection.delete_one({"_id": ObjectId(self.le_ma.text())})
        self.hienThi()

    def suaTaiKhoan(self):
        """Sửa Tài Khoản"""
        if self.le_ma.text():
            collection.update_one({"_id": ObjectId(self.le_ma.text())},
                                  {"$set":{"taikhoan": self.le_ten.text(), "matkhau":self.le_matkhau.text(), "quyen": self.cbb_quyen.currentText()}})
            self.hienThi()
        else:
            QtWidgets.QMessageBox.critical(self,"Thông báo","Không thể sửa khi thiếu mã")
