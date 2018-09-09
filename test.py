

thislist=["Hola","Diego","Molina"]

thislist.insert(0,"Holamundo")

print ("lista thislist:")

print (thislist)
hola=["Diegouno"]

for x in thislist:
    hola.append(x)
    pass

print("Lista hola:")

print(hola)

switcher = {
	"Hola": "eshola",
	"Diego": "esdiego",
	"Molina": "esmolina",
	"Diegouno": "esdiegouno",
	"Holamundo": "esholamundo"
	}
for argument in hola:
	print (switcher.get(argument,"nulo"))
	pass