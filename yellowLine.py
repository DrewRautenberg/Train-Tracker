import api


def yellowline():
    print("Please select a Station:")
    print("1. Dempster - Skokie")
    print("2. Oakton - Skokie")
    print("3. Howard")

    choice = input("Enter your choice: ")

    if choice == "1":
        api.call("40140")
    elif choice == "2":
        api.call("41680")
    elif choice == "3":
        api.call("40900")
    else:
        print("Please select a valid Station")


