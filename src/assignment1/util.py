def runcommands(my_list, command):

    if command[0] == 'insert':
      my_list((command[1]), int(command[2]))

    elif command[0] == 'print': 
      print(my_list)

    elif command[0] == 'remove':
      my_list.remove(command[0])

    elif command[0] == 'append':
      my_list.append(int(command[1]))
      
    elif command[0] == 'sort':
      my_list.sort()

    elif command[0] == 'pop':
      my_list.pop()

    elif command[0] == 'reverse':
      my_list.reverse()

        
