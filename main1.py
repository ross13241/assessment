"""Ross Gallagher
banner ID:B01886848
date: 2/6/2024"""


import security_tools


def main():

    print("Security tools module imported successfully.")

    # Ask user for password and IP address
    password = input("Enter a password: ")
    ip = input("Enter an IP address: ")

    # Check password
    if security_tools.validate_password(password):
        print("Password is valid.")

    else:
        print("Password is invalid.")
        print("Suggested strong password:",
              security_tools.generate_password())

    # Check IP address
    if security_tools.validate_ip(ip):
        print("IP address is valid.")

    else:
        print("IP address is invalid. It must be in the format x.x.x.x where each number is between 0 and 255.")


main()

