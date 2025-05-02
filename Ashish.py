def fact(n):
    digit = 1
    for i in range(1, n + 1):  # start from 1, up to n
        digit *= i
        print(digit)

fact(4)
