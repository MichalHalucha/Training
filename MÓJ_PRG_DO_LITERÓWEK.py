import string

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line,hist)
    return hist
def process_line(line,hist):
    line=line.replace('-'," ")

    for word in line.split():
        word = word.strip(string.punctuation+string.whitespace)
        word = word.lower()
        hist[word]=hist.get(word,0)+1
def sortowanie(hist):
    t = []
    for x, freq in hist.items():
        t.append((freq, x))
    print("GF - ILOŚĆ WYSTĄPIEŃ-LITERA", t)
    # SORTOWANIE MALEJĄCO
    t.sort(reverse=True)
    print("GF - SORTOWANIE MALEJĄCO", t)
    return t

def different_words(hist):
    return len(hist)

def total_words(hist):
    return sum(hist.values())
def subtract(d1,d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key]= "Brak"
    return res


hist = process_file('emma.txt')
print(hist)
x = sortowanie(hist)
print("Liczba słów w pliku:",different_words(hist))
print("Liczba wszystkich słów:",total_words(hist))
word = open("words.txt")
diff = subtract(hist,word)
print("SLOWA KTÓRYCH NIE MA")
print(x)
for word in x:
    print(word,end=' ')