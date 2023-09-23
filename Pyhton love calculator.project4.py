# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆


combined_names =name1+name2
lower_combined_name=combined_names.lower()

t=lower_combined_name.count("t")
r=lower_combined_name.count("r")
u=lower_combined_name.count("u")
e=lower_combined_name.count("e")

true= t + r + u + e

l=lower_combined_name.count("l")
o=lower_combined_name.count("o")
v=lower_combined_name.count("v")
e=lower_combined_name.count("e")

love = l + o + v + e

love_score= int(str(true) + str(love))

if love_score <10 or love_score>90 :
    print(f"Your score is {love_score},you go together like coke and mentos." )
elif (love_score >=40) and (love_score<=50) :
    print(f"Your score is {love_score},you are alright together.")
else :
    print(f"Your scoreis {love_score}.")  