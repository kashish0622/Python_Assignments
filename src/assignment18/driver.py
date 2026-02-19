from util import probability_of_a

def main():
    n = int(input())
    letters = input()
    k = int(input())

    result = probability_of_a(n, letters, k)
    print(result)

if __name__ == "__main__":
    main()