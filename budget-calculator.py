budget = float(input("Enter your budget: "))

food = float(input("Enter food expenses: "))
transportation = float(input("Enter transportation expenses: "))
school = float(input("Enter school expenses: "))

totalExpenses = food + transportation + school
remainingMoney = budget - totalExpenses

print("\n===== Budget Summary =====")
print("Budget:", budget)
print("Total Expenses:", totalExpenses)
print("Remaining Money:", remainingMoney)

if remainingMoney > 0:
    print("Status: NAA pakay kwarta bilin.")
elif remainingMoney == 0:
    print("Status: WALA najud kay kwarta haha.")
else:
    print("Status: Oops oops na OVER budget ka.")