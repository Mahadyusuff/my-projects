class Kid:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def print_info(self):
        print(f"{self.name} is {self.age} years old")


def main():
    the_kid = Kid("Sam", 10)
    the_kid.birthday()
    the_kid.birthday()
    the_kid.print_info()


main()