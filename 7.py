students = ["Arun", "Bala", "Chitra", "Deepak"]
marks = [75, 35, 55, 40]
attendance = [85, 60, 75, 65]
lab_scores = [80, 30, 45, 35]
high_risk = 0
medium_risk = 0
low_risk = 0
for i in range(len(students)):
    risk = 0
    print("\nStudent:", students[i])
    if marks[i] < 40:
        print("Low Marks")
        risk += 1
    if attendance[i] < 75:
        print("Low Attendance")
        risk += 1
    if lab_scores[i] < 40:
        print("Low Lab Score")
        risk += 1
    if risk >= 2:
        category = "High Risk"
        high_risk += 1
    elif risk == 1:
        category = "Medium Risk"
        medium_risk += 1
    else:
        category = "Low Risk"
        low_risk += 1
    print("Risk Factors:", risk)
    print("Category:", category)
print("\nACADEMIC RISK SUMMARY")
print("High Risk Students:", high_risk)
print("Medium Risk Students:", medium_risk)
print("Low Risk Students:", low_risk)