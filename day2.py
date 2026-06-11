age = 24              # int  — whole numbers
height = 5.4          # float — numbers with decimals
name = "Sushmitha"    # str  — text, always in quotes
is_student = True     # bool — True or False only
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

print(5 + 3)        # numbers add → 8
print("5" + "3")    # text joins → 53

text_number = "10"
real_number = int(text_number)   # now it's an int
print(real_number + 5)           # 15 — math works now!

price = 9.99
print("The price is " + str(price))   # convert number to text to join it

print(17 // 5)   # floor division → 3 (how many whole times 5 fits)
print(17 % 5)    # modulo → 2 (the remainder)
print(2 ** 3)    # power → 8 (2 to the power of 3)




print("--- Tip Calculator ---")

bill = float(input("Enter the bill amount: $"))
tip_percent = float(input("Enter tip percentage (e.g. 15): "))
people = int(input("How many people are splitting? "))

tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount
per_person = total / people

print("Tip amount: $" + str(round(tip_amount, 2)))
print("Total bill: $" + str(round(total, 2)))
print("Each person pays: $" + str(round(per_person, 2)))