class CombinationLock:
    def __init__(self, combination: list):
        self.status = 'LOCKED'
        self.combination = combination
        self.enter_digits = []

    def enter_digit(self, digit):
        self.enter_digits.append(digit)
        correct_so_far = self.combination[:len(self.enter_digits)]

        if self.enter_digits == self.combination:
            self.status = 'OPEN'
        elif self.enter_digits == correct_so_far:
            self.status = "".join(map(str, self.enter_digits))
        else:
            self.status = "ERROR"



cl = CombinationLock([1, 2, 3, 4, 5])
print(cl.status)

cl.enter_digit(1)
print(cl.status)

cl.enter_digit(5)
print(cl.status)

cl.enter_digit(3)
print(cl.status)

cl.enter_digit(4)
print(cl.status)

cl.enter_digit(5)
print(cl.status)