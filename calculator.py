def calculadora ():
    print("1. Soma") 
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão") 
    operador = input("Qual operação deseja realizar:")
    valor1 = input('digite um numero: ')
    valor2 = input('digite outro numero: ')

    if operador == 1:
        resultado = valor1 + valor2 
        print(f'o resultado é: {resultado}')
    elif operador == 2:
        resultado = valor1 - valor2
        print(f'o resultado é: {resultado}')
    elif operador == 3:
        resultado = valor1 * valor2
        print(f'o resultado é: {resultado}')
    elif operador == 4:
        resultado = valor1/valor2 
        print(f'o resultado é: {resultado}')

calculadora()