#-*-coding: utf-8 -*-
'''CALCULADORA DE MATRICES PROYECTO INTERSEMESTRAL PYTHON BÁSICO HECHO POR: ZÁRATE DÍAZ SOFÍA VIRIDIANA '''
#********************** Crea la matriz*******************************************
def crear_matriz(filas,filas2,columnas,columnas2,matriz1,matriz2,matrizresultante):#recibe a la cantidad de filas, columnas y las matrices para que las pueda crear 
    
    
   
    for i in range (filas):#Se crea la matriz con ayuda de un for y su limite son las filas, ya que se gregarán elementos de acuerdo al tamaño de las filas 
        matriz1.append([0]*columnas)#los elementos agregados en la lista se irán agregando con el tamaño de las columnas, append los agregará hasta el final de la lista  
        matriz2.append([0]*columnas)
        matrizresultante.append([0]*columnas)
#********************** Llena la matriz*******************************************
def llena_matriz(matriz1, matriz2):#Recibe las dos matrices que están en la función principal 
    for i in range (len(matriz1)):#se irán pidiendo datos hasta la longitud de la matriz para las filas
        for j in range(len(matriz1[i])):#para las columnas 
            matriz1[i][j]=float(input("Dame dato de la primera matriz[{},{}]=".format(i,j)))#se guardan los elementos ingresados , format sirve para ver la ubicación de los datos ingresados
    for i in range (len(matriz2)):#lo mismo para la segunda matriz
        for j in range(len(matriz2[i])):
            matriz2[i][j]=float(input("Dame dato de la segunda matriz[{},{}]=".format(i,j)))
#********************** Suma las matrices*******************************************  
def suma (filas,filas2,columnas,columnas2,matriz1,matriz2,matrizresultante): #recibe la cantidad de filas , columnas y las matrices creadas
   
    for i in range (filas): #se irá sumando elemento con elemento de acuerdo a la cantidad de filas y columnas
        for j in range (columnas): 
            matrizresultante[i][j]+= matriz1[i][j] + matriz2[i][j]#la matriz resultante se va recorriendo con += y las matrices se van sumando
    
    print("la matriz resultante es: "+str(matrizresultante))#se concatena con str y se pone el primer for ya que solo queremos el resultado
    return matrizresultante
    
#********************** Resta de matrices***********************************************
def resta(filas,filas2,columnas,columnas2,matriz1,matriz2,matrizresultante): #se hace lo mismo que la suma nada mas que las matrices se irán restando 
    for i in range (filas):
        for j in range (columnas):
            matrizresultante[i][j]+= matriz1[i][j] - matriz2[i][j]
    print("la matriz resultante es:"+str(matrizresultante))
    return matrizresultante
#********************** Multiplicacion de matrices *******************************************
def multiplicacion(filas,filas2,columnas,columnas2,matriz1,matriz2,matrizresultante): #se recibe la cantidad de filas, columnas y matrices 
    for i in range (filas):
        matrizresultante.append([0]*columnas2)#se crea la matriz resultante de acuerdo a las filas de la primera matriz y a las columnas de la segunda 
                
    for i in range (filas): 
        for j in range (columnas2): #Se hace un for anidado como en la suma, sin embargo su limite va a ser la segunda columna ya que en la multiplicacion de matrices se multiplica la fila y la columna 
                for h in range (columnas): #se utiliza utiliza otro for para que las matrices se vayan recorriendo como es cuadrada no importan si ponemos columnas o filas en su limite ya que será la misma cantidad 
                    matrizresultante[i][j]+=matriz1[i][h]*matriz2[h][j] #como en la multiplicacion se efectua fila por columna y como se suma el resultado la matriz se irá recorriendo con +=
    print("la matriz resultante es:"+str(matrizresultante)) #se concatena
    return matrizresultante
    
    
#********************** Llamada de funciones*******************************************
cadena="\t\t\t*****Bienvenido a la calculadora de matrices elija la operación que desee realizar****\n"      #Declaramos una cadena para utilizar la función upper
print(cadena.upper())#Se hacen mayúsculas
        
