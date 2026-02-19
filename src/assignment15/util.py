def happiness(array, setA, setB):
    happiness = 0
    for i in array:
        if i in setA:
            happiness = happiness+1
        elif i in setB:
            happiness = happiness-1
        else:
            happiness = happiness+0
    return happiness