from random import randint

#zad1

# a = [1 -x for x in range(1,11)]
# print(a)
#
# b = [4**y for y in range(8)]
# print(b)
#
# c = [z for z in b if z%2 == 0]
# print(c)

#zad2

# losowe = [randint(0,100) for x in range(10)]
# print(losowe)
#
# a = [x for x in losowe if x%2 == 0]
# print(a)

#zad3

# produkty = {"jajka":"szt", "cebula":"kg", "mleko":"szt", "jabłka":"kg", "chleb":"szt"}
# print(produkty)
#
# a = [produkt for produkt in produkty.keys() if produkty[produkt] =="szt"]
# print(a)

#zad4

# def trojkat(a,b,c):
#
#     if (a>b) & (a>c):
#         row = b**2 + c**2
#         if a**2 == row:
#             return "Trójkąt jest prostokątny"
#         else:
#             return "Trójkąt nie jest prostokątny"
#     elif (b>a) & (b>c):
#         row = a**2 + c**2
#         if b**2 == row:
#             return "Trójkąt jest prostokątny"
#         else:
#             return "Trójkąt nie jest prostokątny"
#     else:
#         row = a**2 + b**2
#         if c**2 == row:
#             return "Trójkąt jest prostokątny"
#         else:
#             return "Trójkąt nie jest prostokątny"
#
#
#
# a = input("Podaj dlugosc boku a \n")
# b = input("Podaj dlugosc boku b \n")
# c = input("Podaj dlugosc boku c \n")
# a = float(a)
# b = float(b)
# c = float(c)
# print(trojkat(a,b,c))

#zad5

# def trapez(a=1,b=1,h=1):
#    if(a<=0 | b<=0 | h<=0):
#        return "Podaj liczby"
#    else:
#        pole = (a + b) * h / 2
#        return pole
#
# print(trapez())

#zad6

# a = int(input("a:"))
# b = int(input("b:"))
# ile = int(input("ile:"))
# def iloczyn_ciagu(a = 1, b = 4, ile = 10):
#     return a + (b * ile)
#
# print(iloczyn_ciagu(a,b,ile))

#zad7

# a = int(input("a:"))
# b = int(input("b:"))
# ile = int(input("ile:"))
# def te_same_dzialania(*args):
#     return args[0] + (args[1] * args[2])
#
# print(te_same_dzialania(a,b,ile))

#zad8

# def zakupy(**wszystko):
#     produkty = len(wszystko)
#     if wszystko !=0:
#         suma = 0
#         ceny = [cena for cena in wszystko.values()]
#         print(ceny)
#         for x in range(len(ceny)):
#             suma+=float(ceny[x])
#
#     else:
#         return "Nie ma produktów"
#     return suma
# print(zakupy(jajka = 4, mleko = 5, baton = 2.69, picie = 4.20))