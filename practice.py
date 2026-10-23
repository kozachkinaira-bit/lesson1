class Human:
    def __init__(self, name):
        pass


class Car:
    def __init__(self, name, space):
        self.name = name
        self.space = space
        self.passengers = []

    def add_passenger(self,passenger:Human):
        pass

    def info(self):
        pass

audi = Car("Audi", 5)
audi.info()
audi.add_passenger()
audi.info()