while True: #ciclo while para el menú 
    print("1: Suma, 2: Resta, 3: Multiplicacion(nxn), 4: Salir\n") #muestra las opciones del menú
    r=int(input("\t\t\tSeleccione una opción\n")) #guarda la respuesta 
    if(r==1): #condición en caso de que sea la primera opción 
        while True: #ciclo while en caso de que quiera repetir la operacion con otros valores 
            matriz1=[] #declaración de nuestras listas que están vacías 
            matriz2=[]
            matrizresultante=[]
            filas=int(input("Introduzca el numero de filas de su primera matriz: \n")) #Se introduce la cantidad de filas y columnas de ambas matrices 
            columnas=int(input("Introduzca el numero de columnas de su primera matriz: \n"))
            filas2=int(input("Introduzca el numero de filas de su segunda matriz: \n"))
            columnas2=int(input("Introduzca el numero de columnas de su segunda matriz: \n"))
            if(filas==filas2 and columnas==columnas2): #en caso de que las filas y columnas de ambas matrices sean iguales se puede efectuar la suma 
                crear_matriz(filas,filas2,columnas,columnas2,matriz1,matriz2,matrizresultante)#llamamos a la función crear matriz con nuestros argumentos
                llena_matriz(matriz1,matriz2)#llamamos a la funcion llena matriz
                suma(filas,filas2,columnas,columnas2,matriz1,matriz2,matrizresultante)#funcion para sumar matrices
                d=int(input("¿Desea un archivo txt con su resultado? 1: SI 2:NO\n"))#le preguntamos al usuario si quiere crear archivo txt
                if(d==1): #en caso de un si
                    f=open("matriz.txt", "w") #creamos el archivo con w
                    f.writelines("La suma es: "+str(matrizresultante)) #escribimos lo de la matriz resultante en el archivo 
                    f.close() #cerramos el archivo
                    h=int(input("¿Desea realizar otra suma? 1:SI 2:NO\n")) # agregamos una variable si quiere realizar una suma 
                    if(h==1):
                        continue #en caso de que se quiera repetir la operacion usamos la función continue para que siga el ciclo while 
                    if(h==2):
                        break #se rompe ciclo while para que ya no siga esta opcion y se regresa al menu
                    
                if(d==2):
                    t=int(input("¿Desea realizar otra suma? 1:SI 2:NO\n"))#en caso de que no quiera archivo txt pero si quiera realizar una suma otra vez 
                    if(t==1): #condición en caso de que la respuesta sea SI
                        continue
                    if(t==2):
                        break
            
            
            else:
                print("\t\t\tNo se puede realizar la suma") #si no se puede realizar la suma se rompe el ciclo con break 
                break
        
    elif (r==2): #condición en caso de que sea la segunda opción 
        while True:  #ciclo while en caso de que quiera repetir la operacion con otros valores 
            matriz1=[]
            matriz2=[] #ciclo while en caso de que quiera repetir la operacion con otros valores 
            matrizresultante=[]
            filas=int(input("Introduzca el numero de filas de su primera matriz: \n")) #guarda cantidad de filas y columnas 
            columnas=int(input("Introduzca el numero de columnas de su primera matriz: \n"))
            filas2=int(input("Introduzca el numero de filas de su segunda matriz: \n"))
            columnas2=int(input("Introduzca el numero de columnas de su segunda matriz: \n"))
            if(filas==filas2 and columnas==columnas2): #condicion igual que la suma 
                crear_matriz(filas,filas2,columnas,columnas2,matriz1,matriz2,matrizresultante) # se llama a las funciones 
                llena_matriz(matriz1,matriz2)
                resta(filas,filas2,columnas,columnas2,matriz1,matriz2,matrizresultante) #ahora a la funcion resta 
                d=int(input("¿Desea un archivo txt con su resultado? 1: SI 2:NO\n"))#variable en caso de que quiera archivo txt 
                if(d==1):#si lo quiere
                    f=open("matriz.txt", "w") #se crea
                    f.writelines("La resta es: "+str(matrizresultante))#escribe
                    f.close()
                    h=int(input("¿Desea realizar otra resta? 1:SI 2:NO\n")) #si desea realizar otra vez la operacion 
                    if(h==1):
                        continue
                    if(h==2):
                        break
                if(d==2):
                    t=int(input("¿Desea realizar otra resta? 1:SI 2:NO\n"))#en caso de que no quiera archivo txt se pregunta si quiere realizar otra vez la operacion 
                    if(t==1):
                        continue#se continua el ciclo while
                    if(t==2):
                        break #se rompe el ciclo 
            else:
                print("\t\t\tNo se puede realizar la resta") # si no se cumple se sale del while 
                break
    elif(r==3): #opcion para la multiplicacion
        while True: #while para que se repita la operacion en caso de que quiera el usuario
            matriz1=[]
            matriz2=[]
            matrizresultante=[] #declaración de listas 
            filas=int(input("Introduzca el numero de filas de su primera matriz: \n")) #se piden los valores de filas y columnas 
            columnas=int(input("Introduzca el numero de columnas de su primera matriz: \n"))
            filas2=int(input("Introduzca el numero de filas de su segunda matriz: \n"))
            columnas2=int(input("Introduzca el numero de columnas de su segunda matriz: \n"))
            if(filas==columnas and filas2==columnas2): #en caso de que todo sea igual ya que es cuadrada se efectúan las operaciones 
                crear_matriz(filas,filas2,columnas,columnas2,matriz1,matriz2,matrizresultante)
                llena_matriz(matriz1,matriz2)
                multiplicacion(filas,filas2,columnas,columnas2,matriz1,matriz2,matrizresultante)#ahora llamamos a la función multiplicación 
                d=int(input("¿Desea un archivo txt con su resultado? 1: SI 2:NO\n")) #en caso de querer archivo txt 
                if(d==1):
                    f=open("matriz.txt", "w") #se crea 
                    f.writelines("La multiplicacion es: "+str(matrizresultante))#escribe
                    f.close() #lo cierra
                    h=int(input("¿Desea realizar otra multiplicacion? 1:SI 2:NO\n")) #en caso de que quiera realizar una multiplicación
                    if(h==1):
                        continue #se continua el ciclo while
                    if(h==2):
                        break # se rompe 
                if(d==2):
                    t=int(input("¿Desea realizar otra multiplicacion? 1:SI 2:NO\n"))
                    if(t==1):
                        continue
                    if(t==2):
                        break
            
            else:
                print("\t\t\tNo se puede realizar la multiplicacion") # si no se puede realizar regresa al menú 
                break
    if(r==4):
        palabra="\t\t\tadios" #declramos la variable para que la convierta a mayúsculas
        print(palabra.upper())#lo convierte a mayúsuculas
        break #cierra el ciclo del menú en caso de que quiera salir 
    