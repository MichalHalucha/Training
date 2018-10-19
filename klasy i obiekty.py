import copy

"""Tworzenie obiektu jest zwane tworzeniem instancji klasy"""
class Point:
    """"klasa zawierajaca współrzędne środkowe"""
class Rectangle:
    """Klasa zawierająca rozmiar figury"""
def find_center(box):
    p = Point()
    p.x = box.corner.x + box.width / 2
    p.y = box.corner.y + box.height / 2
    return p
def print_point(center):
    print('(%g, %g)' % (center.x,center.y))

#punkt_srodkowy = Point()
#punkt_srodkowy.x = 3.0
#punkt_srodkowy.y = 2.0
#print("Punkt srodkowy x,y:",punkt_srodkowy.x, punkt_srodkowy.y)

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

center = find_center(box)
print_point(center)
#zmiana wartości
box.width = box.width+50
box.height=box.height+100

center = find_center(box)
print_point(center)

print("Kopia obiektu (nowy obiekt)")
#JEST FUNKCJA DO KOPIOWANIA WSZYSTKIEGO deepcopy. Nie kopiuje tylko obiektu lecz wszystko związane z tym obiektem
box1 = copy.copy(box)
center = find_center(box1)
print_point(center)

#MOŻEMY SPRAWDZIĆ CZY OBIEKT JEST INSTANCJĄ KLASY
print(isinstance(box,Rectangle))
#CZY OBIEKT MA OKREŚLONY ATRYBUT
print(hasattr(box,'x'))
#STR194