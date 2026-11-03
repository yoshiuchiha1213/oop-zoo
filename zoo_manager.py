class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"Animal sound"
    
    
class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def give_birth(self):
        return f"{self.name} the {self.species} has given birth"

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

class Reptile(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def bask_in_sun(self):
        return f"{self.name} the {self.species} is basking in the sun"

class Primate(Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def climb_trees(self):
        return f"{self.name} the {self.species} is climbing trees"

class Marsupial(Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def carry_baby(self):
        return f"{self.name} the {self.species} is carrying its baby"

class Aviary:
    def __init__(self):
        self.birds = []
        
    def add_birds(self, bird):
        self.birds.append(bird)
        
class ReptileEnclosure:
    def __init__(self):
        self.reptiles = []
    
    def add_reptile(self, reptile):
        self.reptiles.append(reptile)