train=input("Enter seat type(sleeper/AC/general/luxury)").lower()

match train:
    case "sleeper":
        print("sleeper")
    case "ac":
        print("ac")
    case "general":
        print("general")
    case "luxury":
        print("luxury")
    case _:
        print("Invalid")
    