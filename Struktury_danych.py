def make_word_list1():
    """Wczytuje wiersze z pliku i buduje listę za pomocą funkcji append."""
    t = []
    fin = open('emma.txt')
    for line in fin:
        word = line.strip()
        word = word.replace(" ","")
        word = word.replace(",", "")
        word = word.replace(".", "")
        word = word.lower()
        print(word)
        t.append(word)

    return t

t = make_word_list1()

s = "chce isc spac"
s.replace(" ","")
print(s)