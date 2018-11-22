bicycles = ['trek','cannondale','specialized','scott','dartmoor','nSbikes']
number_list = [2,5,4,3,2,1,6,7]
#MY
def changing_case(name):
    #This return strings with the same size of letters
    #print(name.lower())
    #print(name.upper())
    return name.title()

def combine_string(first_name,second_name):
    #rstrip remove whitespaces on the right and left sides but only temporaty. This not change string. (strip,lstrip rstrip)
    return (first_name.rstrip()+" "+second_name).title()

def calculate(first_number,symbol,second_number):
    return eval(first_number+symbol+second_number)

def add_to_list(list,item):
    list.append(item)
    return list

def insert_to_list(list,position,item):
    list.insert(position,item)
    return list

def remove_position(list,position):
    del list[position]
    return list

def pop_position(list,position):
    #pop() - getting last position from list
    item = list.pop(position)
    return item

def remove_name(list,name):
    list.remove(name)
    return

def sort_list(list):
    #return list.sort(reverse=True)
    return list.sort()

def reverse_list(list):
    return list.reverse()

def lenght_list(list):
    return list.__len__()

def view_list(list):
    for items in list:
        print(items)

def generate_numbers(step,start_number,end_number):
    for value in range(start_number,end_number,step):
        print(value)

def generate_list_numbers(start_number,end_number):
    return list(range(start_number,end_number,1))

def minimum_value(list):
    return min(list)
def maximum_value(list):
    return max(list)
def sum_list(list):
    return sum(list)

print(changing_case("michAL halUCha"))
print("Concatenation:"+ combine_string("\nmichal      ","\thalucha "))
print(calculate("2","+","3"))
#-1 last position, 0 first position
print(bicycles[0].title(),bicycles[-1])
print(add_to_list(bicycles,"giant"))
print(insert_to_list(bicycles,2,"kellys"))
print(remove_position(bicycles,2))
print(pop_position(bicycles,3))
remove_name(bicycles,"dartmoor")
sort_list(bicycles)
print(bicycles)
reverse_list(bicycles)
print(bicycles)
print(lenght_list(bicycles))
view_list(bicycles)
generate_numbers(1,3,5)
print(generate_list_numbers(1,5))
print(maximum_value(number_list))
print(minimum_value(number_list))
print(sum_list(number_list))
#very short command to generate list
square = [value**3 for value in range(1,3)]
print(square)
