def bisiesto(anio):
    bisiesto=False
    if anio % 4 ==0:
        if anio % 100 ==0:
            if anio % 400==0:
                bisiesto=True
        else:
            bisiesto=True
    return bisiesto



def diasDelMes(mes, anio=2021):
    if mes!=2:
        dias=30
        if (mes > 7 and mes % 2==0) or (mes <= 7 and mes % 2==1):
                dias=31
    else:
        if(bisiesto(anio)):
            dias=29
        else:
            dias=28
    return dias

def FechaMasNdiasTuplas(dia,mes, anio, N): # Esta solucion es inválida para Algoritmos I, ya que utiliza tuplas
    while (N >0): # Las tuplas se usana a partir de Programacion I
        dias=diasDelMes(mes,anio)
        diasRestantesDelMes=dias-dia
        if N > diasRestantesDelMes:
            N=N-diasRestantesDelMes-1 # Le resto uno mas que los días restantes para pasar al mes siguiente
            dia=1
            mes=mes+1
            if mes == 13:
                mes=1
                anio+=1
        else:
            dia=dia+N
            N=0

    return dia,mes,anio # Tupla


def FechaMasNdias(dia,mes, anio, N):
    while (N >0):
        dias=diasDelMes(mes,anio)
        diasRestantesDelMes=dias-dia
        if N > diasRestantesDelMes:
            N=N-diasRestantesDelMes-1 # Le resto uno mas que los días restantes para pasar al mes siguiente
            dia=1
            mes=mes+1
            if mes == 13:
                mes=1
                anio+=1
        else:
            dia=dia+N
            N=0

    return [dia,mes,anio] # Lista (esto está permitido

#Programa
#E:


#Proceso

#dia,mes,anio=FechaMasNdias(dia,mes,anio,N)

#print (dia, mes, anio)



# Pruebas

print(FechaMasNdias(20,12,2022, 360))
print(FechaMasNdias(20,1,2023, 365))
print(FechaMasNdias(20,12,2024, 60))
print(FechaMasNdias(25,12,2024, 730))

dia=int(input("Ingrese dia:"))
mes=int(input("Ingrese mes:"))
anio=int(input("Ingrese anio:"))
N=int(input("Ingrese N:"))
L=FechaMasNdias(dia,mes,anio,N)

print (L[0], L[1], L[2])

"""
#Pruebas:
print (diasDelMes(1))
print (diasDelMes(2,2000))
print (diasDelMes(2,2001))
print (diasDelMes(3))
print (diasDelMes(4))
print (diasDelMes(5))
print (diasDelMes(6))
print (diasDelMes(7))
print (diasDelMes(8))
print (diasDelMes(9))
print (diasDelMes(10))
print (diasDelMes(11))
print (diasDelMes(12))
"""
