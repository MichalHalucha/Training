krotka = tuple()
krotka1 = ('a','b','c','d')
"""krotki sa niezmienne, mozemy jedynie zastepować elementy"""
#t = ('A,') + krotka1[1:]

email = 'michal.halucha@gmail.com'
user,domain = email.split('@')
print(user,domain)

"""krotka w matmie"""
iloraz,reszta = divmod(7,3)
print(iloraz,reszta)

#funkce zwracajace min i max
t = '7','8','6','5'
def min_max(t):
    return min(t),max(t)
print(min_max(t))
"""funkcja sum dziala tylko na dwoch argumentach"""
#funkcja zip
for pair in zip(krotka1,t):
    print(pair)
print(list(zip(krotka1,t)))


for index, element in enumerate('abc'):
    print(index,element)

#items zwracajacy ciag krotek
d = {'a':0,'b':1,'c':2}
print(d.items())
for key, value in d.items():
    print(key,value)

