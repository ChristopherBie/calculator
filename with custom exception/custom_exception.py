class CalculatorInputError(Exception):
    def __init__(self):
        super().__init__("No invalid input allowed!")
    pass