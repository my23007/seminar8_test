def first_div_16(n1, n2):
    for num in range(n1, n2):
        if num % 16 == 0:
            return num
    return 0
