import json

def greet_user():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")



numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)


filename = 'numbers.json'
with open(filename) as f_obj:
    #json.dump(username, f_obj)
    numbers = json.load(f_obj)
    print(numbers)


