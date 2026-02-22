import numpy as np
import fitnessPlan

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self): #reminder def is declaring a function
        super().__init__()

        self.title = QtWidgets.QLabel("Well Being Fitness", alignment=QtCore.Qt.AlignCenter)
        self.button = QtWidgets.QPushButton("Start")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.button)

        self.questions = [  
            { "question": "Body Goal", "options": ["Lose", "Gain", "Maintain"]},
            {"question": "Equipment available to you", "options": ["None", "Gym", "Home"]},
            {"question": "Physical state", "options": ["Limitation","No Limitation", ""]},
            {"question": "level", "options": ["Beginner", "Advanced", ""]}]


        self.current_index = 0
        self.answers = []

        self.button.clicked.connect(self.next_question)

    def next_question(self):
        if self.current_index < 4:

            self.button.hide()
            x = self.questions[self.current_index]
            self.title.setText(x["question"])

            self.option1 = QtWidgets.QPushButton()
            self.option2 = QtWidgets.QPushButton()
            self.option3 = QtWidgets.QPushButton()

            self.layout.addWidget(self.option1)
            self.layout.addWidget(self.option2)
            self.layout.addWidget(self.option3)

            self.option1.setText(x["options"][0])
            self.option2.setText(x["options"][1])
            self.option3.setText(x["options"][2])

            self.option1.clicked.connect(lambda: self.store_answer(x["options"][0])) #reminder lamda ignores what the function return
            self.option2.clicked.connect(lambda: self.store_answer(x["options"][1]))
            self.option3.clicked.connect(lambda: self.store_answer(x["options"][2]))

        else:
            user_row = np.array([self.answers], dtype=object)
            category = fitnessPlan.finalPlan(user_row, fitnessPlan.km)
            labels = { 0: "Strength Training", 1: "Stretching/Yoga", 2: "Cardio" }
            self.title.setText(
    f"Based on our previous clients, it indicates that people who share the same factor as you prefer to: {labels[category[0]]}"
)

    def store_answer(self, answer):
        self.answers.append(answer)
        self.current_index += 1
        self.option1.deleteLater()
        self.option2.deleteLater()
        self.option3.deleteLater()
        self.next_question()

    def set_answer(self): 
        body = self.answers[0]
        equipment = self.answers[1]
        physical_state = self.answers[2]
        level = self.answers[3]
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.setStyleSheet("font-size: 24px; background-color: #71AFE2;")
    widget.show()

    rc = app.exec()
    sys.exit(rc)
