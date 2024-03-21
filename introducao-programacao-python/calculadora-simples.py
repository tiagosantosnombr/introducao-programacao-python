import os
import platform


# Checks the current operating system
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')  # Clears the console on Windows
    else:
        os.system('clear')  # Clears the console on Unix systems


clear_console()

primeiro_valor = float(input("Digite o primeiro valor: "))
segundo_valor = float(input("Digite o segundo valor: "))

soma = primeiro_valor + segundo_valor
subtracao = primeiro_valor - segundo_valor
multiplicacao = primeiro_valor * segundo_valor
divisao = primeiro_valor / segundo_valor
resto = primeiro_valor % segundo_valor

clear_console()

print(f"soma = {soma}")
print(f"subtração = {subtracao}")
print(f"multiplicação = {multiplicacao}")
print(f"divisão = {divisao}")
print(f"resto = {resto}")
