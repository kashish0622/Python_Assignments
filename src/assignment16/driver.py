from util import words

if __name__ == "__main__":
    n = int(input())

    word = []
    for i in range(n):
        words.append(input())

    distinct_count, occurrences = words(word)

    print(distinct_count)
    print(*occurrences)
