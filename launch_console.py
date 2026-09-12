print("Hi, welcome to Launch Console!")
print()

def about_me(name):
    return (
        f"I'm {name}, a junior in High School, trying to find my foot in the world!"
    )

def my_goals():
    return (
        "Ship something this term that is actually useful and create an efficient framework for working as a team."
    )

def what_im_building():
    return (
        "A four-script hardening suite that takes a messy Windows image to CIS-benchmarked in just a matter of a few minutes (it has broken in interesting ways)!"
    )

def show_menu():
    print()
    print("1) About me")
    print("2) My goals")
    print("3) What I'm building")
    print("4) Exit")
    print()

name = input("What's your name? ")
print(f"Welcome to {name}'s Launch Console!")

running = True
while running:
    show_menu()
    choice = input("Pick 1-4: ")

    if choice == "1":
        print(about_me(name))
    elif choice == "2":
        print(my_goals())
    elif choice == "3":
        print(what_im_building())
    elif choice == "4":
        print(f"Goodbye, {name}!")
        running = False
    else:
        print("Please pick 1, 2, 3, or 4.")
