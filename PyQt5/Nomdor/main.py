import json
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox

app = QApplication([])
window = QWidget()
window.setFixedSize(310, 300)

lbl1 = QLabel("First name: ", window)
lbl1.move(20, 60)
lbl1.setStyleSheet("""
font-size: 18px;
                """)

edt1 = QLineEdit(window)
edt1.move(150, 60)

lbl3 = QLabel("Phone number: ", window)
lbl3.move(20, 110)
lbl3.setStyleSheet("""
font-size: 18px;
                """)
edt3 = QLineEdit(window)
edt3.move(150, 110)

btn = QPushButton("Ro'yxatdan o'tish", window)
btn.setGeometry(20, 180, 270, 50)
btn.setStyleSheet("""
font-size: 20px
                """)

sign_in = QPushButton("Kirish", window)
sign_in.setGeometry(20, 230, 270, 50)
sign_in.setStyleSheet("""
font-size: 20px
                """)


def user_exists(username, user_list):
    return any(user['username'] == username for user in user_list)

def add_user():
    first_name = edt1.text()
    phone_number = edt3.text()

    # Load existing user data or create an empty list if the file doesn't exist
    try:
        with open("user.json", "r") as file:
            user_list = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        user_list = []

    # Check if the username already exists
    if user_exists(first_name, user_list):
        QMessageBox.warning(window, 'Error', 'Ro\'yxatda mavjud bo\'lgan usernamedan foydalanildi.')
        return

    user_dict = {
        "username": first_name,
        "phone": phone_number
    }

    # Add the new user to the list
    user_list.append(user_dict)

    # Save the updated user data to the file
    with open("user.json", "w") as file:
        json.dump(user_list, file, indent=2)

    edt1.clear()
    edt3.clear()

btn.clicked.connect(add_user)


# sign in
def sign_in_page():
    for widget in window.findChildren(QWidget):
        widget.deleteLater()

    window.setFixedSize(310, 300)

    lbl_username = QLabel("Username: ", window)
    lbl_username.move(20, 60)
    lbl_username.setStyleSheet("""
    font-size: 18px;
                """)

    edt_username = QLineEdit(window)
    edt_username.move(150, 60)

    sign_in_btn = QPushButton("Kirish", window)
    sign_in_btn.setGeometry(20, 180, 270, 50)
    sign_in_btn.setStyleSheet("""
    font-size: 20px
                """)

    def sign_in_user():
        username = edt_username.text()
        greeting_label = QLabel(f"Salom, {username}!", window)
        greeting_label.move(20, 250)
        greeting_label.setStyleSheet("""
        font-size: 18px;
        """)

    sign_in_btn.clicked.connect(sign_in_user)

sign_in.clicked.connect(sign_in_page)

window.show()

app.exec_()
