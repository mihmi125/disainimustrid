from random import randint

class Generator:
    def generator(self, count):
        return [randint(0, 9) for _ in range(count)]

class Splitter:
    def split(self, matrix):
        size = len(matrix)
        result = []

        result.extend(matrix)

        for c in range(size):
            column = []
            for r in range(size):
                column.append(matrix[r][c])
            result.append(column)

        diagonal1 = []
        for r in range(size):
            diagonal1.append(matrix[r][r])
        result.append(diagonal1)

        diagonal2 = []
        for c in range(size):
            col_idx = size -1 -c
            diagonal2.append(matrix[c][col_idx])
        result.append(diagonal2)

        return result


class Verifier:
    pass


class MagicSquareGenerator:
    pass


matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

s = Splitter()
print(s.split(matrix))