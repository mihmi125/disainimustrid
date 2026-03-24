from Shape import Shape

class Square(Shape):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = _size

    @property
    def area(self):
        return self._size ** 2

    def __str__(self):
        return f"Square(Size: {self._size})"