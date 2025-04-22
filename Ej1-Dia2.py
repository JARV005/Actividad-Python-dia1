
x = float(input("Introduce el primer número: "))
y = float(input("Introduce el segundo número: "))
z = float(input("Introduce el tercer número: "))


menor = x

if y < menor:
    menor = y
if z < menor:
    menor = z

print("El número más pequeño es:", menor)