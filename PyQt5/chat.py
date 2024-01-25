import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import openai

# API tokeningizni quyidagi qatori o'zgartiring
api_key = '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'
openai.api_key = api_key

class ChatGPTApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('ChatGPT with PyQt5')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel('User:')
        layout.addWidget(self.label)

        self.input_box = QLineEdit()
        layout.addWidget(self.input_box)

        self.button = QPushButton('Send')
        self.button.clicked.connect(self.get_chatgpt_response)
        layout.addWidget(self.button)

        self.output_label = QLabel('ChatGPT:')
        layout.addWidget(self.output_label)

        self.setLayout(layout)

    def get_chatgpt_response(self):
        user_input = self.input_box.text()
        chatgpt_response = self.request_chatgpt_response(user_input)
        self.output_label.setText(f'ChatGPT: {chatgpt_response}')

    def request_chatgpt_response(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        return response['choices'][0]['message']['content']

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chatgpt_app = ChatGPTApp()
    chatgpt_app.show()
    sys.exit(app.exec_())
