from ctypes.wintypes import HMENU


nome = "JúLIa"


print(nome.upper())
print(nome.lower())
print(nome.title())


texto = "   Óla, mundo!   "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")


menu =  "Python"

print("###" + menu + "####")
print(menu.center(14))
print(menu.center(20, "#")) 

#Fatiamento 