eng2sp = dict()
eng2sp['one']='uno'
print(eng2sp)
"""elementy w słowniku nigdy nie są indeksowane. Wywołując słownik możemy się zdziwić bo za każdym razem będzie inna kolejność"""
"""do słownika dostajemy się za pomocą klucza"""
print(eng2sp['one'])
print(len(eng2sp))
"""czy dany klucz ma wartość w słowniku"""
vals = eng2sp.values()
print ('one' in eng2sp)

#LICZNIK
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] +=1
    return d

#WZORZEC WYSZUKIWANIA W SŁOWNIKU
def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('wartość nie występuje w słowniku')
"""lookupError jest to funkcja wbudowana mówiąca o tym, że nie znaleziono"""

#FUNCKJA ODWRACAJĄCA SŁOWNIK
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

#ZMIENNA GLOBALNA
"""Jeżeli chcemy wywołać funkcje to wstawiamy zmienną globalną. Nie można robić tak, że zmieniamy tą zmienną"""
verbose = True
def example():
    """jeżeli byśmy tutaj zrobili verbose = True to tworzymy nową zmienna lokalną"""
    if verbose:
        print("uruchom tą funkcje jeżeli jest true")

"""aby możńa było w funkcji przypisać zmienną globalna musi ona zostać zdeklarowana"""
def example2():
    global verbose
    verbose = True



zmienna1 = 1
def jeden(zmienna1):
    zmienna1 = zmienna1+1
    print("Zmienna z funkcji 1=",zmienna1)
    return zmienna1
def dwa():
    global zmienna1
    zmienna1 = zmienna1+1
    print("Zmienna z funkcji 2 =",zmienna1)
    return zmienna1
dwa()
jeden(zmienna1)

