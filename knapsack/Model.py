import array


class Model:
    def __init__(self, weight: array, value: array, capacity: int):
        # initialize weight
        self.weights = weight

        # initialize values (profit)
        self.values = value

        # initalize capacity (max value)
        self.capacity = capacity

        self.memo = [[-1] * (capacity + 1) for d in range(len(weight) + 1)]

    # calculate brute force approach O(n^2)
    def calculate_brute_force(self, i: int = 0, current_weight: int = 0, current_value: int = 0):
        if i >= len(self.weights):
            return current_value
        value_one = 0
        value_two = 0
        value = self.values[i]
        weight = self.weights[i]
        if current_weight + weight <= self.capacity:
            value_one = self.calculate_brute_force(i + 1, current_weight + weight, current_value + value)
        value_two = self.calculate_brute_force(i + 1, current_weight, current_value)

        return max(value_one, value_two)


    def calculate_memo(self, i: int = 0, current_weight: int = 0) -> int:
        if i >= len(self.weights):
            return 0

        if self.memo[i][current_weight] != -1:
            return self.memo[i][current_weight]

        value_one = self.calculate_memo(i + 1, current_weight)

        value_two = 0
        if current_weight + self.weights[i] <= self.capacity:
            value_two = self.values[i] + self.calculate_memo(i + 1, current_weight + self.weights[i])

        self.memo[i][current_weight] = max(value_two, value_one)
        return self.memo[i][current_weight]


