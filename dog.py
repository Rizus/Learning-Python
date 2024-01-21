class Dog:
    # Атрибут класса
    species = "Canis familiaris"

    # Инициализация атрибутов экземпляров класса
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Метод экземпляра класса
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Еще один метод экземпляра класса
    def speak(self, sound):
        return f"{self.name} barks: {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


miles = JackRussellTerrier("Miles", 4)
print(miles.speak())
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
print(jim.speak("Woof"))
print(miles.speak())
cheese = GoldenRetriever("Сheese", 3)
print(cheese.speak())
print(type(miles))
print(type(cheese))
print(isinstance(miles, Dog))
