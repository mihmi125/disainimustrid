from Rectangle import Rectangle
from Square import Square

if __name__ == "__main__":
    r = Rectangle(2, 3)
    s = Square(5)

    print(r)
    print(s)

    print(f"Rectangle area: {r.area}")
    print(f"Square area: {s.area}")