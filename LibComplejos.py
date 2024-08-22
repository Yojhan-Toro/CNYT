import numpy as np

def division(a, b):

    parteE = round(((a[0]*b[0]) + (a[1]*b[1])) / ((b[0]**2)+(b[1]**2)),3)
    parteC = round(((b[0]*a[1]) - (a[0]*b[1])) / ((b[0]**2)+(b[1]**2)),3)

    return (parteE, parteC)

def suma(a, b):

    parteE = a[0] + b[0]
    parteC = a[1] + b[1]

    return (parteE, parteC)

def multiplicacion(a, b):

    parteE = (a[0]*b[0]) - (a[1]*b[1])
    parteC = (a[0]*b[1]) + (a[1]*b[0])

    return (parteE, parteC)

def conjugado(a):

    return (a[0], -a[1])


def modulo(a):

    return ((a[0]**2)+(a[1]**2))**(1/2)

def fase(a):

    return np.arctan(a[1]/a[0])

def polarCar(a, b):

    return round(-(a * np.cos(b)),2), round(-(a* np.sin(b)),2)


def prettyPritingC(a):

    a = (round(a[0],2), round(a[1],2))
    if a[1]<0:
        print(a[0]," - ",(-1)*a[1],"i", sep = "")
    else:
        print(a[0]," + ",a[1],"i", sep = "")




