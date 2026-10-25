# Hadi Hassan
# EPPS 6317
# Lab 7 - Guessing Game
import sys
import random
from PySide6.QtWidgets import *
from PySide6.QtCore import Slot
from frmGuess import Ui_frmGuess

# Starting values for the game
times_guessed = 0
num_to_guess = random.randrange(1, 101)
# Program the hint button to give a hint
hint_number = num_to_guess + random.randrange(-5, 6)

class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()

        # Load the window layout I designed in Qt Designer
        self.ui = Ui_frmGuess()
        self.ui.setupUi(self)

        # Display the starting guess count
        self.ui.timesGuessedLabel.setText(str(times_guessed))
        # Connect the guess button to the guess_clicked
        self.ui.guess_button.clicked.connect(self.guess_click)
        self.ui.hint_button.clicked.connect(self.hint_click)

        self.show()
    @Slot()
    def hint_click(self):
        global times_guessed
        # take the current count and add five as a penalty
        times_guessed += 5
        self.ui.timesGuessedLabel.setText(str(times_guessed))
        # Needed in order to reference global variables
        QMessageBox.question(self, "Hint", "The secret number is within 5 of " + str(hint_number) + ".",
                             QMessageBox.Ok)
    def guess_click(self):
        # Needed in order to reference global variables
        global times_guessed
        global num_to_guess
        global hint_number
        # Prompt for a guess between 1 - 100
        guess, okPressed = QInputDialog.getInt(self, "Guess",
                                               "Enter a number between 1 and 100",
                                               1, 1, 100, 1)
        # If the user pressed OK, check the guess
        if okPressed:
            # Increment the guess count
            times_guessed += 1
            # Update the guess display
            self.ui.timesGuessedLabel.setText(str(times_guessed))
            # Check if guess too small
            if guess < num_to_guess:
                # Give a hint that the guess was too small
                QMessageBox.question(self, "Low", "Your guess is too low.",
                                     QMessageBox.Ok)
            # Else if too big
            elif guess > num_to_guess:
                # Give a hint that the guess was too big
                QMessageBox.question(self, "High", "Your guess is too high.",
                                     QMessageBox.Ok)
            # Else the guess is correct
            else:
                # Congratulate the user
                # I have added two congratualtions because on Mac it would not display if its not in the same ""
                QMessageBox.question(self, "Congratulations!", "Congratulations! You guessed right in " 
                                     + str(times_guessed) + " guesses.",
                                     QMessageBox.Ok)
                # Reset count
                times_guessed = 0
                # Reset display
                self.ui.timesGuessedLabel.setText(str(times_guessed))
                # Regenerate random number
                num_to_guess = random.randrange(1, 101)
                hint_number = num_to_guess + random.randrange(-5, 6)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Mainwindow()
    sys.exit(app.exec())