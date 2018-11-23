import math
if __name__ == '__main__':
    godz = float(input("What hour is it?"))
    min = float(input("which minute is it?"))
    print(godz,min)

    print(godz,min)
    if godz > 12:
        godz=godz%12
    if min > 60:
        min=min%60

    hour_point = godz * 30
    min_point = min * 6

    print(hour_point,min_point)
    print("Różnica między wskazówkami =", math.fabs(min_point-hour_point))
