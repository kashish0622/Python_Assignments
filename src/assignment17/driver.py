from util import block

def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        cubes = list(map(int, input().split()))

        if block(cubes):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()