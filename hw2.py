class Cat:
    def __init__(self, name:str, age:int, breed:str,  weight:float, energy:int, happiness:int, hunger:int) -> None:
        self.name  = name
        self.age  = age 
        self.breed = breed
        self.weight = weight
        self.energy = energy
        self.happiness = happiness
        self.hunger = hunger

    def tell_age(self):
        if self.age < 10:
            return f"This kitty is young. It is {self.age}"
        return f"Kitty is qite old. It is {self.age}"

    def eat(self):
        if self.hunger == 0:
           self.weight += 0.3
           return f"Kitty overate. Its weight now is {self.weight}"
        self.hunger -= 1
        return f"kitty ate. Now hunger is {self.hunger}"
    
    def play(self):
        if self.energy < 5:
            return "Kitty is tired. It should rest"
        self.energy -= 2
        self.happiness += 1
        self.weight -= 0.2
        return f'kitty playde. Now its happy level is {self.happiness} and energy level is {self.energy}'

    def rest(self):
        if self.energy > 25:
            return "Kitty is not tired. It wants to play"
        self.energy += 4
        return f"Kitty got some rest. Energy level is {self.energy}"


cat = Cat('Mary', 4, 'cat', 5.7, 18, 20, 1)
print(cat.tell_age())
print(cat.eat())
print(cat.eat())
print(cat.play())
print(cat.rest())