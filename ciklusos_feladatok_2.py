import math
import random


# 1.	Írjuk ki a számokat 100-tól 1-ig visszafelé, 1 sorba 10 szám kerüljön
def elso_feladat():
    for szam in range(100, 0, -1):
        print(str(szam) + " ", end="")
        if szam % 10 == 1:
            print("")


# 2.	Írjuk ki 0-tól 150-ig a páros számokat
def masodikelso_feladat():
    for szam in range(0, 151, 1):
        if szam % 2 == 0:
            print(str(szam) + " ", end="")


def masodikmasodik_feladat():
    for szam in range(0, 151, 2):
        print(str(szam) + " ", end="")


# 3.	Írjuk ki 0-tól 150-ig a négyzetszámokat
def harmadik_feladat():
    for szam in range(0, 151, 1):
        print(str(int(math.pow(szam, 2))) + " ", end="")


# 5.	Írjuk ki egy TOTÓ szelvény lehetséges kitöltését
def otodik_feladat():
    for db in range(0, 14, 1):
        if db != 13:
            print(str(db+1) + ". tipp: ", end="")
        else:
            print("13+1. tipp: ", end="")
        tipp = random.randint(0, 2)
        if tipp == 0:
            print("x")
        else:
            print(tipp)


# 7.	Írjuk ki az első 100 szám összegét
def hetedik_feladat():
    osszeg = 0
    for szam in range(1, 101, 1):
        osszeg += szam
    print("Az első 100 száma összege: " + str(osszeg))
