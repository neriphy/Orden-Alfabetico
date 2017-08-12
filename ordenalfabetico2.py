#Creado por @neriphy

import webbrowser

elementos = 0
lista = []

elementos = int(input("¿Cuantos elementos agrara a la lista? "))
print("Ok, la lista contendra" , str(elementos), "elementos")


while elementos > 0:
	print("\nEsriba para agregar el elmento")
	palabra = input()
	lista.append(palabra)
	elementos = elementos - 1


print("Ok, la lista quedo de la siguiente forma: ")
lista.sort()
print(lista)

print("Si te servido este pequeño programa sigueme en Twitter")
webbrowser.open("https://twitter.com/neriphy")