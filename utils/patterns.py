def patterns():
    while True:
        try:
            print("<----------------------------------->")
            print("|          Patterns Menu            |")
            print("<----------------------------------->")
            print("| [1] Search Pattern                |")
            print("| [2] Store Pattern                 |")
            print("| [3]                               |")
            print("<----------------------------------->")
            print("| [4] Return to main menu            |")
            print("<----------------------------------->")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                print("Returning to main menu...")
                return
            else:
                print("Please enter a valid choice from the menu.")
            
        except ValueError:
            print("Please enter a valid choice from the menu.")

def search():
    while True:
        try:
            print("<----------------------------------->")
            print("|          Search a Pattern         |")
            print("<----------------------------------->")
            print("| What would you like to learn?     |")
            print("| [1] Clothes                       |")
            print("| [2] Headwears                     |")
            print("| [3] Bags                          |")
            print("| [4] Amigurumis                    |")
            print("<----------------------------------->")
            print("| [5] Return to patterns menu       |")
            print("<----------------------------------->")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                clothes()
            elif choice == 2:
                headwears()
            elif choice == 3:
                bags()
            elif choice == 4:
                amigurumis()
            elif choice == 5:
                print("Returning to patterns menu...")
                return
            else:
                print("Please enter a valid choice from the menu.")

        except ValueError:
            print("Please enter a valid choice from the menu.")

def clothes():
    while True:
        try:
            print("<----------------------------------->")
            print("|             Clothes               |")
            print("<----------------------------------->")
            print("| [1]                               |")
            print("| [2]                               |")
            print("| [3]                               |")
            print("<----------------------------------->")
            print("| [4] Return to search menu         |")
            print("<----------------------------------->")

        except ValueError:
            print("Please enter a valid choice from the menu.")

def headwears():
    while True:
        try:
            print("<----------------------------------->")
            print("|             Headwears             |")
            print("<----------------------------------->")
            print("| [1]                               |")
            print("| [2]                               |")
            print("| [3]                               |")
            print("<----------------------------------->")
            print("| [4] Return to search menu         |")
            print("<----------------------------------->")

        except ValueError:
            print("Please enter a valid choice from the menu.")

def bags():
    while True:
        try:
            print("<----------------------------------->")
            print("|                Bags               |")
            print("<----------------------------------->")
            print("| [1]                               |")
            print("| [2]                               |")
            print("| [3]                               |")
            print("<----------------------------------->")
            print("| [4] Return to search menu         |")
            print("<----------------------------------->")

        except ValueError:
            print("Please enter a valid choice from the menu.")

def amigurumis():
    while True:
        try:
            print("<----------------------------------->")
            print("|            Amigurumis             |")
            print("<----------------------------------->")
            print("| [1]                               |")
            print("| [2]                               |")
            print("| [3]                               |")
            print("<----------------------------------->")
            print("| [4] Return to search menu         |")
            print("<----------------------------------->")

        except ValueError:
            print("Please enter a valid choice from the menu.")