students = ["Arun", "Bala", "Chitra", "Deepak",
            "Esha", "Farhan"]
scores = [80, 60, 90, 70, 85, 65]
group_size = 2
groups = [[], [], []]
totals = [0, 0, 0]
for i in range(len(scores)):
    for j in range(i + 1, len(scores)):
        if scores[j] > scores[i]:
            scores[i], scores[j] = scores[j], scores[i]
            students[i], students[j] = students[j], students[i]
for i in range(len(students)):
    min_group = 0
    for j in range(1, len(groups)):
        if totals[j] < totals[min_group]:
            min_group = j
    groups[min_group].append(students[i])
    totals[min_group] += scores[i]
print("Student Groups:")
for i in range(len(groups)):
    print("Group", i + 1, ":", groups[i])
    print("Group Total Score:", totals[i])
difference = max(totals) - min(totals)
print("Difference between group totals:", difference)