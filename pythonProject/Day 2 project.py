# Day 2 Project: Tip Calculator

print("Welcome to the Tip Calculator!")

bill = float(input("Enter total bill: $"))
tip_percentage = float(input("Enter tip percentage you would like to give: "))
people = int(input("Enter number of people to split the bill: "))

tip_amount = (tip_percentage / 100) * bill
total_amount = bill + tip_amount

amount_per_person = total_amount / people
final_amount = round(amount_per_person, 2)

print(f"Each person has to pay: ${final_amount}")
