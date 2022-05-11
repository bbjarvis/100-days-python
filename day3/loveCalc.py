# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆
# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."
#Write your code below this line 👇

names = name1 + name2
totTrue = names.count("t") + names.count("r") + names.count("u") + names.count("e")
totLove = names.count("l") + names.count("o") + names.count("v") + names.count("e")
loveScore = str(totTrue) + str(totLove)
if int(loveScore) > 90 or int(loveScore) < 10:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif int(loveScore) > 40 and int(loveScore) < 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")


