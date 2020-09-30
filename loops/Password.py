
passWord = ""

while passWord != "redhat":
    passWord = input("Please enter the password: ")
    if passWord == "redhat":
        print("Correct password!")
    elif passWord == "admin@123":
        print("It was previously used password")
    elif passWord == "Redhat@123":
        print(f"{passWord} is your recent changed password")
    else:
        print("Incorrect Password- try again!")
