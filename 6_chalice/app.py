from chalice import Chalice

app = Chalice(app_name='6_chalice')


@app.route('/')
def index():
    return {'Status': 'OK'}

@app.route('/calc')
def calc():
    operation = input('Informe a operação: [soma] [sub] [mult] [div] ')
    valor1 = int(input('Informe o primeiro valor: '))
    valor2 = int(input('Informe o segundo valor: '))
    if operation == 'soma':
        return {'A soma': valor1 + valor2}
    elif operation == 'sub':
        return {'A subtração': valor1 - valor2}
    elif operation == 'mult':
        return {'A multiplicação': valor1 * valor2}
    elif operation == 'div':
        return {'A divisão': valor1 / valor2}
    else:
        return {'Operação inválida'}


@app.route('/soma/{valor1}/{valor2}')
def soma(valor1, valor2):
    return {'A soma': int(valor1) + int(valor2)}

@app.route('/sub/{valor1}/{valor2}')
def sub(valor1, valor2):
    return {'A subtração': int(valor1) - int(valor2)}

@app.route('/mult/{valor1}/{valor2}')
def mult(valor1, valor2):
    return {'A multiplicação': int(valor1) * int(valor2)}

@app.route('/div/{valor1}/{valor2}')
def div(valor1, valor2):
    return {'A divisão': int(valor1) / int(valor2)}