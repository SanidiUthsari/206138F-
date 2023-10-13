print("welcome to the voting system :)")
name = input("Enter your name:")
print("Hello",name)

Minimum_Voting_age = 18
age = int(input("Enter your age:"))

if age >=   Minimum_Voting_age :
    print("You can vote")
    vote = input("do you prefer to vote?").upper()
    if vote == "YES":
        print("Great! you can elect.")
    elif vote == "NO":
        print(" may be next time :)")
    else:
        print("invalid input :(")
else:
    print("You cannot vote, come back when you are 18 :)")



