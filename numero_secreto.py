import random
import csv
nombre=input("Escribe tu nombre: ")
nombre=nombre[0:1].upper() + nombre[1:] #probando mayusculas
print("Hola", nombre)
numero_secreto=random.randint(1,100) #random es la libreria, randint la funcion dentro de esa libreria
print(numero_secreto)
intentos=0
while True: #bucle, donde lo de dentro del bucle lleva tabulación
    adivinanzauser= int(input("ESCRIBE UN NÚMERO DEL 1 AL 100: "))
    intentos=intentos+ 1
    #print(adivinanza)
    if adivinanzauser<numero_secreto: #si pasa esto entonces
        print("El número secreto es más alto")
    elif adivinanzauser>numero_secreto: #si no pasa lo anterior pero pasa esto
        print("El número secreto es más bajo ")
    else: #si no pasa nada de lo anterior, por eso va sin condición
        print(f"Enhorabuena, has acertado en {intentos} intentos")
        break #si acierta sale del bucle
archivo=open("resultados.csv", "a") #para guardar los datos obtenidos
archivo.write(nombre+","+str(intentos)+"\n")
archivo.close()
def mostrar_resultados():
    try:
        archivo=open("resultados.csv","r")
        lineas=archivo.readlines() #devuelve una lista de filas, cada una en un string
        #print("\n---Resultados de todos los usuarios---") no hace falta mostrarlo todo el rato
        lista_intentos=[] #para meter aqui los intentos
        nombres=[]
        for linea in lineas:
            print(linea.strip())
            partes=linea.strip().split(",") #separa el nombre y el intento como por celdas 
            intento=int(partes[1]) #se queda de "partes" solo con el intento que es el 1, nombre es 0
            lista_intentos.append(intento) # va a añadir a la lista cada intento (1,3,8,2,6...)
            nombres.append(partes[0])
        promedio=sum(lista_intentos)/len(lista_intentos)
        print("Promedio de intentos:",round(promedio,2))
        minimo=min(lista_intentos)
        maximo=max(lista_intentos)
        extitos_directos=lista_intentos.count(1)#esta contando solo aquellos aciertos a la primera, si qusieramos contar como exito otra cosa seria con bernouilli
        print("Número de exitos directos:", extitos_directos)
        total_usuarios=len(lista_intentos)
        if total_usuarios>0:
            tasa_exito=(extitos_directos/total_usuarios)*100
            print(f"El {tasa_exito.__round__(2)} % han acertado a la primera")
        else:
            print("Sin datos suficientes")
        mejores=[nombres[i] for i in range(len(lista_intentos)) if lista_intentos[i]==minimo]
        peores=[nombres[i] for i in range(len(lista_intentos))if lista_intentos[i]==maximo]
        print(f"El mejor resultado es {",".join(mejores)} con {minimo} intentos")
        print(f"El peor resultado es {",".join(peores)} con {maximo} intentos") 
        fracasos=[i-1 for i in lista_intentos]
        promedio_fracasos=sum(fracasos)/len(fracasos)
        print(f"El promedio de fracasos antes del exito es de {round(promedio_fracasos,2)}")
        bernouilli=[1 if i== 1 else 0 for i in lista_intentos] #el exito es acertar a la primera, la variable exitos_directos es lo mismo en este caso ya que el exito es acertar a la primera
        #print(bernouilli) no hace falta enseñarlo todo el rato
        prob_exito=sum(bernouilli)/len(bernouilli)
        print(f"Probabilidad de exito: {round(prob_exito,2)*100}%")
        prob_fracaso=(1-prob_exito)
        print(f"Probabilidad de fracaso: {round(prob_fracaso,2)*100}%")
        totalbernouilli=len(bernouilli) #mide el numero de indices (todos los intentos)
        exitosbernouilli=sum(bernouilli) #suma solo aquellos que son 1, es decir exitos
        print(f"De {total_usuarios} usuarios, {exitosbernouilli} acertaron a la primera")

    except FileNotFoundError:
     print("Aun no hay resultados registrados")
mostrar_resultados()
