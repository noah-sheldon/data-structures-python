def left_pyramid(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print("\n")


if __name__ == "__main__":
    left_pyramid(5)
