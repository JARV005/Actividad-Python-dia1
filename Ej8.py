x=input("Ingrese su peso en Kg ")
x=float(x)
y=input("Ingrese su altura en m ")
y=float(y)

imc=(x/(y*y))

if imc<18.5:
    print("Bajo peso")

if 18.5>=imc<=24.9:
    print("Normal")

if 25>=imc<=29.9:
    print("Sobrepeso") 

if imc>=30:
    print("Obesidad")       

print(imc)