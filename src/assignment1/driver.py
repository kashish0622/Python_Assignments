if __name__ == '__main__':
    from util import runcommands
    my_list = []
    n = int(input())
    for _ in range(n):
        command = input().split()
        if command[0] == 'print':
            print(my_list)
        else: 
            runcommands(my_list, command)