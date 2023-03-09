import api


def redline():
    print("Please select a Station:")
    print("1.  Howard       11. Addison             21. Roosevelt")
    print("2.  Jarvis       12. Belmont             22. Cermak - Chinatown")
    print("3.  Morse        13. Fullerton           23. Sox - 35th")
    print("4.  Loyola       14. Clark / Division    24. 47th")
    print("5.  Granville    15. Chicago             25. Garfield")
    print("6.  Thorndale    16. Grand               26. 63rd")
    print("7.  Bryn Mawr    17. Lake                27. 69th")
    print("8.  Argyle       18. Monroe              28. 79th")
    print("9.  Wilson       19. Jackson             29. 87")
    print("10. Sheridan     20. Harrison            30. 95th / Dan Ryan")

    choice = input("Enter your choice: ")

    if choice == "1":  # Howard
        api.call("40900")
    elif choice == "2":  # Jarvis
        api.call("41190")
    elif choice == "3":  # Morse
        api.call("40100")
    elif choice == "4":  # Loyola
        api.call("41300")
    elif choice == "5":  # Granville
        api.call("40760")
    elif choice == "6":  # Thorndale
        api.call("40880")
    elif choice == "7":  # Bryn Mawr
        api.call("41380")
    elif choice == "8":  # Argyle
        api.call("41200")
    elif choice == "9":  # Wilson
        api.call("40540")
    elif choice == "10":  # Sheridan
        api.call("40080")
    elif choice == "11":  # Addison
        api.call("41420")
    elif choice == "12":  # Belmont
        api.call("41320")
    elif choice == "13":  # Fullerton
        api.call("41220")
    elif choice == "14":  # Clark / Division
        api.call("40630")
    elif choice == "15":  # Chicago
        api.call("41450")
    elif choice == "16":  # Grand
        api.call("40330")
    elif choice == "17":  # Lake
        api.call("41660")
    elif choice == "18":  # Monroe
        api.call("41090")
    elif choice == "19":  # Jackson
        api.call("40560")
    elif choice == "20":  # Harrison
        api.call("41490")
    elif choice == "21":  # Roosevelt
        api.call("41400")
    elif choice == "22":  # Cermak - Chinatown
        api.call("41000")
    elif choice == "23":  # Sox - 35th
        api.call("40190")
    elif choice == "24":  # 47th
        api.call("41230")
    elif choice == "25":  # Garfield
        api.call("41170")
    elif choice == "26":  # 63rd
        api.call("40910")
    elif choice == "27":  # 69th
        api.call("40990")
    elif choice == "28":  # 79th
        api.call("40240")
    elif choice == "29":  # 87
        api.call("41430")
    elif choice == "30":  # 95th / Dan Ryan
        api.call("40450")
    else:
        print("Please select a valid Station")
