class Fibonacci:

    def __init__(self, upper_limit):
        self.fibonacci = [1, 2]
        while self.fibonacci[-1] < upper_limit:
            self.fibonacci.append(self.fibonacci[-1] + self.fibonacci[-2])

    def sum(self):
        return sum(self.fibonacci)

    def sum_evens(self):
        return sum([x for x in self.fibonacci if x % 2 == 0])

    def sum_odds(self):
        return sum([x for x in self.fibonacci if x % 2 != 0])

if __name__ == "__main__":
    print(Fibonacci(4000000).sum_evens())
