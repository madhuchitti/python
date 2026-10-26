teams = [("Team A", [101, 102]),
    ("Team B", [103, 104, 105]),
    ("Team C", [106, 107])]
scores = [[80, 90, 85],
    [90, 85, 80],
    [80, 90, 85]]
min_size = 2
max_size = 3
totals = []
for i in range(len(teams)):
    name = teams[i][0]
    members = teams[i][1]
    print(name)
    if len(members) < min_size or len(members) > max_size:
        print("Invalid Team Size")
        total = -1
    else:
        print("Team Size:", len(members))

        total = 0
        for j in range(len(scores[i])):
            total += scores[i][j]
        print("Total Score:", total)
    totals.append(total)
for i in range(len(totals)):
    for j in range(i + 1, len(totals)):
        if totals[j] > totals[i]:
            totals[i], totals[j] = totals[j], totals[i]
            teams[i], teams[j] = teams[j], teams[i]
            scores[i], scores[j] = scores[j], scores[i]
print("\nFinal Rankings")
rank = 1
for i in range(len(teams)):
    if totals[i] == -1:
        print(teams[i][0], "- Disqualified")
    else:
        if i > 0 and totals[i] == totals[i - 1]:
            print("Rank", rank, ":", teams[i][0], "-", totals[i])
        else:
            rank = i + 1
            print("Rank", rank, ":", teams[i][0], "-", totals[i])