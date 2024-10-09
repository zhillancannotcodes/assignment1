x = {1: "Jan.", 2: "Feb.", 3: "Mar.", 4: "Apr.", 5: "May.", 6: "Jun.", 7: "Jul.", 8: "Aug.", 9: "Sep.", 10: "Oct.", 11: "Nov.", 12: "Dec." }

x_month = int(input("Enter the month in integer: " ))
y_day = int(input("Enter the day in integer: "))

if 1 <= x_month <= 12:
    print(f"The date is: {x.get(x_month)} {y_day}th")
else:
    print("Invalid Input!")