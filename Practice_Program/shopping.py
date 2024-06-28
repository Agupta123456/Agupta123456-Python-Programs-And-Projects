amt = float(input("Enter the amount of shopping: $"))
gender = str(input("What is your gender: male or female ? : "))

if amt >= 4000 and gender == 'female':
    dis = 50
elif amt < 4000 and gender == 'female':
    dis = 25
elif amt >= 4000 and gender == 'male':
    dis = 30
else:
    dis = 10

discount = amt * dis / 100

amount = amt - discount

print(f"Your bill amount after discount is : ${amount}")
