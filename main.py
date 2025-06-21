from knapsack.Model import Model


def main():
    weights = [1,3,3,1]
    values = [3,8,4,7]
    capacity = 6
    knapsack_model = Model(weights, values, capacity)
    print(knapsack_model.calculate_brute_force())
    weights_two = [3, 1, 6, 10, 1, 4, 9, 1, 7, 2, 6, 1, 6, 2, 2, 4, 8, 1, 7, 3, 6,
               2, 9, 5, 3, 3, 4, 7, 3, 5, 30, 50]
    values_two = [7, 4, 9, 18, 9, 15, 4, 2, 6, 13, 18, 12, 12, 16, 19, 19, 10, 16,
              14, 3, 14, 4, 15, 7, 5, 10, 10, 13, 19, 9, 8, 5]
    knapsack_model_memo = Model(weights_two, values_two, 75)
    print(knapsack_model_memo.calculate_memo())

if __name__ == '__main__':
    main()


# values = [3,8,4,7]
# weights = [1,3,3,1]
#           0 0 0 0
#           1 0 0 0

#           0 0 0 0
#           1 1 0 0



