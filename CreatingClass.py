class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)


r1 = Robot("Sofia", "yellow", 55)
r2 = Robot("Alia", "blue", 70)

r1.introduce_self()
r2.introduce_self()
