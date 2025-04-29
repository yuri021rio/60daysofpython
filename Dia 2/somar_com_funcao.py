## Duas formas de escrever função em Python.
def somar_dois (numero1, numero2):
  somar = numero1 + numero2
  print(f"{somar}") #Exibir o valor da soma na tela
  return somar #retorna o valor da soma para possível reutilização em outras partes do código. 

##somar_dois(1,8) chama a função somar_dois passando 1 e 8 como argumentos. 

def somar_dois_numeros ():
  numero_1 = int(input("Digite o número 1: "))
  numero_2 = int(input("Digite o número 2: "))

  somar_dois_numeros = numero_1 + numero_2
  print(somar_dois_numeros)
  return somar_dois_numeros

somar_dois_numeros () #Chamar a função para ser executada. 