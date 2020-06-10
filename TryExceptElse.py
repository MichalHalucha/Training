try:
    Value = int(input("Podaj liczbe"))
except ValueError as e:
    for Arg in e.args:
        print(Arg)
else:
    if (Value > 0) and (Value <=10):
        print("Podales liczbe", Value)
    else:
        print("Podana wartosc nie prawidlowa")
