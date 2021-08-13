import os
from time import sleep
print("Bienvenido a mi laboratorio") 
option1=int(input("Para ingresar los datos de el o los pacientes usando una queue\nPresione 1.\nPara ingresarlos usando un stack\nPresione 2.\n"))
sleep(2)#Waiting two seconds
os.system('cls')#Clearing screen
if option1==1:
    datos_de_hoy=[]
    i=1
    while i!=0:
        option=int(input("Presione 1 para guardar la información de un paciente\nPresione 2 para salir\n "))
        if option==1:
            age=input("Ingrese la edad del paciente: ")
            indicator=input("Ingrese el indicador del paciente: ")
            data=age+','+indicator
            datos_de_hoy.append(data)
        elif option==2:
            i=0
        else:
            print("Opcion inválida. Intente de nuevo\n")
    sleep(2)#Waiting two seconds
    os.system('cls')#Clearing screen
    if len(datos_de_hoy)==0:
        print("Cero pacientes registrados. Esperamos que haya terminado la pandemia")
    else:
        while len(datos_de_hoy)!=0:
            element=datos_de_hoy[0].split(',')
            print("La edad del paciente es: ", element[0])
            indicator=float(element[1])
            print("El indicador del paciente es: ", indicator)
            if indicator>=0.8:
                print("POSITIVO. El paciente tiene COVID")
            else:
                print("NEGATIVO. El paciente no tiene COVID")
            datos_de_hoy.pop(0)
    print(datos_de_hoy)
elif option1==2:
    datos_de_hoy=[]
    i=1
    while i!=0:
        option=int(input("Presione 1 para guardar la información de un paciente\nPresione 2 para salir\n "))
        if option==1:
            age=input("Ingrese la edad del paciente: ")
            indicator=input("Ingrese el indicador del paciente: ")
            data=age+','+indicator
            datos_de_hoy.append(data)
        elif option==2:
            i=0
        else:
            print("Opcion inválida. Intente de nuevo\n")
    sleep(2)#Waiting two seconds
    os.system('cls')#Clearing screen
    if len(datos_de_hoy)==0:
            print("Cero pacientes registrados. Esperamos que haya terminado la pandemia")
    else:
        while len(datos_de_hoy)!=0:
            length=len(datos_de_hoy)-1
            element=datos_de_hoy[length].split(',')
            print("La edad del paciente es: ", element[0])
            indicator=float(element[1])
            print("El indicador del paciente es: ", indicator)
            if indicator>=0.8:
                print("POSITIVO. El paciente tiene COVID")
            else:
                print("NEGATIVO. El paciente no tiene COVID")
            datos_de_hoy.pop()
    print(datos_de_hoy)
else:
    print("Opción inválida. Intente de nuevo.")