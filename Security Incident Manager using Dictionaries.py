
def main():

    # Create a dictionary containing security incident information
    incident = {
        "username": "admin",
        "IP address": "192.168.1.10",
        "event type": "Failed login",
        "risk level": "High"
    }

    # Display the security incident information
    print("Username:", incident["username"])
    print("IP Address:", incident["IP address"])
    print("Event Type:", incident["event type"])
    print("Risk Level:", incident["risk level"])

    # Add a new field called status
    status = input("Enter status: ")
    incident["status"] = status

    # Update the risk level
    risk = input("Enter new risk level: ")
    incident["risk level"] = risk

    # Remove one field from the dictionary
    field = input("Enter field to remove: ")

    if field in incident:
        del incident[field]
        print("Field removed successfully.")
    else:
        print("Field not found.")

    # Display all remaining keys and values
    print("\nUpdated Security Incident:")

    for key, value in incident.items():
        print(key, ":", value)

    # Display the total number of key-value pairs
    print("\nTotal number of fields:", len(incident))


main()
