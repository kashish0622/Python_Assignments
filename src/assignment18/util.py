import math
def probability_of_a(n, letters, k):
    countofa = letters.count('a')
    non_a = n - countofa

    if k > non_a:
        return 1.0

    prob_of_a = math.comb(non_a, k) / math.comb(n, k)

    return 1 - prob_of_a