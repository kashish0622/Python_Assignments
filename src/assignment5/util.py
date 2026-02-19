def mergetools(s, k):
    result = []
    for i in range(0, len(s), k):
        part = s[i:i+k]
        print("".join(dict.fromkeys(part)))
    return result
