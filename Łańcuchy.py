#Pobieranie znaków od tylu


#Funkcja ORD wkazuje miejsce litery w alfabecie
#print(ord('d')-ord('a'))


#LISTOWANIE ILOSCI WYRAZÓW W TEKSCIE
#tekst = "cos mfemwq cos dopqewdcos mepoocos"
#x = tekst.count("cos")
#print(x)


#word = "banan word"
#if word > "banan":
#    print("WOrd jest wczesniej")
#elif word > "banan":
#    print("word jest pozniej")


#Znajdywanie liter
#tekst = "error koekwpof error kdopqwkdopqw errorerror"
#def find_error(tekst,count):
#    for word in tekst:
#        if word == "e":
#            count = count + 1
#    return count
#print(find_error(tekst,count=0))
#x = tekst.find('error',2)
#print(int(x))

#Licznik który zlicza errory w lancuchu
#lancuch = "koepwkpofeopsakpockasopkcekosckapokcopaleasocksoapkcleaopskclxakce"
##count = 0
#for letter in lancuch:
#    if letter == "e":
#        count = count+1
#print(count)


#WYSZUKIWANIE
#word = "ZNAJDZ LITERE M"
#def find(word,letter, position):
#    index = position
#    while index < len(word):
#        if word[index] == letter:
#            return index
#        index = index+1
#    return -1
#print(find(word, "M", position=3))


#Fragment lancucha
#s = "Jedziemy na wakacje"
#print(s[0:8])
#"""Od początku"""
#print(s[:8])
#"""DO końca"""
#print(s[8:])
#print(s[:])


#fruit = "Pomarancza"
#for letter in fruit:
#    print(letter)


#LITEROWANIE
#letter = input("Podaj tytul")
#def literowanie(letter):
#    index = 0
#    while index < len(letter):
#        litera = letter[index]
#        index = index + 1
#        print(litera)
#literowanie(letter)

#WYDOBYWANIE LITER
#fruit = "pomarancza"
#length = len(fruit)
#last = fruit[length -1]
#print(last)