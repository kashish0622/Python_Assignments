from util import marks
if __name__ == "__main__":
    n = int(input)
    columns = input().split()

    rows = []
    for _ in range(n):
        rows.append(input())

    avg = marks(n, columns, rows)
    print (round(avg, 2))