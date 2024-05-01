import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://localhost:8005')

numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

print("Resultado da invocação da soma: ",s.add(int(numero1), int(numero2)))