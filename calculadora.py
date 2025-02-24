while True:
    numero1 = input('Digite o primeiro numero: ')
    numero2 = input('Digite o segundo numero: ')
    operador = input('Digite o operador ( +-*/ ): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero1)
        num_2_float = float(numero2)
        numeros_validos = True
    except:
       numeros_validos = None

    if numeros_validos is None:
        print("Algum dos numeros são invalidos!!")
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print("Operador invalido.")
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    calculo = 0
    if operador == '+':
        calculo = num_1_float + num_2_float
    elif operador == '-':
        calculo = num_1_float - num_2_float 
    elif operador == '/':
        calculo = num_1_float / num_2_float
    elif operador == '*':
        calculo = num_1_float * num_2_float
    
    print(f'O resultado da operação dos valores {num_1_float} {operador} {num_2_float} = {calculo}') 


    sair = input("Quer sair? [s]im: ").lower().startswith('s')

    if sair is True:
        break