import getpass

p = getpass.getpass(prompt="what is your favorite color? ")
if p.lower() == "blue":
    print("right, off you go.")
else:
    print("Auuuuugh!")
