class Human:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def can_walk(self):
        print('  i can walk')
    def can_breathe(self):
        print('  i can breathe')
    def what_can_i_do(self):
        self.can_walk()
        self.can_breathe()
    def who_am_i(self):
        print(self.__class__.__name__)

class Workman(Human):

    def farm_money(self):
        print('  can make money')
    def can_communicate(self):
        print('  communicates with people')
    def what_can_i_do(self):
        super().what_can_i_do()
        self.farm_money()
        self.can_communicate()

class Doctor(Workman):
    def advice(self):
        print('  advice people')
    def pills(self):
        print('  prescribes pills')
    def what_can_i_do(self):
        super().what_can_i_do()
        self.advice()
        self.pills()


class Car_mechanic(Workman):
    def repairs(self):
        print('  repairs car')
    def what_can_i_do(self):
        super().what_can_i_do()
        self.repairs()


class Pilot_of_plane(Workman):
    def fly(self):
        print('  fly the plane')
    def what_can_i_do(self):
        super().what_can_i_do()
        self.fly()


doctor = Doctor('Alex', 27)
mechanic = Car_mechanic('Judy', 31)
pilot = Pilot_of_plane('Raze', 25)
for worker in [doctor,mechanic,pilot]:
    worker.who_am_i()
    worker.what_can_i_do()

