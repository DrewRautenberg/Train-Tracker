import api


def redline():
    print("Please select a Station:")
    print("1. Argyle")
    print("2. Addison")
    print("3. Belmont")
    print("4. Fullerton")
    print("5. Lake")

    choice = input("Enter your choice: ")

    if choice == "1":
        api.call("41200")
    elif choice == "2":
        api.call("41420")
    elif choice == "3":
        api.call("41320")
    elif choice == "4":
        api.call("41220")
    elif choice == "5":
        api.call("41660")
    else:
        print("Please select a valid Station")
