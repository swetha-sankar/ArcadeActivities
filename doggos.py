'''
Animals have a name, energy level, hunger level, and mood
    eat
    sleep

Dogs have breeds
    play

Cats have coat color
    hunt
'''


class Dog:
    # class makes a new type
    name: str
    energy: int
    hungry: bool
    mood: str

    def __init__(self, the_name: str):
        # method: function that lives in a class. special purpose: constructor.
        # constructs instances (in this case: dogs). name is an attribute of all dogs.
        # type of dog always the same as the type of class (this is b/c of the "self")
        self.name = the_name
        self.energy = 0
        self.hungry = False
        self.mood = "happy"

    def feed(self):
        self.hungry = False

    def play_with_dog(self):
        self.mood = "happy"
        self.hungry = True
        self.energy -= 1

    def rest(self, length_of_time: int):
        self.energy += length_of_time


ada = Dog("Ada")
ada.rest(8)
ada.play_with_dog()
ada.rest(5)
print(ada.mood)

babbage = Dog("Babbage")
babbage.mood = ada.mood


