

def rectangular_pyramid(n: int):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print("\n")


if __name__ == "__main__":
    rectangular_pyramid(5)
