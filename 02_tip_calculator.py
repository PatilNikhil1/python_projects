# greeting
print("Welcome to the tip calculator!")

# user inputs
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

# calculation
total_bill = bill * tip / 100 + bill
per_people = total_bill / people
each_person = round(per_people, 2)

# print result
print(f"Each person should pay: ${each_person}")