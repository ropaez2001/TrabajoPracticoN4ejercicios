"""Escriba una función que muestre todos los números primos entre 1 y un número n que
 es ingresado por parámetro.
 
Primos(numero ):
   
def NumeroPrimo():    
  numero =int(input( "Ingresar un numero:  "))
  if numero >1:
    cont=0
    for i in range (2,numero): 
        
       resto= numero % i 
       print( resto)
       
       if resto==0:
        cont+=1
        
    
    if cont==0:
           print("numero  es primo: ",numero)
    else:
        print(numero ,"no es un numero primo")
        
  else:      
         print("el numero es menor que 2 ")
       
NumeroPrimo()      """
#-------------------------------------------------------------------------------

"""2) Escriba una función que le pida al usuario ingresar condimentos para un sándwich, 
hasta que el usuario ingrese ‘salir’. 
Cada vez que se ingrese un condimento, 
muestre un mensaje avisando que ya se agregó el condimento al sándwich.
Escriba versiones diferentes del programa de acuerdo a estos criterios:
       
• Use un test condicional en el ciclo while para detener la ejecución.
• Use un test condicional dentro del ciclo para decidir si continuar la ejecución."""
    
"""def Sandwich():
       aderezos=[] 
       
       condimentos=input(" Ingresar condimentos : ")
       
       while condimentos!="salir":
              aderezos.append(condimentos)
              print("ya se agregó el", aderezos, "al sándwich: ")
              condimentos = input("Ingresar otro condimento (o 'salir' para terminar): ")
       print(" los condimentos agregados al sandwich son: ", aderezos)       
Sandwich()"""


# la otra version---------------------------------------------------------
"""def Sandwich():
       aderezos=[] 
       
       condimentos=input(" Ingresar condimentos : ")
       
       while True:
              
              if condimentos=="salir":
               break
               
              if condimentos not in aderezos:
                      aderezos.append(condimentos)
                      print("ya se agregó el", aderezos, "al sándwich: ")
               
                      condimentos = input("Ingresar otro condimento,(o 'salir' para terminar): ")
                      
              elif condimentos  in aderezos:
                 print(" Ingresar otro condimento, esta repetido")
                 condimentos=input(" Ingresar otro  condimento , (o 'salir' para terminar): ") : ")
              
       print(" los condimentos agregados al sandwich son: ", aderezos)
                            
Sandwich()"""
              
"""3) A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un
tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje
describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez
usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.
B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los
valores por defecto, y la segunda con valores diferentes. """    
#----------------------------------------------------------       
""" A)"""      
"""def hacer_remera(tamaño,mensaje):
        
        print(f"Su remera tiene tamaño {tamaño} y el mensaje es: {mensaje} ")
        
        return tamaño,mensaje
while True: 
 talle=input("Ingresar el tamaño de la remera: ")
 leyenda=input(" ingresar un mensaje a la remera: ")
 
 hacer_remera(talle,leyenda)"""
#----------------------------------------------------------
"""B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los
valores por defecto, y la segunda con valores diferentes. """

"""def hacer_remera(tamaño,mensaje):
        
        print(f"Su remera {i} tiene tamaño {tamaño} y el mensaje de la remera {i} es: {mensaje} ")
        
        return tamaño,mensaje
for i in range(1,3): 
 talle=input(f"Ingresar el tamaño de la remera numero {i}: ")
 leyenda=input(f" ingresar un mensaje a la remera numero {i}: ")
 
 hacer_remera(talle,leyenda)"""

#------------------------------------------------------------------       

"""4) Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros
de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo
número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …)."""
                  
"""def Fibonacci(numero1,numero2):
       
       cont=0
       while cont<=numero2 and cont <=10:
        numero1=numero1+numero2
        numero2=numero1+numero2
        print(numero1,numero2, end=" ")
        cont+=1
       return numero1,numero2
num1=0
num2=1

Fibonacci(num1,num2)"""