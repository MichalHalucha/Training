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

