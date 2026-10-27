"""Case Study 11: Examination Result and Grace-Mark Validation
Calculate total and percentage, and determine pass/fail using a simple example rule.
"""

maximum = float(input("Maximum marks per subject: "))
marks1 = float(input("Marks in subject 1: "))
marks2 = float(input("Marks in subject 2: "))
marks3 = float(input("Marks in subject 3: "))

marks = [marks1, marks2, marks3]
if maximum <= 0 or any(mark < 0 or mark > maximum for mark in marks):
    print("Invalid marks or maximum marks.")
else:
    total = sum(marks)
    percentage = total / (3 * maximum) * 100
    result = "PASS" if all(mark >= 35 for mark in marks) else "FAIL"
    print(f"Total marks: {total:g} / {3 * maximum:g}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Result: {result}")
