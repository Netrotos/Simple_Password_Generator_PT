import random
import string

errormessage="Utiliza um número valido"

carac=int(input("Quantos carateres queres (8-16)? "))
while carac<8 or carac>16:
    print (errormessage)
    carac=int(input("Quantos carateres queres (8-16)? "))

num=int(input("Quantos numeros queres (0-5)? "))
while num<0 or num>5:
    print (errormessage)
    num=int(input("Quantos numeros queres (0,5)? "))

scarac=int(input("Quantos carateres especiais queres (0-3)? "))
while scarac<0 or scarac>3:
    print (errormessage)
    scarac=int(input("Quantos carateres especiais queres (0-3)? "))
    
#acima 100% Nuno; abaixo nao
    
scaracopt = [".", "+", "_", "-"]
scaracf = random.choices(scaracopt, k=scarac)

numf = ""
for _ in range(num):
    numopt = random.randint(1, 9)
    numf += str(numopt)

letter=carac-(num+scarac)
letterf = random.choices(string.ascii_letters, k=letter)

passw = ''.join(letterf + list(numf) + scaracf)

print(passw)
    
