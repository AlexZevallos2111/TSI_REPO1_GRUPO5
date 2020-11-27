while True:
    numero=int(input("Ingrese un numero: "))
    if numero>=0:
        break
    else: 
        print("Ingrese números naturales: ")

def primo(num1):
    primo=True 
    if num1==1 or num1==0:
        primo=False
    for i in range(2,num1):
        if (num1%i==0):
            primo=False
    
    return primo

print("El número " , numero , " es primo :" , primo(numero) )
