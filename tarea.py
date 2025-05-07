print ("este programa calcula el imc")  
B = float(input("peso del usuario: ")) 
while B > 500 or B < 0:  
       B =float(input("ingrese un peso valido: "))
A =float(input("altura del usuario en metros: ")) 
while A < 0 or  A > 2.50:
      A =float(input("ingrese una altura valido: "))
imc = B/A**2
print("tu imc es", imc)
if imc >= 0 and imc <= 18.49:
    print ("Delgado")
elif imc >= 18.50 and imc <= 24.99:
    print ("peso ideal")
elif imc >= 25.00 and imc <= 39.00:
    print ("obeso")
else: print ("obeso morbido")  