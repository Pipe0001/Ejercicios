class punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

punto_1 = punto(3, 4)
print(f'coordenadas del punto 1: {punto_1}')