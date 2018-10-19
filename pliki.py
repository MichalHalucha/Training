import os
import dbm
import pickle
import wc

try:
    file = open("data.txt", "w")
except:
    print("Nie ma takiej opcji")

x = 56
file.write("Plik bazy damych: %d " %x)
#file.write(str(x))
file.write("Ucze się już %d dzień %g %s..." %(3,0.1,'pythona'))
print(os.getcwd())
print(os.path.exists("pliki.py"))
file.close()

db = dbm.open('captions', 'c')
db['kaczka.png']='zdjecie_kaczki'
print(db['kaczka.png'])

#ITERACJA BAZY DANYCH
#for key in db:
#    print(key, db[key])
#db.close()

t=[1,2,3]
s=pickle.dumps(t)
print(s)
s = pickle.loads(s)
print(s)
db.close()

cmd = "ls"
fp = os.popen(cmd)
res = fp.read()
#print(res)"data.txt"
fp.close()
"""md5sum służy do porównywania plików. Oblicza sume kontrolną"""
print(wc.__name__)

#print(repr(s)
#zwraca łańcuch bez spacji itp