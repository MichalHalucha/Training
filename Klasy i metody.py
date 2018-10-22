class Time:
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

#__str__ to prawie to samo co init. zwraca reakcje lancuchowa
    def __init__(self, hour = 0,minute = 0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    #przeciążenie operatorów
    #def __add__(self,other):
    #    seconds = self.time_to_int()+self.other.time_to_int()
    #    return int_to_time(seconds)
    #pamiętaj o __radd__ (right side add)

    """POLIMORFIZM: Funkcja histogram pracuje z różnymi typami dlatego jest polimorficzna"""


time = Time(2,2,2)
Time.print_time(time)




#class Time:
#    def print_time(time):
#        print('%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second))

#start = Time()
#start.hour = 9
#start.minute = 45
#start.second = 90
#Time.print_time(start)

#innys sposób Time.print_time(start)
#start.print_time(start), nie działa

# jeżeli nie jestem pewien atrybutów użyj funkcji vars
#przykład
def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj,attr))
