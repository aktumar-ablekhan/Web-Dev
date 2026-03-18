from class_file import Animal, Dog, Cat


def main():
    a1 = Animal("Generic", 5, "food")
    d1 = Dog("Aktos", 3, "meat", "Buldak")
    c1 = Cat("Bulbul", 2, "fish", "red")

    animals = [a1, d1, c1]

    for animal in animals:
        print(animal)
        print(animal.speak())
        print(animal.eat())
        print("-" * 30)

    for animal in animals:
        print(animal.speak())

    print("-" * 30)
    print(d1.guard())
    print(c1.sleep())


if __name__ == "__main__":
    main()