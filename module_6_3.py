class Horse:
    x_distance = 0
    sound = 'Frrr'

    def __init__(self, dx):
        self.dx = dx

    def run(self, dx):
        self.dx = dx
        Horse.x_distance += self.dx


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep and repeat'

    def __init__(self, dy):
        self.dy = int(dy)

    def fly(self, dy):
        self.dy = dy
        Eagle.y_distance += self.dy


class Pegasus(Horse, Eagle):
    def __init__(self, dx, dy):
        super().__init__(dx)
        super().__init__(dy)

    def move(self, dx, dy):
        Horse.run(self, dx)
        Eagle.fly(self, dy)

    def get_pos(self):
        return Horse.x_distance, Eagle.y_distance

    def voice(self):
        print(f'{self.sound}')


p1 = Pegasus(0, 0)

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
