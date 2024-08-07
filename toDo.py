#---------------------------------------#
#     To-Do app personal project,       #
#        available for public.          #
#       Carlos Paredes Márquez          #
#       start date: 08/03/2024          #
#---------------------------------------#

from PySide6.QtWidgets import *     # import everything from QtWidgets
from PySide6.QtCore import *        # import everything from QtCore
#from PySide6.QtCore import Qt       
from PySide6.QtGui import QIcon

import sys                      # functions and variables that used in runtime environment
from pathlib import Path        # helps with various windows path operations

class Window(QMainWindow):

    def __init__(self, holder):
        super().__init__()
        self.setWindowTitle(" ")                # set the title void to not print Python in the window
        self.setWindowIcon(QIcon("2D.png"))     # set the logo that I created for the app
        self.setGeometry(100,100,400,200)        # set the geometry of the window
        self.UiComponents(holder)               # calling method
        self.task_to_do = []        # Saving task's in a list


    def UiComponents(self, holder):

        # creating a central display from the welcome title
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # creating the welcome messagge at the top & center
        main_layout = QVBoxLayout(central_widget)

        self.label = QLabel("Welcome 2Do")
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        main_layout.addWidget(self.label)

        content_layout = QHBoxLayout()

        # Left side layout
        left_layout = QVBoxLayout()

        self.task_list_widget = QListWidget()
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.task_list_widget)
        scroll_area.setFixedWidth(196)

        left_layout.addWidget(scroll_area)

        # Line edit for text entrance: add task
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText('Set new task')
        left_layout.addWidget(self.text_input)

        content_layout.addLayout(left_layout)

        right_layout = QVBoxLayout()

        # Line edit for text entrance: delete task
        self.text_input_remove = QLineEdit()
        self.text_input_remove.setPlaceholderText('Task number to delete')
        
        # Button to add a new task
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button = QPushButton("Add new task")
        button.clicked.connect(self.action_add_task)
        
        right_layout.addWidget(button)
        
        # Button to remove a task
        button_remove = QPushButton("Remove a task")
        button_remove.clicked.connect(self.action_remove_task)

        # Setting the right side ui
        right_layout.addWidget(button_remove)
        right_layout.addStretch()
        right_layout.addWidget(self.text_input_remove)

        content_layout.addLayout(right_layout)

        main_layout.addLayout(content_layout)

    def action_add_task(self):
        text = self.text_input.text()  # Read the text

        if (str(text) != '' and str(text) not in self.task_to_do):
            self.task_to_do.append(str(text))
            self.print_in_widget()
    
    def action_remove_task(self):
        if (self.text_input_remove.text() != ''):
            number = self.text_input_remove.text()
            n = int(number)
            n -= 1 
        
            if (n >= 0 and n < len(self.task_to_do)):
                self.task_to_do.pop(n)
                self.print_in_widget()
            elif (len(self.task_to_do) == 0):
                text = "No data to delete"
                self.task_list_widget.addItem(text)
    
    def print_in_widget(self):
        self.task_list_widget.clear()
        cont = 0

        for element in self.task_to_do:
            cont += 1
            text = "["+ str(cont) + "]" + str(element)
            self.task_list_widget.addItem(text)


if __name__ == '__main__':

    App = QApplication(sys.argv)
    holder = QWidget()
    window = Window(holder)
    window.show()

    sys.exit(App.exec())