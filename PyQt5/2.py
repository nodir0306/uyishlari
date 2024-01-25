from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

dastur = QApplication([])
oyna = QWidget()
oyna.setFixedSize(310,250)

lbl1 = QLabel("First name: ", oyna)
lbl1.move(20, 20)
lbl1.setStyleSheet("""
font-size: 18px;
                """)

edt1 = QLineEdit(oyna)
edt1.move(150, 20)

lbl2 = QLabel("Last name: ", oyna)
lbl2.move(20, 80)
lbl2.setStyleSheet("""
font-size: 18px;
                """)

edt2 = QLineEdit(oyna)
edt2.move(150, 80)

lbl3 = QLabel("Phone number: ", oyna)
lbl3.move(20, 140)
lbl3.setStyleSheet("""
font-size: 18px;
                """)
edt3 = QLineEdit(oyna)
edt3.move(150, 140)

btn = QPushButton("Add user", oyna)
btn.setGeometry(20, 180, 270, 50)
btn.setStyleSheet("""
font-size: 20px
                """)

def adduser():
    first_name = edt1.text()
    last_name = edt2.text()
    phone_number = edt3.text()

    user_dict = {
        "First Name": first_name,
        "Last Name": last_name,
        "Phone Number": phone_number
    }
    edt1.clear()
    edt2.clear()
    edt3.clear()

    with open("user.txt", "a") as file:
        file.write(str(user_dict) + "\n")
    

btn.clicked.connect(adduser)

oyna.show()
dastur.exec_()
