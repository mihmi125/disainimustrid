class Square:
    def __init__(self, side=0):

        self.side = side

class SquareToRectangleAdapter(Square):
    def __init__(self, square):
        super().__init__(square.side)
        self.height = square.side
        self.width = square.side

def calculate_area(rc):
    return rc.width * rc.height

sq = Square(5)
adapter = SquareToRectangleAdapter(sq)

print(calculate_area(adapter))