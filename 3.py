start = int(input("Enter starting weekday (0=Sun, 1=Mon, ..., 6=Sat): "))
days = int(input("Enter number of days in the month: "))
if start < 0 or start > 6 or days < 28 or days > 31:
    print("Invalid input")
else:
    print("Sun Mon Tue Wed Thu Fri Sat")

    for i in range(start):
        print("    ", end="")
    day = 1
    count = start
    while day <= days:
        for j in range(7):
            if day <= days and count >= start:
                print("%3d " % day, end="")
                day += 1
            else:
                print("    ", end="")
            count += 1
        print()