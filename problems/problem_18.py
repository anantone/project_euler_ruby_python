GRID = "triangle_pb_18.txt"

def main():
    with open(GRID) as file:
        arrays = [[int(num) for num in line] for line in [line.split() for line in file]]
    arrays.reverse()
    for i in range(1, len(arrays)):
        for j in range(len(arrays[i])):
            arrays[i][j] += max(arrays[i - 1][j: j + 2])
    print(arrays[-1][0])

if __name__ == "__main__":
    main()
