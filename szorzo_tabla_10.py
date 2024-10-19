# 9.	Írjuk ki a 10x10-es szorzótáblát

def kilencedik_feladat():
    # első sor
    print("   ", end="")
    for sor in range(1, 11, 1):
        print(str(sor) + " ", end="")
    print("")

    # első oszlop
    for szam in range(1, 11, 1):
        print(str(szam) + " ")

    # közepe
    for sor in range(1, 11, 1):
        for oszlop in range(1, 11, 1):
            print(str(sor * oszlop) + " ", end="")
        print("")


def szor10kesz():
    # első sor
    print("   ", end="")
    for sor in range(1, 11, 1):
        print(str(sor) + " ", end="")

    # első oszlop + közepe
    # közepe
    for sor in range(1, 11, 1):
        print(str(sor) + " ", end="")
        for oszlop in range(1, 11, 1):
            print(str(sor * oszlop) + " ", end="")
        print("")
