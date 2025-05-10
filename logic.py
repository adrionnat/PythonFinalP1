import csv
import os.path
from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """This function initializes the gui and adds widgets"""
        super().__init__()
        self.setupUi(self)
        self.submit_button.clicked.connect(lambda :self.submit())

    def submit(self) -> None:
        """
        Check user submission to ensure completeness.
        In order to save to csv file, the user id must be unique, candidate must be selected, and id must be numerical
        """
        #collects user input
        id_number = self.id_input.text()
        if not id_number or not id_number.isdigit():
            self.label_under_button.setStyleSheet("color:red")
            self.label_under_button.setText("Enter valid ID")

        #Ensures button is selected
        if not self.buttonGroup.checkedButton():
            self.label_under_button.setStyleSheet("color:red")
            self.label_under_button.setText("Select Candidate")

        if self.radioButton_john.isChecked():
            vote = "John"
        if self.radioButton_jane.isChecked():
            vote = "jane"

        if os.path.exists('data.csv'):
            with open('data.csv', 'r', newline='') as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    if row[0] == id_number:
                        self.label_under_button.setStyleSheet("color:red")
                        self.label_under_button.setText("Already Voted")

        # saves to csv once requirements are met
        if id_number.isdigit() and self.buttonGroup.checkedButton():
            with open('data.csv', 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                csv_file.write('ID, Candidate\n')
                try:
                    if row [0] != id_number or not row:
                        writer.writerow([id_number, vote])
                        self.label_under_button.setStyleSheet("color:green")
                        self.label_under_button.setText("Vote submitted")
                        self.id_input.setFocus()
                        self.id_input.setFocus()
                        self.id_input.clear()

                        if self.buttonGroup.checkedButton() != 0:
                            self.buttonGroup.setExclusive(False)
                        self.buttonGroup.checkedButton().setChecked(False)
                        self.buttonGroup.setExclusive(True)

                except ValueError:
                    self.label_under_button.setText(text="Data not saved")
