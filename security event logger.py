"""Ross Gallagher
banner ID:B01886848
date: 2/6/2024"""



import random
import socket
from datetime import datetime
def main():
    # Correct login details
    correct_username = "admin"
    correct_password = "ross12"

    #  Get the computer's IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()

    # Login system
    authenticated = False

    print("SECURITY EVENT LOG")
    print("==================")

    while authenticated == False:

        # Asking for a username and password
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Generating an event ID
        event_id = random.randint(1000, 9999)

        # Get current date and time
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Checking login details
        if username == correct_username and password == correct_password:

            print("\nEvent ID:", event_id)
            print("Username:", username)
            print("IP Address:", ip_address)
            print("Event: Successful login")
            print("Timestamp:", timestamp)

            print("\nLogin successful!")
            authenticated = True

        else:

            print("\nEvent ID:", event_id)
            print("Username:", username)
            print("IP Address:", ip_address)
            print("Event: Failed login")
            print("Timestamp:", timestamp)

            print("\nIncorrect username or password. Try again.")

main()

