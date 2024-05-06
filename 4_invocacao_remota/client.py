import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://localhost:8005')

numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

print(f"Soma ({numero1}+{numero2}): ",s.add(int(numero1), int(numero2)))
print(f"Multiplicação ({numero1}x{numero2}): ",s.mul(int(numero1), int(numero2)))
print(f"Potência ({numero1}^{numero2}): ",s.pow(int(numero1), int(numero2)))
print(f"Divisão ({numero1}/{numero2}): ",s.div(int(numero1), int(numero2)))
print(f"Subtração ({numero1}-{numero2}): ",s.sub(int(numero1), int(numero2)))