from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont

dastur = QApplication([])
oyna = QWidget()

# oyna.setGeometry(1200, 300, 350, 500)
# oyna.setFixedWidth(350)
# oyna.setFixedHeight(500)
oyna.setFixedSize(450, 500)
oyna.setWindowTitle("Dastur")
oyna.setWindowIcon(QIcon("C:\\Users\\Acer\\Desktop\\python-telegram-bot-image.jpg"))

yozuv1 = QLabel("Start", oyna)
yozuv1.setFont(QFont("Times New Roman", 28, italic=True))
yozuv1.setStyleSheet("color: green;")
yozuv1.move(50, 50)


input = QLineEdit(oyna)
input.setGeometry(50, 250, 350, 50)
input.setStyleSheet("font-size: 30px;")
input.setPlaceholderText("Son kiriting:")


def bosildi():
    txt = input.text()
    yozuv1.setText(txt)
    yozuv1.adjustSize()
    input.clear()


button = QPushButton("Jo'natish", oyna)
button.setGeometry(100, 400, 150, 50)
button.setStyleSheet("font-size: 20px;")

button.clicked.connect(bosildi)



oyna.show()
dastur.exec_()