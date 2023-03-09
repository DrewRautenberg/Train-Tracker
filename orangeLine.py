import api


def orangeline():
    print("Please select a Station:")
    print("1.  Midway           11. State / Lake")
    print("2.  Pulaski          12. Clark / Lake")
    print("3.  Kedzie           13. Washington / Wells")
    print("4.  Western          14. Quincy")
    print("5.  35th / Archer    15. LaSalle / Van Buren")
    print("6.  Ashland          16. Harold Washington Library - State / Van Buren")
    print("7.  Halsted")
    print("8.  Roosevelt")
    print("9.  Adams / Wabash")
    print("10. Washington / Wabash")

    choice = input("Enter your choice: ")

    if choice == "1":  # Midway
        api.call("40930")
    elif choice == "2":  # Pulaski
        api.call("40960")
    elif choice == "3":  # Kedzie
        api.call("41150")
    elif choice == "4":  # Western
        api.call("40310")
    elif choice == "5":  # 35th / Archer
        api.call("40120")
    elif choice == "6":  # Ashland
        api.call("41060")
    elif choice == "7":  # Halsted
        api.call("41130")
    elif choice == "8":  # Roosevelt
        api.call("41400")
    elif choice == "9":  # Adams / Wabash
        api.call("40680")
    elif choice == "10":  # Washington / Wabash
        api.call("41700")
    elif choice == "11":  # State / Lake
        api.call("40260")
    elif choice == "12":  # Clark / Lake
        api.call("40380")
    elif choice == "13":  # Washington / Wells
        api.call("40730")
    elif choice == "14":  # Quincy
        api.call("40040")
    elif choice == "15":  # LaSalle / Van Buren
        api.call("40160")
    elif choice == "16":  # Harold Washington Library - State / Van Buren
        api.call("40850")

    else:
        print("Please select a valid Station")
