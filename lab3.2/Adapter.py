class Square:
    def __init__(self, side=0):
        self.side = side

class SquareToRectangleAdapter:
    def __init__(self, square):
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side

def calculate_area(rc):
    return rc.width * rc.height

sq = Square(5)
adapter = SquareToRectangleAdapter(sq)

print(calculate_area(adapter))