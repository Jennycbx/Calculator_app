from app import app
from modules import calculator


@app.route('/add/<number1>/<number2>')
def add(number1, number2):
    return f"The answer is {calculator.add(int(number1, number2))}"

@app.route('/subtract/<number1>/<number2>')
def subtract(number1, number2):
    return f"The answer is {calculator.subtract(int(number1, number2))}"

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    return f"The answer is {calculator.multiply(int(number1, number2))}"

@app.route('/divide/<number1>/<number2>')
def divide(number1, number2):
    return f"The answer is {calculator.divide(int(number1, number2))}"