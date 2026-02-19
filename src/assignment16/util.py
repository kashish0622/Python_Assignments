def words(words):
    freq = {}
    order = []
    for i in words:
        if i not in freq:
            freq[w] = 1
            order.append(w)
        else:
            freq[i] = freq[i] + 1
    count = []
    for i in order:
        count.append(freq[i])

    return len(order), count
