def left_numbers(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print("\n")


if __name__ == "__main__":
    left_numbers(5)