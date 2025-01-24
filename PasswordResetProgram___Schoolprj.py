def passwordChecker(password):
    containLower = False # int of vars
    containUpper = False
    containSpecial = False
    valid = False
    security = None
    specialSym = ["@", "!", "$", "%", "&", "*", "#", "?", "."]
    if len(password) < 8: # checks for length
        print("Error, Password less than 8 char...")
    security = "Low"
    for char in password: # checks for lower or uppercase
        if char == char.lower():
            containLower = True
        elif char == char.upper():
            containUpper = True
        else:
            print("No lowercase or upper case.")
    for sym in specialSym: # checks for special chars
        if sym in password:
            containSpecial = True
    if containLower == True and containUpper == True:
        security = "Low"
        if len(password) > 10: # ajusting security
            security = "Medium"
        if containSpecial == True:
            security = "High"
        valid = True
        return password, valid, security # returns as a tuple
    else:
        if containLower == False: # gives false if no lower or upper case
            print("No Lowercase Char... \nTry again...")
        elif containUpper == False:
            print("No Uppercase char... \nTry again...")

#main
while True:
    print("Make sure your password has min. 8 char, lower and uppercase. Special Symbols are optional.") # shows what to do
    password = input("What is your new password: ")
    debugfunc = passwordChecker(password)
    if debugfunc == None: # if no pass entered or nothing is returned
        print("You must enter a password")
    else:
        print("Your password is:", debugfunc[0], "\nValidity:", debugfunc[1], "\nSecurity Rating:", debugfunc[2]) # shows stats
        choice = input("Re-enter your password")
        if choice == debugfunc[0]:
            print("Password Confirmed...")
    # To exit program
    choice = input("Test new password? : ") # checks whether to continue
    if choice.lower() == "no" or choice.lower() == "n" or choice == "":
        print("Exiting Program...")
        break