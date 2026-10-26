appliances = ["Fan", "Light", "AC"]
readings = [[2, 3, 2, 4, 3, 2, 3],
            [1, 1, 2, 1, 2, 1, 1],
            [5, 6, 7, 8, 6, 7, 9]]
limit = 40
daily_limit = 10
for i in range(len(appliances)):
    total = 0
    for j in range(7):
        total += readings[i][j]
    print(appliances[i], "weekly consumption:", total, "units")
    if total > limit:
        print("Warning: Appliance exceeds weekly limit")
    else:
        print("Consumption is within weekly limit")
print("\nDaily Electricity Consumption:")
for j in range(7):
    daily_total = 0
    for i in range(len(appliances)):
        daily_total += readings[i][j]
    print("Day", j + 1, ":", daily_total, "units")
    if daily_total > daily_limit:
        print("Warning: Daily limit exceeded")
    else:
        print("Daily consumption is within limit")