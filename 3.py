class Skladniki():
    def __init__(self,name,how_many):
        self.name = name
        self.how_many =how_many
    def fire(self):
        for i in range(4):
            print("Fire " + str(i))

class Cars(Skladniki):
    def __init__(self,name,how_many):
        super().__init__(name,how_many)

    def run_auto(self):
        print("BRUM! Brum!")
    def fire(self):
        print("We can't destroy auto")

