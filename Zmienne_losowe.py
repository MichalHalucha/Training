import random

s = ['a','a','b']
#LICZNIK
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] +=1
    return d

def choose_from_hist(s):
    dict = histogram(s)
    print(dict)

choose_from_hist(s)


for i in range(10):
    x = random.random()
    print(x)
y = random.randint[1:5]
print(y)

t = [1,2,3]
z = random.choice(t)
print(t)

