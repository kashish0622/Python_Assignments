def diff_values(n):
    width = len(bin(n)[2:])
    for i in range(1, n+1):
        decimal = float(i)
        octal = oct(i) [2: ]
        hexa = hex(i) [2: ].upper()
        binary = bin(i) [2: ]

    print(decimal.rjust(width), octal.rjust(width), hexa.rjust(width), binary.rjust(width))
