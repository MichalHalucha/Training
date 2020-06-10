try:
    Value = int(input("Podaj liczbe"))
except ValueError:
    print("Zła")
else:
    if (Value > 0) and (Value <=10):
        print("Podales liczbe", Value)
    else:
        print("Podana wartosc nie prawidlowa")
