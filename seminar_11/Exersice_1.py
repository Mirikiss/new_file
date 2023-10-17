class Factorial:
    def __init__(self, limit: int):
        self.limit = limit
        self.storage = {}

    def _fact(self, num: int):
        factorial = []
        number = 1
        for i in range(1, num + 1):
            number *= i
            factorial.append(number)
        return factorial

    def __call__(self, number: int):
        result = self._fact(number)[-self.limit:]
        self.storage[number] = result
        return result