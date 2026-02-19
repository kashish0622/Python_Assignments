from util import happiness
if __name__ == '__main__':
    n, m = map(int(input()))
    array = list(map(int, input()))
    setA = set(map(int, input()))
    setB = set(map(int, input()))
    result = happiness(array, setA, setB)
    print(result)
