class Сircle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius

circ = circle(10)
circ.set_radius(2)

print('новый радиус:',circ.get_radius())