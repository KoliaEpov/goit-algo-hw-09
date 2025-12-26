import timeit

def find_coins_greedy(value):
    coins = [50, 25, 10, 5, 2, 1]
    result = {50: 0, 25: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    i = 0
    if value <= 0:
        return "Please use a valid cost"

    while value > 0:
        if value >= coins[i]:
            result[coins[i]] = result.get(coins[i], 0) + 1
            value -= coins[i]
        else:
            i += 1

    return result


def find_min_coins(value):
    coins = [50, 25, 10, 5, 2, 1]
    result = [0] + [float("inf")] * value
    prev = [None] * (value + 1)

    for i in range(1, value + 1):
        for coin in coins:
            if coin <= i and result[i - coin] + 1 < result[i]:
                result[i] = result[i - coin] + 1
                prev[i] = coin

    result = {}
    cur = value

    while cur > 0:
        coin = prev[cur]
        result[coin] = result.get(coin, 0) + 1
        cur -= coin

    return result


def test_find_coins_greedy(value):
    find_coins_greedy(value)


def test_find_min_coins(value):
    find_min_coins(value)


def main():
    print("Start find_coins_greedy")
    print(timeit.timeit(lambda: test_find_coins_greedy(16), number=5))
    print(timeit.timeit(lambda: test_find_coins_greedy(127), number=5))
    print(timeit.timeit(lambda: test_find_coins_greedy(264), number=5))
    print(timeit.timeit(lambda: test_find_coins_greedy(339), number=5))
    print(timeit.timeit(lambda: test_find_coins_greedy(473), number=5))
    print(timeit.timeit(lambda: test_find_coins_greedy(591), number=5))
    print("End find_coins_greedy")

    print("Start find_min_coins")
    print(timeit.timeit(lambda: test_find_min_coins(16), number=5))
    print(timeit.timeit(lambda: test_find_min_coins(127), number=5))
    print(timeit.timeit(lambda: test_find_min_coins(264), number=5))
    print(timeit.timeit(lambda: test_find_min_coins(339), number=5))
    print(timeit.timeit(lambda: test_find_min_coins(473), number=5))
    print(timeit.timeit(lambda: test_find_min_coins(591), number=5))
    print("End find_min_coins")


if __name__ == "__main__":
    main()
