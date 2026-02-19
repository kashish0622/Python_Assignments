def diff_values(n):
    result = []

    for i in range(1, n+1):
        decimal = str(i)
        octal = oct(i) [2: ]
        hexa = hex(i) [2: ].upper()
        binary = bin(i) [2: ]
        line = line = decimal + " " + octal + " " + hexa + " " + binary

        result.append(line)

    return result
