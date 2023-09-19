#İf the bill was $150.00, split beetween 5 people, with 12% tip
#Each person should pay (150.00 /5) *1.12 =33.6
#round the result to 2 decimal places = 33.60

print("Welcome to a tip calculator!")

bill = float(input("what was your total bill ? "))

tip = int(input("How muvh tip would you like to give ? 10,12, or 15 ?"))
people = int(input("How many people to split the bill ?"))


tip_as_percent = tip /100
total_tip_amount = bill *  tip_as_percent 
total_bill = bill *total_tip_amount
bill_per_person = total_bill / people,
final_amount=round(bill_per_person)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay : ${final_amount}")


