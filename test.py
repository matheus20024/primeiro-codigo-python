#primeiro código
print("Hello World")

#alisteamento exercito
nome = str(input("Digite seu nome: "))
idade = int(input("Dgite sua Idade: "))
if idade >= 18:
    print(f"Parabéns {nome} você vai para exercito brasileiro")
else:
    print(f"Parabéns {nome} você não vai para exercito brasileiro")

#operação
number1 = float(input("Digite o primeiro número: "))
number2 = float(input("Digite o segundo número: "))
operecao = (number1 + number2) * 2 / 10 + 15
print(operecao) 

#calculadora simples
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
print("Adição - 1")
print("Subtração - 2") 
print("Multiplicação - 3")
print("Divisão - 4")
print("Potenciação - 5")
calculadora = int(input("Digite a operação que deseja fazer? "))
if calculadora == 1:
    resultado = numero1 + numero2
    print(f"O resultado da adição primeiro e segundo é: {resultado}")
elif calculadora == 2:
    resultado = numero1 - numero2
    print(f"O resultado da subtração primeiro e segundo é: {resultado}")
elif calculadora == 3:
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação primeiro e segundo é: {resultado}")
elif calculadora == 4:
    resultado = numero1 // numero2
    print(f"O resultado da divisão primeiro e segundo é: {resultado}")
elif calculadora == 5:
    resultado = numero1 ** numero2
    print(f"O resultado da potenciação primeiro e segundo é: {resultado}")
else:
    print("Operador Inválido!")