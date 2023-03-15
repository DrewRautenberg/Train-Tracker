import api

# Define a dictionary of stations and their corresponding station IDs
stations = {
    "Midway": "40930",
    "Pulaski": "40960",
    "Kedzie": "41150",
    "Western": "40310",
    "35th / Archer": "40120",
    "Ashland": "41060",
    "Halsted": "41130",
    "Roosevelt": "41400",
    "Adams / Wabash": "40680",
    "Washington / Wabash": "41700",
    "State / Lake": "40260",
    "Clark / Lake": "40380",
    "Washington / Wells": "40730",
    "Quincy": "40040",
    "LaSalle / Van Buren": "40160",
    "Harold Washington Library - State / Van Buren": "40850"
}


def orangeline():
    # Print list of stations and their corresponding numbers
    print("Please select a Station:")
    for i, station in enumerate(stations, 1):
        print(f"{i}. {station}")

    # Prompt user for station choice
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice not in range(1, len(stations) + 1):
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid choice")

    # Call api with the chosen station code
    station_name = list(stations.keys())[choice - 1]
    station_code = stations[station_name]
    api.call(station_code)
