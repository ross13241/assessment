"""Ross Gallagher
banner ID:B01886848
date: 2/6/2024"""



from ipaddress import ip_address


def validate_ip(ip):

    # Remove unnecessary spaces
    ip = ip.strip()

    # Check if the IP address contains dots
    if "." not in ip:
        return False

    # Check if there are exactly 3 dots
    if ip.count(".") != 3:
        return False

    # Split the IP address into 4 parts
    parts = ip.split(".")

    # Check if there are 4 numbers
    if len(parts) != 4:
        return False

    # Check each part of the IP address
    for part in parts:

        # Check if each part contains only numbers
        if not part.isdigit():
            return False

        # Convert the part into an integer
        number = int(part)

        # Check if the number is between 0 and 255
        if number < 0 or number > 255:
            return False

    # If all checks pass, return True
    return True


# Main program

ip_address = input("Enter an IP address: ")

if validate_ip(ip_address):
    print("Valid IP address")
else:
     print("Invalid IP address")
