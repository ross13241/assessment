"""Ross Gallagher
banner ID:B01886848
date: 2/6/2024"""


def security_event_counter(): #this function will count the number of correct and incorrect passwords entered by the user

    correct_password = "ross12" #this is the correct password 
    correct_count = 0
    incorrect_count = 0

    for i in range(10): #this loop will run 10 times to get 10 password inputs from the user
        password = input("Enter password: ") # this will prompt the user to enter a password

        if password == correct_password: #this will check if the password entered is correct or not
            print("Correct password") #this will print if the password entered is correct
            correct_count += 1 #this will increment the correct password count by 1
        else:
            print("Incorrect password")
            incorrect_count += 1 #this will increment the incorrect password count by 1

    percentage = (incorrect_count / 10) * 100 #this will calculate the percentage of incorrect passwords entered by the user

    print("Correct passwords:", correct_count)
    print("Incorrect passwords:", incorrect_count)
    print("Percentage incorrect:", percentage, "%")

    if percentage > 50:
        print("ALERT: More than 50% of passwords were incorrect!")


def brute_force_simulation(): #this function will simulate a brute-force attack by allowing the user to guess a password multiple times

    correct_password = "ross12"
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts: #this loop will run until the user has made 5 attempts to guess the password

        guess = input("Guess the password: ") #this will prompt the user to guess the password
        attempts += 1

        if guess == correct_password: #this will check if the password guessed by the user is correct or not
            print("Password cracked!")
            break #this will break the loop if the password guessed by the user is correct
        else:
            print("Incorrect password")
            print("Attempts remaining:", max_attempts - attempts)

    if attempts == max_attempts and guess != correct_password:
        print("Maximum attempts reached. Access denied.")


def login_authentication(): #this function will authenticate the user by checking if the username and password entered are correct

    correct_username = "admin"
    correct_password = "ross12"
    failed_attempts = 0
    max_attempts = 3

    while failed_attempts < max_attempts: #this loop will run until the user has made 3 failed attempts to login

        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password: #this will check if the username and password entered by the user are correct or not
            print("Authentication successful!")
            break

        else:
            print("Authentication failed!")
            failed_attempts += 1 #this will increment the failed attempts count by 1
            print("Failed attempts:", failed_attempts)

    if failed_attempts == max_attempts: #this will check if the user has made 3 failed attempts to login
        print("Account frozen for 24 hours.")


# Main program

authenticated = False #this variable will be used to check if the user is authenticated or not

while authenticated == False: #this loop will run until the user is authenticated

    username = input("Enter program username: ")
    password = input("Enter program password: ")

    if username == "admin" and password == "ross12": #this will check if the username and password entered by the user are correct or not
        print("Authentication successful!")
        authenticated = True
    else:
        print("Incorrect username or password. Try again.")


# Security menu

choice = ""

while choice != "4":

    print("\n===== SECURITY TOOL =====")
    print("1. Security Event Counter")
    print("2. Brute-Force Simulation")
    print("3. Login Authentication")
    print("4. Exit")

    choice = input("Select an option: ").strip()

    if choice == "1":
        security_event_counter()

    elif choice == "2":
        brute_force_simulation()

    elif choice == "3":
        login_authentication()

    elif choice == "4":
        print("Thank you for using the security tool")

    else:
        print("Invalid option. Please try again.")
