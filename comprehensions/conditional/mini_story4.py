device_status=input("Enter device status(active/off)").lower()
temperature=int(input("Enter temp"))

if device_status=="active":
    if temperature>35:
        print(f"High tempererature alert:")
    else:
        print(f"Temperature is low")
else:
    print(f"off")
      