import api

# Define a dictionary of stations and their corresponding station IDs
stations = {
    "Howard": "40900",
    "Jarvis": "41190",
    "Morse": "40100",
    "Loyola": "41300",
    "Granville": "40760",
    "Thorndale": "40880",
    "Bryn Mawr": "41380",
    "Argyle": "41200",
    "Wilson": "40540",
    "Sheridan": "40080",
    "Addison": "41420",
    "Belmont": "41320",
    "Fullerton": "41220",
    "Clark / Division": "40630",
    "Chicago": "41450",
    "Grand": "40330",
    "Lake": "41660",
    "Monroe": "41090",
    "Jackson": "40560",
    "Harrison": "41490",
    "Roosevelt": "41400",
    "Cermak - Chinatown": "41000",
    "Sox - 35th": "40190",
    "47th": "41230",
    "Garfield": "41170",
    "63rd": "40910",
    "69th": "40990",
    "79th": "40240",
    "87": "41430",
    "95th / Dan Ryan": "40450"
}


def redline():
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
    station_name = list(stations.keys())[choice-1]
    station_code = stations[station_name]
    api.call(station_code)