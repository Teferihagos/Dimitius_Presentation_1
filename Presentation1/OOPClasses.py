class Animal:
    """
    Class for Dogs & Cats
    """

    def __init__(self, name: str, animal_type: str):
        self.name = name
        self.animal_type = animal_type

    def run(self):
        print(f"{self.name} can run")

    def speak(self):
        print(f"{self.name} can speak")

    def eat(self):
        return print(self.name + "Can eat")


# *args, and **kwargs
animal = Animal(animal_type="Cat", name="Michou")

# animal.run()
print(animal.name)
