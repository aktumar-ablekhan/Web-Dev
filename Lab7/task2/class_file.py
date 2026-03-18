class Animal:
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food

    def speak(self):
        return "Animal makes a sound"

    def eat(self):
        return f"{self.name} eats {self.food}"

    def __str__(self):
        return f"Animal: {self.name}, Age: {self.age}, Food: {self.food}"


class Dog(Animal):
    def __init__(self, name, age, food, breed):
        super().__init__(name, age, food)
        self.breed = breed

    def speak(self):
        return "Woof"

    def guard(self):
        return f"{self.name} is guarding the house"

    def __str__(self):
        return f"Dog: {self.name}, Breed: {self.breed}, Age: {self.age}"


class Cat(Animal):
    def __init__(self, name, age, food, color):
        super().__init__(name, age, food)
        self.color = color

    def speak(self):
        return "Meow"

    def sleep(self):
        return f"{self.name} is sleeping"

    def __str__(self):
        return f"Cat: {self.name}, Color: {self.color}, Age: {self.age}"