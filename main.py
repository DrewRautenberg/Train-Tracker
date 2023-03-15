import api
import stations


def select():
    print("Please select a Line:")
    print("1. Red")
    print("2. Blue")
    print("3. Green")
    print("4. Brown")
    print("5. Purple")
    print("6. Pink")
    print("7. Orange")
    print("8. Yellow")

    choice = input("Enter your choice: ")

    if choice == "1":
        api.stationSelection(stations.redLine)
    elif choice == "2":
        api.stationSelection(stations.blueLine)
    elif choice == "3":
        api.stationSelection(stations.greenLine)
    elif choice == "4":
        api.stationSelection(stations.brownLine)
    elif choice == "5":
        api.stationSelection(stations.purpleLine)
    elif choice == "6":
        api.stationSelection(stations.pinkLine)
    elif choice == "7":
        api.stationSelection(stations.orangeLine)
    elif choice == "8":
        api.stationSelection(stations.yellowLine)
    else:
        print("Please select a valid Station")


select()
