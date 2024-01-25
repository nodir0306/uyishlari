from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

from time import sleep

dastur = QApplication([])
oyna = QWidget()
oyna.setFixedSize(395, 400)
oyna.setWindowTitle("Calculator")
oyna.setWindowIcon(QIcon("D:\\Python\\PyQt5\\calculator.jpg"))



button_width = 90
button_spacing = 5
button_height_map = 260
#-----------------------------------------------------------------------------------------------------------------------
def main_func():
    current_text = edt.text()
    if current_text == "" or current_text[0] == "0":
        edt.setText("")
    else:
        try:
            res = eval(current_text)
            if not any(char.isdigit() for char in str(res)):
                edt.setText("")
            else:
                edt.setText(str(res))
        except ZeroDivisionError:
            edt.setText("")
        except SyntaxError:
            edt.setText("")
        except IndexError:
            edt.setText("")




#----------------------------------------------------------------------------------------------------------------------
def clear_btn():
    edt.clear()
#-----------------------------------------------------------------------------------------------------------------------
def button_1():
    current_text = edt.text()
    edt.setText(current_text+"1")
    
def button_2():
    current_text = edt.text()
    edt.setText(current_text+"2")
    
def button_3():
    current_text = edt.text()
    edt.setText(current_text+"3")
    
def button_4():
    current_text = edt.text()
    edt.setText(current_text+"4")
def button_5():
    current_text = edt.text()
    edt.setText(current_text+"5")
    
def button_6():
    current_text = edt.text()
    edt.setText(current_text+"6")
    
def button_7():
    current_text = edt.text()
    edt.setText(current_text+"7")
    
def button_8():
    current_text = edt.text()
    edt.setText(current_text+"8")
    
def button_9():
    current_text = edt.text()
    edt.setText(current_text+"9")
    
def button_0():
    current_text = edt.text()
    edt.setText(current_text+"0")

#-----------------------------------------------------------------------------------------------------------------------

def button_pul():
    current_text = edt.text()
    if current_text == "":
        edt.setText(current_text+"")
    else:
        edt.setText(current_text+"+")
    
def button_min():
    current_text = edt.text()
    if current_text == "":
        edt.setText(current_text+"")
    else:
        edt.setText(current_text+"-")
    
def button_div():
    current_text = edt.text()
    if current_text == "":
        edt.setText(current_text+"")
    else:
        edt.setText(current_text+"/")
    
def button_mul():
    current_text = edt.text()
    if current_text == "":
        edt.setText(current_text)
    else:
        edt.setText(current_text + "*")


edt  = QLineEdit(oyna)
edt.setGeometry(9, button_height_map-250, button_width+283, 110)

#-----------------------------------------------------------------------------------------------------------------------
btn_clear = QPushButton("C", oyna)
btn_clear.setGeometry(9, button_height_map+67, button_width, 60)
btn_clear.setStyleSheet("""
font-size: 25px;
color: red;
font-weight: bold;
                        """)
btn_clear.clicked.connect(clear_btn)

btn_0 = QPushButton("0", oyna)
btn_0.setGeometry(9 + button_width + button_spacing, button_height_map+67, button_width, 60)
btn_0.setStyleSheet("font-size: 18px;")
btn_0.clicked.connect(button_0)

btn_res = QPushButton("=", oyna)
btn_res.setGeometry(9 + 2 * (button_width + button_spacing), button_height_map+67, button_width, 60)
btn_res.setStyleSheet("""
font-size: 25px;
color: green;
font-weight: bold;
                        """)
btn_res.clicked.connect(main_func)

btn_plus = QPushButton("+", oyna)
btn_plus.setGeometry(9 + 3 * (button_width + button_spacing), button_height_map+67, button_width, 60)
btn_plus.setStyleSheet("""
font-size: 25px;
color: blue;
font-weight: bold;
                        """)
btn_plus.clicked.connect(button_pul)
#-----------------------------------------------------------------------------------------------------------------------
btn_1 = QPushButton("1", oyna)
btn_1.setGeometry(9, button_height_map, button_width, 60)
btn_1.setStyleSheet("font-size: 18px;")
btn_1.clicked.connect(button_1)

btn_2 = QPushButton("2", oyna)
btn_2.setGeometry(9 + button_width + button_spacing, button_height_map, button_width, 60)
btn_2.setStyleSheet("font-size: 18px;")
btn_2.clicked.connect(button_2)

btn_3 = QPushButton("3", oyna)
btn_3.setGeometry(9 + 2 * (button_width + button_spacing), button_height_map, button_width, 60)
btn_3.setStyleSheet("font-size: 18px;")
btn_3.clicked.connect(button_3)

btn_minus = QPushButton("-", oyna)
btn_minus.setGeometry(9 + 3 * (button_width + button_spacing), button_height_map, button_width, 60)
btn_minus.setStyleSheet("""
font-size: 25px;
color: blue;
font-weight: bold;
                        """)
btn_minus.clicked.connect(button_min)

#-----------------------------------------------------------------------------------------------------------------------
btn_4 = QPushButton("4", oyna)
btn_4.setGeometry(9, button_height_map-65, button_width, 60)
btn_4.setStyleSheet("font-size: 18px;")
btn_4.clicked.connect(button_4)

btn_5 = QPushButton("5", oyna)
btn_5.setGeometry(9 + button_width + button_spacing, button_height_map-65, button_width, 60)
btn_5.setStyleSheet("font-size: 18px;")
btn_5.clicked.connect(button_5)

btn_6 = QPushButton("6", oyna)
btn_6.setGeometry(9 + 2 * (button_width + button_spacing), button_height_map-65, button_width, 60)
btn_6.setStyleSheet("font-size: 18px;")
btn_6.clicked.connect(button_6)
btn_multiply = QPushButton("*", oyna)
btn_multiply.setGeometry(9 + 3 * (button_width + button_spacing), button_height_map-65, button_width, 60)
btn_multiply.setStyleSheet("""
font-size: 25px;
color: blue;
font-weight: bold;
                        """)
btn_multiply.clicked.connect(button_mul)


#-----------------------------------------------------------------------------------------------------------------------

btn_7 = QPushButton("7", oyna)
btn_7.setGeometry(9, button_height_map-130, button_width, 60)
btn_7.setStyleSheet("font-size: 18px;")
btn_7.clicked.connect(button_7)

btn_8 = QPushButton("8", oyna)
btn_8.setGeometry(9 + button_width + button_spacing, button_height_map-130, button_width, 60)
btn_8.setStyleSheet("font-size: 18px;")
btn_8.clicked.connect(button_8)

btn_9 = QPushButton("9", oyna)
btn_9.setGeometry(9 + 2 * (button_width + button_spacing), button_height_map-130, button_width, 60)
btn_9.setStyleSheet("font-size: 18px;")
btn_9.clicked.connect(button_9)

btn_division = QPushButton("/", oyna)
btn_division.setGeometry(9 + 3 * (button_width + button_spacing), button_height_map-130, button_width, 60)
btn_division.setStyleSheet("""
font-size: 25px;
color: blue;
font-weight: bold;
                        """)
btn_division.clicked.connect(button_div)

# Vid-------------------------------------------
oyna.setStyleSheet("""
background-color: #A9A9A9; ;
                   """)
edt.setStyleSheet("""
background-color: white;
font-size: 30px;
                   """)

#-----------------------------------------------------------------------------------------------------------------------


oyna.show()
dastur.exec_()
