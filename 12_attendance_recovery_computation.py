"""Case Study 12: Attendance Recovery Computation
Calculate attendance percentage and determine whether the minimum attendance requirement is met.
"""

held = int(input("Total classes held: "))
attended = int(input("Classes attended: "))
required = float(input("Required attendance percentage: "))

if held < 0 or attended < 0 or attended > held or not 0 <= required <= 100:
    print("Invalid attendance details.")
elif held == 0:
    print("Attendance percentage cannot be calculated because no classes were held.")
else:
    percentage = attended / held * 100
    print(f"Attendance: {percentage:.2f}%")
    if percentage >= required:
        print("Attendance requirement met.")
    else:
        print("Attendance requirement not yet met.")
        if required == 100:
            extra = held - attended
        else:
            extra = max(0, int((required * held - 100 * attended) // (100 - required)) + 1)
            while (attended + extra) / (held + extra) * 100 < required:
                extra += 1
        print(f"Attend the next {extra} consecutive classes without absence to reach the requirement.")
