entrada = input("Digite um número: ")

try: #Tente rodar
  numero = int(entrada) #Conversão de string (entrada) para inteiro
  if numero % 2 == 0: #Verifica se o número é par usando o operador de módulo %; retorna o resto da divisão: se for 0 é par, não é ímpar. 
    print(f"Este número é par: {entrada}")
  else:
    print(f"Este número é impar: {entrada}")
except ValueError:
  print("Você não passou um número inteiro.")