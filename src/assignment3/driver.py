if __name__ == '__main__':
    from util import second_maximum
    n = int(input())
    score = list(map(int, input().split()))
    result = second_maximum(score)
    print (result)