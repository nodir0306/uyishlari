from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QRadioButton, QMessageBox
from PyQt5.QtCore import QTimer

class LabelStyle(QLabel):
    def __init__(self, txt, parent=None):
        super().__init__(txt, parent)
        self.move(20, 60)
        self.setStyleSheet('font-size: 20px;')

class RadioStyle(QRadioButton):
    def __init__(self, txt, parent=None):
        super().__init__(txt, parent)
        self.setStyleSheet('font-size: 20px;')

class Button(QPushButton):
    def __init__(self, txt, parent=None):
        super().__init__(txt, parent)
        self.setStyleSheet('''
            QPushButton {
                font-size: 20px;
                background-color: lightblue;
                color: black;
            }
                           
            QPushButton:hover {
                font-size: 20px;
                background-color: blue;
                color: black;
            }
        ''')

class QuizWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.current_quiz = 1
        self.correct_answers = 0

        self.setup_questions()
        self.setup_ui()

    def setup_questions(self):
        self.question_1 = "Microsoft yaratuvchisi kim?"
        self.options_1 = ["Bill Gates", "Steve Jobs", "Mark Zuckerberg", "Elon Musk"]
        self.correct_option_1 = 0

        self.question_2 = "Fransiya poytaxti qayer?"
        self.options_2 = ["Berlin", "London", "Paris", "Madrid"]
        self.correct_option_2 = 2

        self.question_3 = "Apple asoschisi kim?"
        self.options_3 = ["Bill Gates", "Steve Jobs", "Mark Zuckerberg", "Elon Musk"]
        self.correct_option_3 = 1

        self.question_4 = "StarLink asoschisi kim?"
        self.options_4 = ["Bill Gates", "Steve Jobs", "Mark Zuckerberg", "Elon Musk"]
        self.correct_option_4 = 3
        
        self.question_5 = "Facebook asoschisi kim?"
        self.options_5 = ["Bill Gates", "Steve Jobs", "Mark Zuckerberg", "Elon Musk"]
        self.correct_option_5 = 2

        self.question_6 = "Ispaniya poytaxti bu?"
        self.options_6 = ["Berlin", "London", "Paris", "Madrid"]
        self.correct_option_6 = 3
        
        self.question_7 = "Viktus asoschisi?"
        self.options_7 = ["HP", "ACER", "MacBooc", "Lisa"]
        self.correct_option_7 = 3

        self.question_8 = "Operats?"
        self.options_8 = ["Machintosh", "Windows", "macOS", "Linux"]
        self.correct_option_8 = 0
        
        self.question_9 = "Antivirus dasturi?"
        self.options_9 = ["Windows", "Edit", "Depin", "Avast"]
        self.correct_option_9 = 3

        self.question_10 = "Text editorni toping?"
        self.options_10 = ["Windows", "macOS", "Notepad", "Avast"]
        self.correct_option_10 = 2

        self.total_questions = 10

    def setup_ui(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Quiz App")

        self.timer_label = QLabel("Qolgan vaqt: 120s", self)
        self.timer_label.move(20, 10)
        self.timer_label.setStyleSheet("font-size: 18px;")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)
        self.seconds_left = 120

        self.question_label = LabelStyle("", self)

        self.option_1 = RadioStyle("", self)
        self.option_1.move(40, 150)

        self.option_2 = RadioStyle("", self)
        self.option_2.move(40, 180)

        self.option_3 = RadioStyle("", self)
        self.option_3.move(40, 210)

        self.option_4 = RadioStyle("", self)
        self.option_4.move(40, 240)

        self.btn_next = Button("Next", self)
        self.btn_next.move(500, 350)
        self.btn_next.clicked.connect(self.next_quiz)

        self.btn_previous = Button("Previous", self)
        self.btn_previous.move(400, 350)
        self.btn_previous.clicked.connect(self.previous_quiz)
        self.btn_previous.hide()

        self.update_quiz()

    def update_quiz(self):
        current_question = getattr(self, f"question_{self.current_quiz}")
        current_options = getattr(self, f"options_{self.current_quiz}")
        self.correct_option = getattr(self, f"correct_option_{self.current_quiz}")

        self.question_label.setText(f"{self.current_quiz}. {current_question}")
        self.option_1.setText(current_options[0])
        self.option_2.setText(current_options[1])
        self.option_3.setText(current_options[2])
        self.option_4.setText(current_options[3])

        if self.current_quiz == self.total_questions:
            self.btn_next.setText("Finish")

        if self.current_quiz == 1:
            self.btn_previous.hide()
        else:
            self.btn_previous.show()

    def next_quiz(self):
        if self.check_answer():
            self.correct_answers += 1

        self.current_quiz += 1

        if self.current_quiz > self.total_questions:
            self.show_result()
        else:
            self.update_quiz()

    def previous_quiz(self):
        if self.current_quiz > 1:
            self.current_quiz -= 1
            self.update_quiz()

    def check_answer(self):
        selected_option = -1

        if self.option_1.isChecked():
            selected_option = 0
        elif self.option_2.isChecked():
            selected_option = 1
        elif self.option_3.isChecked():
            selected_option = 2
        elif self.option_4.isChecked():
            selected_option = 3

        return selected_option == self.correct_option

    def update_timer(self):
        self.seconds_left -= 1
        self.timer_label.setText(f"Qolgan: {self.seconds_left}s")

        if self.seconds_left == 0:
            self.timer.stop()
            self.show_result()

    def show_result(self):
        self.timer.stop()

        result_msg = QMessageBox()
        result_msg.setIcon(QMessageBox.Information)
        result_msg.setWindowTitle("Test natijasi")
        result_msg.setText(f"Siz {self.total_questions} ta savoldan dan {self.correct_answers}   tasiga javob berdingiz.")
        result_msg.setStandardButtons(QMessageBox.Ok)

        retval = result_msg.exec_()

        if retval == QMessageBox.Ok:
            self.close()

if __name__ == '__main__':
    app = QApplication([])
    quiz_window = QuizWindow()
    quiz_window.show()
    app.exec_()
