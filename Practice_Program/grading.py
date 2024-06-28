percentage = float(input("Enter your percentage : "))

if percentage >= 60:
    print("You passed by 1st division")
elif percentage >= 50:
    print("You passed by 2nd division")
elif percentage >= 40:
    print("You passed by 3rd division")
else:
    print("You failed in exam")