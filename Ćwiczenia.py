import math
import tkinter
import turtle




#Rysowanie kształtów
#t = turtle.Turtle()
#n = 30
#length = 150
#angle = -170
#def polyline(t, n, length, angle):
#    '''Rysuje n odcinków liniowych o długości, ilości odcinków i konta'''
#    for i in range(n):
#        t.fd(length)
#        t.lt(angle)
#polyline(t, n, length, angle)

#KWADRAT OGRĄG
#t = turtle.Turtle()
#length = 30
#n = 20
#r = length
#def circle(t,r = 100):
#    circumference=2*math.pi*r
#    n = 50
#    length = circumference/n
#def square(t,n, length):
#    angle = 360/n
#    for i in range(n):
#        t.lt(angle)
#        t.fd(length)
#circle(t,r)
#square(t,n,length)
#tkinter.mainloop()

#TURTLE RYSOWANIE KWADRATU
#t = turtle.Turtle()
#for i in range(4):
#    t.fd(100)
#    t.lt(90)
#print(t)
#tkinter.mainloop()


#RUSOWANIE PÓL ZA POMOCĄ FUNKCJI
#a = 11
#b = 11
#x = "+" + "-" * 4 + "+" + "-" * 4 + "+"
#y = "|" + " " * 4 + "|" + " " * 4 + "|"
#def do_twice(func, arg):
#    func(arg)
#    func(arg)
#def print_twice(arg):
#    print(arg)
#    print(arg)
#def do_four(func, arg):
#    do_twice(func, arg)
#    do_twice(func, arg)
#do_four(print_twice, "SPAM")
#def rysujkwadrat(a,b):
#    print("Plansza:"+ str(a) + "x" + str(b))
#    print(x)
#    do_twice(print_twice, y)
#    print(x)
#    do_twice(print_twice, y)
#    print(x)
#rysujkwadrat(a,b)


#WYWOŁYWANIE FUNKCJI W FUNKCJACH
#def do_twice(func, arg):
#    func(arg)
#    func(arg)

#def print_twice(arg):
#    print(arg)
#    print(arg)

#def do_four(func, arg):
#    do_twice(func, arg)
#    do_twice(func, arg)

#do_twice(print_twice, 'spam')
#print('')
#do_four(print_twice, 'spam')


#SPAM
#a = 2
#def do_twice(a):
#    print(a)
#    def print_spam():
#        do_twice(a)
#    print_spam()
#do_twice(a)


#WYŚWIETLANIE W ODPOWIEDNICH KOLUMNACH
#s = "monty"
#def right_justify(s):
#    def space():
#        print(" "*65 + s)
#    space()
#right_justify(s)


#FUNCKJA LOKALNA
#a=2
#b=3
#def lokalna(a,b):
#    x = a+b
#    print(x)
#lokalna(a,b)

#DEFINICJE
#def wierszyk():
#    print("Jestem")
#    print("Michal")

#def powtorz_wierszyk():
#    wierszyk()
#
#wierszyk()
#powtorz_wierszyk()


#STOSUNEK SYGNAŁU DO SZUMU
#signal_power = 10
#noise_power = 20
#ratio = signal_power/noise_power
#decibels = 10 * math.log10(ratio)
#radians = 0.7
#height = math.sin(radians)
#print(decibels,height)
#KONWERSJA STOPNI NA RADIANY
#degrees = 45
#radians = degrees / 180.0 * math.pi
#math.sin(radians)
#print(radians)
#x = math.sqrt(2)/2.0
#print(x)

#CZAS POWROTU DO DOMU
#JendaMila = (8*60)+15
#DrugaMila = (7*60)+12
#TrzeciaMila = JendaMila
#CzasPowrotu = JendaMila+DrugaMila+TrzeciaMila
#Final = CzasPowrotu/60
#print(Final)


#SPRZEDAŻ MASOWA KSIĄŻEK
#ilosc = 60
#koszt = 0
#cena = 24.95
#upust = (40*0.01)*24.95
#cenaupust = cena - upust
#print(upust)
#wysylka = 3
#wysylkamasowa = 0.75
#if(ilosc>1):
#    koszt = (ilosc*(cena-upust))+(ilosc*wysylkamasowa)
#    print(koszt)


#OBlICZANIE OBJETOŚCI
#promien = input("Podaj promien")
#y = float(promien)
#x = 4/3
#r = y**3
#pi = 3.14
#objetosc = x*pi*r
#print(objetosc)


#WARTOŚĆ PROCENTOWA GODZINY
#minute = 60
#procentage = (minute * 100)/60
#print(procentage)



