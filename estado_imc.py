# Módulo estado IMC

def definir_estado(imc):
    estado = 'Vazio'
    if imc < 18.5:
        estado = 'Abaixo do peso'

    elif imc >= 18.5 and imc < 25.00:
        estado = 'Peso ideal'

    elif imc >= 25.00 and imc < 30.00:
        estado = 'Levemente acima do peso'

    elif imc >= 30.00 and imc < 35.00:
        estado = 'Obesidade grau 1'

    elif imc >= 35.00 and imc < 40.00:
        estado = 'Obesidade grau 2'

    else:
        estado = 'Obesidade grau 3'

    print(f'O IMC do paciente é : {imc:.2f} - {estado}')

def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    definir_estado(imc)
