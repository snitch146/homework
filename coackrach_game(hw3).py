import random

class Cockroach:
    def __init__(self, name) -> None:
        self.name = name
        self.position = 0
    
    def run(self):
        self.position = self.position + random.randint(0,5)



class Game:
    def __init__(self, field_length, round_count) -> None:
        self.field_length = field_length
        self.round_count = round_count
        self.cockroaches = []
        self.game_over = False



    def add_cockroach(self, cockroach):
        self.cockroaches.append(cockroach)
        
    def show_cockroaches(self):
        for cockroach in self.cockroaches:
            self.display(cockroach)          
    def display(self,cockroach):
        stf = ''
        position = cockroach.position
        if position > self.field_length:
            position = self.field_length
        for i in range(self.field_length):
            if i == position - 1:
                stf = stf + 'x'
            else:
                stf = stf + '.'
        print('  '+ cockroach.name + '  ' +(stf))


    def run(self):
        for i in range(self.round_count):
            print('Round '+ str(i+1) )
            self.push_cockcroaches()
            self.show_cockroaches()
            self.check_winner()
            if self.game_over == True:
                print('Game over')
                break
         
    def push_cockcroaches(self):
        for cockroach in self.cockroaches:
            cockroach.run()  

    def check_winner(self):
        for cockroach in self.cockroaches:
            if cockroach.position >= self.field_length:
                print(cockroach.name +' win')
                self.game_over = True


cockroach1 = Cockroach("Vasya")
cockroach2 = Cockroach("Petya")
cockroach3 = Cockroach("Kolya")
game = Game(10, 3)
game.add_cockroach(cockroach1)
game.add_cockroach(cockroach2)
game.add_cockroach(cockroach3)
game.run()
