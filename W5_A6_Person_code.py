class Person:
    def __init__(self, name, address, age):
        self._name = name
        self._address = address
        self._age = age

    def greet(self):
        print (f"Greeting and felicitation from Maestro, {self._name}")

if __name__ == "__main__":
    person1 = Person ("Alice","123 Main St", 20)
    person1.greet()