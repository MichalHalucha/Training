#listy proste
x = [2,7,6,4,6,4]
j = ["m","d","d","w","q"]
k = ["2","3","2","wiersz","32","samochod",[10, 20]]
"""Lista wewnątrz innej listy to lista zagnieżdżona"""
def sprawdź(litera):
    if litera in j:
        print("Jest!")
sprawdź("w")

#Przejscie i aktualizacja listy
for i in range(len(x)):
    x[i] = x[i] * 2
print(x)

wynikowa = j+k
print(wynikowa)
"""operator mnożenia powtarza listę n razy"""
"""operator wyodrębnienia przykład: j[1:3]"""
"""można też nadpisać elementry t[1:3]=['x','y']"""
"""Append, dodanie elementu do listy"""
"""extend pobiera liste jako argument i dodaje na koniec"""
"""sort sortuje liste alfabetycznie albo rosnąco"""

#sumowanie wszystkiego na liście
def sum_all(x):
    total = 0
    for y in x:
        total +=y
    return total
print(sum_all(x))

#Lub
w = sum(x)
print(w)

"""usuwanie elementów z listy"""
zmienna_usunieta = x.pop(1)
print(zmienna_usunieta)
#albbo del x[1]
x.remove(8)
print(x)
#del x[2:5]

#konwersja lancucha na liste
s = "spam"
t = list(s)
print(t)

#wyrazy w liscie
s = "chce-isc-spac"
delimiter = "-"
t = s.split(delimiter)
print(t)
#s= delimiter.join działa odwrotnie i zmienia liste na lancuch
def tail(t):
    return t[1:]
letters = ["a","b","c"]
rest = tail(letters)
print(rest)

"""FUnkcja t2 = sorted(t) zwraca liste posortowaną t2 oraz zachowuje oryginalna t"""
