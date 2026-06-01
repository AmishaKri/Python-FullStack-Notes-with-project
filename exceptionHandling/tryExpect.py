def serveChai(flavor):
    try:
        
        print(f"Inside function {flavor}")
        if flavor == "unknown":
            raise ValueError(f"Unknown flavor: {flavor}")
    except ValueError as e:
        print("Error message:", e)
        
    else:
        print("No exception")
        
    finally:
        print("Cleaning up")
        
serveChai("unknown")
        