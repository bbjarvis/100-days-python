# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if not(year % 4) and (year % 100) and (year % 400):
    print("Leap year.")
else:
    print("Not leap year.")

