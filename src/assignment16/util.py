def words(word):
    freq = {}
    order = []
    for i in word:
        if i not in freq:
            freq[i] = 1
            order.append(i)
        else:
            freq[i] = freq[i] + 1
    count = []
    for i in order:
        count.append(freq[i])

    return len(order), count
