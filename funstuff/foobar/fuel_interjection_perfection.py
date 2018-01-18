def answer(n):
    count = 0
    n = int(n)
    while not n == 1:
        if n & 1 == 0:
            number = number / 2
        elif n == 3 or n % 4 == 1:
            number -= 1
        else:
            number += 1
        count++
    return count
