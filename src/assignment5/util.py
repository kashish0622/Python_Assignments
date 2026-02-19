def mergetools(s, k):
    for i in range(0, len(s), k):
        part = s[i:i+k]
        print("".join(dict.fromkeys(part)))
