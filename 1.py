#import pizza
# i can impoer make_pizza method as mp and change name of method in main funcktion
from pizza import make_pizza
import skladniki
import myCars

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

def sum (n,m=0):
    if m!=0:
        return n + m
    elif type(n)==list:
        return n[0]+n[1]

if __name__=='__main__':
    print("Main:")
    assert sum(16, 15) == 31, "EXAMPLE"
    assert sum([16, 16]) == 32, "result - missing 1 required positional"

    user_profile = build_profile('albert', 'einstein',
                                 location='princeton',
                                 field='physics')
    print(user_profile)

    """import pizza
    make_pizza(16, 'pepperoni')
    make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')"""
    #import only method
    make_pizza(16, 'pepperoni')
    make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


    myPizza = skladniki.Skladniki('Marga',5)
    print(myPizza.name,myPizza.how_many)
    myPizza.fire()

    myCar = skladniki.Cars('Opel',2)
    print(myCar.name,myCar.how_many)
    #Klasa Cars dziedziczy po skladniki, ma te same argumenty i może wykorzystywać metody. Obiekt inaczej się nazywa. Nie my pizza tylko My Car
    myCar.fire()
    myCar.run_auto()

