from util import words

if __name__ == "__main__":
    n = int(input())

    word = []
    for i in range(n):
        word.append(input())

    count, occurrence = words(word)

    print(count)
    print(*occurrence)
