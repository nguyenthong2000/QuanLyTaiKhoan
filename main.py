import sys
from PySide6 import QtGui,QtCore,QtWidgets

from taikhoan import TaiKhoan

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản Lý Tài Khoản")
        self.taikhoan = TaiKhoan()
        self.setCentralWidget(self.taikhoan)
        self.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    sys.exit(app.exec())