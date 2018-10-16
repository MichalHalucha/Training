import math
#print(eval('1+2*3'))
#print(eval('math.sqrt(5)'))
#print(eval('type(math.pi)'))
#

#METODA NEWTONA
#x = int(input("Podaj"))
#a = int(input("Podaj"))
#print(float((x+a/x)/2))


#przydatny WHILE
#def wprowadz():
#    while True:
#        line = input("Podaj teskt ")
#        if line == "gotowe":
#            break
#        print(line)
#wprowadz()


#def factorial(n):
#    """Oblicza rekurencyjnie silnię z n."""
#    if n == 0:
#        return 1
#    else:
#        recurse = factorial(n - 1)
#        result = n * recurse
#        return result
#def estimate_pi():
#   """Oblicza przybliżenie liczby pi.
#
#   Algorytm autorstwa Srinivasa Ramanujana dostępny pod adresem
#  https://pl.wikipedia.org/wiki/Pi
# """
#    total = 0
#    k = 0
#    factor = 2 * math.sqrt(2) / 9801
#    while True:
#        num = factorial(4 * k) * (1103 + 26390 * k)
#        den = factorial(k) ** 4 * 396 ** (4 * k)
#        term = factor * num / den
#        total += term
#
#        if abs(term) < 1e-15:
#            break
#        k += 1
#    return 1 / total
#print(estimate_pi())