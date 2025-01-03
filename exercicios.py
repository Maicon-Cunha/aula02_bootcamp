import math
# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

#numero_01 = int(input("Digite um numero inteiro: "))
#numero_02 = int(input("Digite outro numero inteiro: "))
#resultado = numero_01 + numero_02
#print("A soma é:", resultado)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

#numero = int(input("Digite um numero: "))
#calculo = numero // 5
#print("O resto da divisão por 5 é:", calculo)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

#numero_01 = float(input("Digite o primeiro número: "))
#numero_02 = float(input("Digite o segundo número: "))
#multiplicacao = numero_01 * numero_02
#print("O resultado da multiplicação é:", multiplicacao)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

#try:
#numero_01 = int(input("Digite o primeiro número: "))
#numero_02 = int(input("Digite o segundo número: "))
#divisao = numero_01 / numero_02
#print(divisao)
#except:
 #   print("integer division or modulo by zero")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

#numero = int(input("Insira um número: "))
#quadrado = (numero)**2
#print("O quadrado do número é:", quadrado)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

#numero_01 = float(input("Escreva o primeiro numero: "))
#numero_02 = float(input("Escreva o segundo numero: "))
#soma = numero_01 + numero_02
#print(f"A soma dos números é: {soma}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

#numero_01 = float(input("Escreva o primeiro numero: "))
#numero_02 = float(input("Escreva o segundo numero: "))
#media = (numero_01 + numero_02) /2
#print(f"A média dos números é: {media}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

#base = float(input("Insira a base: "))
#expoente = float(input("Insira o expoente: "))
#resultado = (base)**expoente
#print(f"O resultado de {base} elevado a {expoente} é: {resultado}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

#celsius = float(input("Insira a temperatura em graus Celsius: "))
#fator = celsius * (9/5) + 32
#print(f"O resultado de Celsius p Fahrenheit é: {fator}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

#raio_do_circulo = float(input("Digite o raio: "))
#area_do_circulo = math.pi * raio_do_circulo ** 2
#print(f"{area_do_circulo: .2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

#texto = input("Digite um texo para deixar maiúsculo: ").upper()
#print(texto)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

#texto = input("Digite seu nome completo: ").lower()
#print(texto)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

#texto = input("Digite uma frase: ").strip()
#print(texto)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

#data = input("Insira uma data no formato dd/mm/aaaa: ")
#lista_dia_mes_ano = data.split("/")
#print(f"O dia é: {lista_dia_mes_ano[0]}")
#print(f"O mes é: {lista_dia_mes_ano[1]}")
#print(f"O ano é: {lista_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

#palavra01 = input("Insira a primeira palavra: ")
#palavra02 = input("Insira a segunda palavra: ")
#uniao = palavra01 + palavra02
#print(uniao)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

#valor1 = True
#valor2 = True
#resultado_and = valor1 and valor2
#print("Resultado do AND lógico:", resultado_and)


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

#valor1 = input("Digite o primeiro valor (True ou False): ")
#valor2 = input("Digite o segundo valor (True ou False): ")
#resultado_or = valor1 or valor2
#print("Resultado do OR lógico:", resultado_or)


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# Solicita o valor booleano do usuário
#valor = input("Digite um valor booleano (True ou False): ")

# Converte a entrada para booleano
#valor = valor.strip().capitalize() == "True"

# Inverte o valor
#valor_invertido = not valor

# Exibe o valor invertido
#print(f"O valor invertido de {valor} é: {valor_invertido}")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# Solicita os dois números ao usuário
#numero1 = float(input("Digite o primeiro número: "))
#numero2 = float(input("Digite o segundo número: "))

# Compara os números
#sao_iguais = numero1 == numero2

# Exibe o resultado
#if sao_iguais:
 #   print(f"Os números {numero1} e {numero2} são iguais.")
#else:
 #   print(f"Os números {numero1} e {numero2} são diferentes.")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# Solicita os dois números ao usuário
#numero1 = float(input("Digite o primeiro número: "))
#numero2 = float(input("Digite o segundo número: "))

# Compara os números
#sao_diferentes = numero1 != numero2

# Exibe o resultado
#if sao_diferentes:
 #   print(f"Os números {numero1} e {numero2} são diferentes.")
#else:
 #   print(f"Os números {numero1} e {numero2} são iguais.")

# #### try-except e if

# 21: Conversor de Temperatura

#try:
#    celsius = float(input("Insira a temperatura em graus Celsius: "))
#    fator = celsius * (9/5) + 32
#    print(f"O resultado de Celsius p Fahrenheit é: {fator}")
#except ValueError:
#     print("Insira um valor válido")

# 22: Verificador de Palíndromo

#entrada = input("Digite uma palavra ou frase: ")
#if isinstance(entrada, str):
#    formatado = entrada.replace(" ", "").lower()
#    if formatado == formatado[::-1]:
#        print("É um palíndromo.")
#    else:
#        print("Não é um palíndromo.")
#else:
#    print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# 23: Calculadora Simples

#try:
#    num1 = float(input("Digite o primeiro número: "))
#    num2 = float(input("Digite o segundo número: "))
#    operador = input("Digite o operador (+, -, *, /): ")
#    if operador == "+":
#        resultado = num1 + num2
#    elif operador == "-":
#        resultado = num1 - num2
#    elif operador == "*":
#        resultado = num1 * num2
#    elif operador == "/":
#        resultado = num1 / num2
#    else:
#        print("Operador inválido ou divisão por zero.")
#    print("Resultado: ", resultado)
#except ValueError:
#    print("Erro: Entrada inválida. Certifique-se de inserir números.")

# 24: Classificador de Números
#try:
#    numero = int(input("Digite um número: "))
#    if numero > 0:
#        print("Positivo")
#    elif numero < 0:
#        print("Negativo")
#    else:
#        print("Zero")
#    if numero % 2 == 0:
#        print("Par")
#    else:
#        print("Ímpar")
#except ValueError:
#    print("Por favor, digite um número inteiro válido.")

# 25: Conversão de Tipo com Validação

entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")
