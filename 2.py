students = ["Arun", "Bala", "Chitra"]
exam1 = [60, 35, 80]
exam2 = [70, 30, 85]
exam3 = [80, 25, 90]
for i in range(3):
    print("\nStudent:", students[i])
    avg = (exam1[i] + exam2[i] + exam3[i]) / 3
    print("Average Marks:", avg)
    change = exam3[i] - exam1[i]
    print("Change in Marks:", change)
    if change > 0:
        print("Trend: Improved")
    elif change < 0:
        print("Trend: Declined")
    else:
        print("Trend: No Change")
    if avg >= 80:
        print("Category: Excellent")
    elif avg >= 60:
        print("Category: Good")
    elif avg >= 40:
        print("Category: Average")
    else:
        print("Category: Needs Improvement")
    if exam1[i] < 40 and exam2[i] < 40 and exam3[i] < 40:
        print("Weak Performance: Yes")
    else:
        print("Weak Performance: No")