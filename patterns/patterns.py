def p_1(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print("\n")


def p_2(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print("\n")


def p_3(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(str(j), end=" ")
        print("\n")


def p_4(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(str(i), end=" ")
        print("\n")


def p_5(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("* ", end="")
        print("\n")


def p_6(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(str(i), end=" ")
        print("\n")


def p_7(n):
    for i in range(n):
        for j in range(n - i - 1):
            print("  ", end="")
        for j in range(2 * i + 1):
            print("* ", end="")
        for j in range(n - i - 1):
            print(" ", end="")
        print("\n")


def p_8(n):
    for i in range(n - 1, -1, -1):
        for j in range(n - i - 1):
            print(" ", end=" ")
        for j in range(2 * i + 1):
            print("* ", end="")
        for j in range(n - 1 - i):
            print(" ", end=" ")
        print("\n")


def p_9(n):
    for i in range(n):
        for j in range(n - i - 1):
            print("  ", end="")
        for j in range(2 * i + 1):
            print("* ", end="")
        for j in range(n - i - 1):
            print(" ", end="")
        print("\n")
    for i in range(n - 1, -1, -1):
        for j in range(n - i - 1):
            print(" ", end=" ")
        for j in range(2 * i + 1):
            print("* ", end="")
        for j in range(n - 1 - i):
            print(" ", end=" ")
        print("\n")


def p_10(n):
    for i in range(n):
        for j in range(i + 1):
            print("* ", end="")
        print("\n")
    for i in range(n - 1, 0, -1):
        for j in range(i):
            print("* ", end="")
        print("\n")


def p_11(n):
    start = 1
    for i in range(n):
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(i + 1):
            print(str(start), end="")
            start = 1 - start
        print("\n")


if __name__ == "__main__":
    p_1(5)
    p_2(5)
    p_3(5)
    p_4(5)
    p_5(5)
    p_6(5)
    p_7(5)
    p_8(5)
    p_9(5)
    p_10(5)
    p_11(5)
