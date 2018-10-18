"""GF - GŁÓWNA FUNKCJA"""
def make_word_list1(file):
    """Wczytuje wiersze z pliku i buduje listę za pomocą funkcji append."""
    t = []
    fin = open(file)
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


def read_file(filename):
    """Zwraca zawartość pliku jako łańcuch."""
    return open(filename).read()

lancuch = "michalhalucha"
def most_frequent(lancuch):
    hist = make_histogram(lancuch)
    #ZAMIANA ILOŚĆ WYSTĄPIEŃ-LITERA, ZAMIANA NA LISTĘ
    t=[]
    for x, freq in hist.items():
        t.append((freq,x))
    print("GF - ILOŚĆ WYSTĄPIEŃ-LITERA",t)
    #SORTOWANIE MALEJĄCO
    t.sort(reverse=True)
    print("GF - SORTOWANIE MALEJĄCO",t)

    res = []
    for freq, x in t:
        res.append((freq,x))
    print("GF - WYNIKOWE",res)
    return res


#DWIE OPCJE HISTOGRAMU
def make_histogram(lancuch):
       """przyjmuje lancuch i zwraca slownik zawierajacy litere:ilosc wystąpień"""
       hist = {}
       for indeks in lancuch:
           hist[indeks] = hist.get(indeks, 0) + 1
       return hist


#Bardziej zrozumiala dla mnie forma histogramu
def histogram(lancuch):
    d = dict()
    for c in lancuch:
        if c not in d:
            d[c] = 1
        else:
            d[c] +=1
    return d

"""MAIN"""
print("Histogram trudna wersja",make_histogram(lancuch))
print("Histogram latwa wersja",histogram(lancuch))




text = read_file("emma.txt")
letter_seq = most_frequent(text)
for x in letter_seq:
    print("SZUKAMY!",x)

#ODCZYT PLIKU I WYŚWIETLENIE
words = make_word_list1("emma.txt")
print(words)