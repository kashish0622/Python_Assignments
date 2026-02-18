from util import min_max
if __name__ == '__main__':

 a, b = map(int, input().split())
 values = []
 for i in range (a):
     a = list(map(int, input().split()))
     values.append(a)

result = min_max(values)
print(result)
