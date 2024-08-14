from utils.user_manager import UserManager
from utils.user import User
from utils.tools import tools
from utils.yarns import yarns
from utils.stitches import stitches_menu
from utils.patterns import patterns

usermanager = UserManager()
user = User()

def menu():
    while True:
        try:
            print("<----------------------------------->")
            print("|             Welcome!              |")
            print("<----------------------------------->")
            print("| [1] Sign-up                       |")
            print("| [2] Log-in                        |")
            print("<----------------------------------->")
            print("| [3] Exit                          |")
            print("<----------------------------------->")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                usermanager.clear_screen()
                sign_up()
            elif choice == 2:
                usermanager.clear_screen()
                log_in()
            elif choice == 3:
                print("\nExiting...")
                quit()
            else:
                print("Please enter a valid choice from the menu.")

        except ValueError:
            print("Please enter a valid choice from the menu.")

def sign_up():
    print("*-----------------------------------*")
    print("*             SIGN-UP               *")
    print("*-----------------------------------*")

    while True:
        username = usermanager.username_input()

        if username == "x" or username == "X":
            usermanager.clear_screen()
            return
        
        if not user.username_exists(username):
            break
        print("Username already exists.")
    
    user.set_username(username)

    password = usermanager.password_input()
    user.set_password(password)

    user.save_user()

    usermanager.clear_screen()
    print(f"Sign-up successful! Welcome, {username}!")
    usermanager.press_return()

def log_in():
    print("*-----------------------------------*")
    print("*             LOG-IN                *")
    print("*-----------------------------------*")   

    while True:
        username = usermanager.username_input()

        if username == "x" or username == "X":
            usermanager.clear_screen()
            return
        
        password = usermanager.password_input()

        if user.load_user(username, password):
            usermanager.clear_screen()
            print(f"Login successful! Welcome back, {username}!")
            usermanager.press_return()
            main_menu()
        else:
            usermanager.clear_screen()
            print("Invalid username or password.")
            usermanager.press_return()

def main_menu():
    while True:
        try:
            print("<----------------------------------->")
            print("|        Welcome to Krochet!        |")
            print("<----------------------------------->")
            print("| What do you want to learn?        |")
            print("| [1] Crochet Tools                 |")
            print("| [2] Yarns Description             |")
            print("| [3] Stitch Learning Assistant     |")
            print("| [4] Crochet Patterns              |")
            print("| [5] Your Yarn Stash               |")
            print("| [6] Project Color Suggester       |")
            print("<----------------------------------->")
            print("| [7] Log out                       |")
            print("<----------------------------------->")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                tools()
            elif choice == 2:
                yarns()
            elif choice == 3:
                stitches_menu()
            elif choice == 4:
                patterns()
            elif choice == 5:
                pass
            elif choice == 6:
                pass
            elif choice == 7:
                print("Logging out...")
                return
            else:
                print("Please enter a valid choice from the menu.")

        except ValueError:
            print("Please enter a valid choice from the menu.")
