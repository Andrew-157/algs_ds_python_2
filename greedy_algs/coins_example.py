# Greedy Algorithm example on Coins Problem


"""
Problem: You have to make a change of an amount using the smallest possible number of coins.
Amount: $18

Available coins are
  $5 coin
  $2 coin
  $1 coin
There is no limit to the number of each coin you can use.

"""


def solution(amount: int, coins: list[int]) -> list[int]:

    coins.sort(reverse=True)

    solution_set = []

    a = 0

    i = 0

    while a != amount:
        coin = coins[i]
        if a + coin > amount:
            i += 1
        else:
            a += coin
            solution_set.append(coin)

    return solution_set


print(solution(amount=18, coins=[5, 2, 1]))
