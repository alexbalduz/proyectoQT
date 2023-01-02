import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGridLayout, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget

ERROR_MSG = "ERROR"
WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40

from files.Calculadora import Calculadora

class PyCalcWindow(QMainWindow):
    #Constructor de la ventana prncipal
    def __init__(self):
        #Llama al constructor de la clase padre
        super().__init__()
        self.setWindowTitle("Calculadora de Alex")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()

    #Metodo para crear la pantalla
    def _createDisplay(self):
        #Crea el display
        self.display = QLineEdit()
        #Establece la altura de la pantalla
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        #Establece el alineamiento de la pantalla
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        #Crea los botones
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]
        #Agrega los botones a sus correspondientes posiciones
        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)

        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        #Establece el texto de la pantalla
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        #Devuelve el texto de la pantalla
        return self.display.text()

    def clearDisplay(self):
        #Limpia la pantalla
        self.setDisplayText("")


def evaluateExpression(expression):
    #Evalua la expresion por si hay entradas no válidas
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result

def main():
    #Crea la aplicacion y la ventana, funcion principal
    pycalcApp = QApplication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    Calculadora(model=evaluateExpression, view=pycalcWindow)
    sys.exit(pycalcApp.exec())

