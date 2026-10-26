rows = 4
cols = 5

reserved = [(1, 2), (3, 4)]
seat_no = 1

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        if (i, j) in reserved:
            print("RES", end="\t")
        elif (i + j) % 2 == 0:
            print("X", end="\t")
        else:
            print(seat_no, end="\t")
            seat_no += 1
    print()