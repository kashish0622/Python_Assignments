from util import mutate_string
if __name__ == '__main__':
    a = input()
    position, character = input().split()
    position = int(position)

    string2 = mutate_string(a, position, character)
    print(string2)