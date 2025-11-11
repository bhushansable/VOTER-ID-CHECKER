# VOTER ID ELIGIBILITY CHECKER
print("WELCOME TO VOTER ID ELIGIBILITY CHECKER")
# GIVE YOUR NAME
voter = input("ENTER YOUR NAME = ")
while True: # This While Loop is used to repeat the process if the user input is invalid
    country = "india"
    user = input("Enter Your Country Name :- ").lower()

    if user != country:
        print(f"Sorry {voter} Your are not Indian Citizen")
        break # this break statement is used to exit the loop if the user is not from India
    age = int(input("Enter Your Age :- "))
    if age >= 18:
        print("Your Are Eliglable for Voter ID")

    elif age < 18:
        print(F"SORRY {voter} Your not Eliglable For Voter ID ")

    repeat = input("Do you want to check again? (yes/no): ").lower()
    if repeat != "yes":
        print("Thank you for using Voter ID Eligibility Checker! 🙏")
        break