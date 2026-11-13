"""Ross Gallagher
banner ID:B01886848
date: 2/6/2024"""



def main():

 #  Create a dictionary containing security incident information
    incident = {
        "username": "admin",
        "IP address": "192.168.1.10",
        "event type": "Failed login",
        "risk level": "High"
    }

    #  Display the username and IP address
    print("Username:", incident["username"])
    print("IP Address:", incident["IP address"])

    #  Add a new field called status
    incident["status"] = "Under investigation"

    #  Update the risk level
    incident["risk level"] = "Medium"

    #  Remove one field from the dictionary
    del incident["event type"]

    #  Display all remaining keys and values
    print("\nUpdated Security Incident:")

    for key, value in incident.items():
        print(key, ":", value)

    #  Display the total number of key-value pairs
    print("\nTotal number of fields:", len(incident))
main()