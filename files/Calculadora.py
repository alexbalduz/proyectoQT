from functools import partial

ERROR_MSG = "ERROR"

class Calculadora:
    #Constructor de la calculadora
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    #Metodo para calcular el resultado
    def _calculateResult(self):
        #Evaluamos la expresion por si hay entradas no válidas
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    #Metodo para construir la expresion
    def _buildExpression(self, subExpression):
        #Si el texto de la pantalla es igual al mensaje de error, limpiamos la pantalla
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        #Concatenamos la expresion
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    #Metodo para conectar las señales y los slots
    def _connectSignalsAndSlots(self):
        #Conectamos los botones con sus respectivas funciones
        for keySymbol, button in self._view.buttonMap.items():
            #Si el simbolo no es igual a "=" o "C", conectamos el boton
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
        #Conectamos el boton "=" y el boton "C" con sus respectivas funciones
        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)