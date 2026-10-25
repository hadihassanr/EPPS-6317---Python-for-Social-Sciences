# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab7.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_frmGuess(object):
    def setupUi(self, frmGuess):
        if not frmGuess.objectName():
            frmGuess.setObjectName(u"frmGuess")
        frmGuess.resize(400, 300)
        self.guess_button = QPushButton(frmGuess)
        self.guess_button.setObjectName(u"guess_button")
        self.guess_button.setGeometry(QRect(30, 130, 100, 32))
        self.hint_button = QPushButton(frmGuess)
        self.hint_button.setObjectName(u"hint_button")
        self.hint_button.setGeometry(QRect(190, 130, 121, 32))
        self.guessTextLabel = QLabel(frmGuess)
        self.guessTextLabel.setObjectName(u"guessTextLabel")
        self.guessTextLabel.setGeometry(QRect(20, 160, 131, 16))
        self.timesGuessedLabel = QLabel(frmGuess)
        self.timesGuessedLabel.setObjectName(u"timesGuessedLabel")
        self.timesGuessedLabel.setGeometry(QRect(170, 160, 171, 16))

        self.retranslateUi(frmGuess)

        QMetaObject.connectSlotsByName(frmGuess)
    # setupUi

    def retranslateUi(self, frmGuess):
        frmGuess.setWindowTitle(QCoreApplication.translate("frmGuess", u"Guess a number between 1 and 100", None))
        self.guess_button.setText(QCoreApplication.translate("frmGuess", u"Guess...", None))
        self.hint_button.setText(QCoreApplication.translate("frmGuess", u"Give me a hint...", None))
        self.guessTextLabel.setText(QCoreApplication.translate("frmGuess", u"Number of guesses:", None))
        self.timesGuessedLabel.setText("")
    # retranslateUi

