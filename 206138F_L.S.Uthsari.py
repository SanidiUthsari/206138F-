
print("welcome to the voting system :)")
name = input("Enter your name:")
print("Hello",name)


minimum_Voting_age = 18 

def check_age(age):
    if age >= minimum_Voting_age :
        print("You are eligible to vote!")
        vote = input("Do you want to vote?" ).upper()
        if vote == "YES":
            print("Great! You can cast your vote.")
        elif vote == "NO":
            print("Okay, maybe next time!")
        else:
            print("Invalid input.")
    else:
        print("You cannot vote, Come back when you're 18 :).")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError:
    print("Invalid input. Please enter a valid age.")

print("Thank you!")
print("Try Again")






