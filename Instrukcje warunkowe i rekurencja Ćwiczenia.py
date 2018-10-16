import math
import time


#CIĄG FIBONACCI
#x = input("podaj cyfre")
#n = int(x)
#def fibonacci(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        return n-1 + n-2
#y = fibonacci(n)
#print(y)


#Silnia
#x = input("Podaj cyfrę")
#n = int(x)
#def liczba(n):
#    if n == 0:
#        return 1
#    else:
#        recurse = liczba(n-1)
#        result = n*recurse
#        return result
#y = liczba(n)
#print(y)

#ZWRACANIE, RETURN, FUNKCJE BOOLEAN
#def is_between(x, y, z):
#    return x>=y>=z
#if is_between(1,2,2) == True:
#    print("Jest równe!")
#else:
#    print("Nie jest równe")

#FUNKCJA ZWRACAJĄCA PRZECIWPROSTOKĄTNĄ
#x = math.hypot(3,4)
#print(x)


#Obliczanie odcinków, Algebra liniowa
#def distance(x1,y1,x2,y2):
#    dx = x2-x1
#    dy = y2-y1
#    dsquared = dx**2 + dy**2
#    result = math.sqrt(dsquared)
#    return result


#ZWRACANIE WARTOŚCI
#x = 1
#y = 2
#def value(x,y):
#    if x>y:
#        print("1")
#        return x
#    elif x == y:
#        print("0")
#        return 0
#    elif x < y:
#        print("-1")
#        return -x
#value(x,y)

#FUNKCJA PRZYDATKA DO RYSOWANIA SPIRALI
#def recurse(n,s):
#    print(n)
#    print(s)
#    if n == 0:
#        print(s)
#    else:
#        recurse(n-1,n+s)
#recurse(3,0)


#BUDOWANIE TRÓJKĄTA
#patyk1 = input("patyk1")
#patyk2 = input("patyk2")
#patyk3 = input("patyk3")
#if patyk1 > patyk2+patyk3:
#    print("jest możliwe zbudowanie trójkąta!")
#elif patyk2 > patyk1+patyk3:
#    print("jest możliwe zbudowanie trójkąta!")
#elif patyk3 > patyk1+patyk2:
#    print("jest możliwe zbudowanie trójkąta!")
#else:
#    print("nie jest możliwe zbudowanie trójkąta!")


#TWIERDZENIE FERMATA NIE PRAWIDŁOWE
#a = b = c = input("Podaj cyfrę")
#a = int(a)
#b = int(b)
#c = int(c)
#def podaj_n():
#    n = input("Podaj n")
#    n = int(n)
#    if n>2:
#        c = a**n+b**n
#        wynik = c**n
#        print(wynik)
#        print(c)
#        print(wynik)
#        if c == wynik:
#            print("równa się!")
#        else:
#            print("nie równa się!")
#    else:
#        print("Żle podałeś")
#        podaj_n();
#podaj_n()


#CZAS
#time = time.localtime()
#print(time)


#Pobieranie znaków, STOSUNEK SYGNALU DO SZUMU
#sygnal = input("Sygnal")
#szum = input("Szum")
#x=float(sygnal)
#y=float(szum)
#ratio = x/y
#SNR=10 * math.log10(ratio)
#print(SNR)


#STABILIZACJA
#s = 2
#n = 4
#def stabilizacja(s,n):
#    if n<=0:
#        return
#    print(n)
#    stabilizacja(s, n -1)
#stabilizacja(s,n)


#Rekurencja, wywołanie samą siebie
#n=3
#def countdown(n):
#    if n <= 0:
#        print('Odpalenie!')
#    else:
#        print(n)
#        countdown(n-1)
#countdown(n)

#Boolean, IF, ELSE, ELIF
#type(True)
#if 5 == 6:
#    print("nie równa się")
#elif 5 == 5:
#    print("równa się")
#else:
#    print("coś poszło nie tak")


#OSTATNIA CYFRA, DWIE OSTATNIE CYFRY
#x = 215
#Ostatnia=x%10
#print(Ostatnia)
#Dwieostatnie=x%100
#print(Dwieostatnie)

#Czas trwania filmu
#czas_filmu = 130
#godzin = czas_filmu//60
#minut = czas_filmu-godzin*60
#print(godzin, minut)
#"""Druga możliwość"""
#wynik = czas_filmu%60
#print(godzin,wynik)