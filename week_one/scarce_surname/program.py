surname: str = input("What is your surname? ").strip(" ").lower()

if surname.startswith("q"):
    print("You have an extremely rare surname!")
elif "q" in surname:
    print("You have a rare surname!")
else:
    print("No Qs here.")
