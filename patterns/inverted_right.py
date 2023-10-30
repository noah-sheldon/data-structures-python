def inverted_right(n):
    for i in range(n):
        for j in range(n - i, 0, -1):
            print("*", end=" ")
        print("\n")


if __name__ == "__main__":
    inverted_right(5)
