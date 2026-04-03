from random import randint


class Generator:
    def generate(self, count):
        return [randint(1, 9) for _ in range(count)]


class Splitter:
    def split(self, matrix):
        size = len(matrix)
        result = []

        result.extend(matrix)

        for c in range(size):
            column = [matrix[r][c] for r in range(size)]
            result.append(column)

        diagonal1 = [matrix[i][i] for i in range(size)]
        result.append(diagonal1)

        diagonal2 = [matrix[i][size - 1 - i] for i in range(size)]
        result.append(diagonal2)

        return result


class Verifier:
    def verify(self, sequences):
        if not sequences:
            return False

        target_sum = sum(sequences[0])

        return all(sum(seq) == target_sum for seq in sequences)


class MagicSquareGenerator:
    def __init__(self):
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier()

    def generate(self, size):
        while True:
            data = self.generator.generate(size * size)

            matrix = []
            for i in range(0, len(data), size):
                matrix.append(data[i: i + size])

            sequences = self.splitter.split(matrix)

            if self.verifier.verify(sequences):
                return matrix


gen = MagicSquareGenerator()
square = gen.generate(3)

for row in square:
    print(row)