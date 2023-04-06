import imp
from pydoc import doc
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QPixmap
from Ui_hangman import Ui_MainWindow
from datastore import Datastore

class MainWindow:
    def __init__(self):
        # Init UI elements
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        # Init App vars
        Self.db = Datastore()