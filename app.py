def switch (): 
    numero1 = int(input("introduzca el primer numero:"))
    numero2 = int(input("intruszca el segundo numeero"))
                  
eleccion = 0

while True:
    print("""
    indique la operacion a realizar:
         
    1) sumar     
    2) restar 
    3) multiplicar
    4) dividir
    5) cambiar los numeros introducidos
    6) salir de la calculadora   
    """ )    
     
    eleccion = int(input())



    if eleccion == 1:
       print(" ") 
       print("RESULTADO: ",numero1," + ",numero2," = ", numero1+numero2)   
    elif eleccion == 2:
       print("")    
       print("RESULTADO: ",numero1," - ",numero2, " = ", numero1-numero2)
    elif eleccion == 3:
       print("")
       print("RESULTADO: ",numero1," x ",numero2," = ",numero1*numero2)

    elif eleccion == 4:
       print("")
       print("RESULTADO: ",numero1," / ",numero2," = ",float(numero2/numero2))
    elif eleccion == 5:
       numero1 = int(input("introduzca el primer numero: ") )   
       numero2 = int(input("introduzca el segundo numero:") )
    elif eleccion == 6:
       print("Hasta pronto")   


def introducirnumeros ():
    global numero1, numero2
    numero1 = int(input("introduzca el primer numero") )
    numero2 = int(input("introduzca el segundo numero"))

def sumar (a,b):
    print("la suma de ",a,"+",b,"=",a+b)

def restar (a,b):
     print("la resta de ",a,"-",b,"=",a-b) 

def multiplicar (a,b):
    print("la multiplicacion de",a,"x",b,"=",a*b)

def division (a,b):
     if b == 0:
        print("no se puede dividir entre cero")    
     else:
        print("la division de ",a,"/",b,"=",a/b)


while True:
      print("""
       indique la opercion a realizar:
       1) sumar
       2) restar
       3) multiplicar
       4) dividir
       5) salir de la calculara
        """)
      eleccion = int(input())


if eleccion == 1:
        introducirnumeros()
        sumar(numero1,numero2) 
elif eleccion == 2:
    introducirnumeros()
    restar (numero1,numero2)
elif eleccion == 3:
    introducirnumeros()
    multiplicar(numero1,numero2)
elif eleccion == 4: 
    introducirnumeros()
    division(numero1,numero2)
elif eleccion == 5:
    print("Hasta pronto")
               
                  