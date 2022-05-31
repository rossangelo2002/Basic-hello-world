import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

status = "Screen"
firstName = ""
lastName = ""
email = ""
password = ""


def sign_in():
    global status
    status = "Sign"
    print("\nSign In Page")
    tries = 0

    while status != "Home" and tries != 3:
        # print(email)
        # print(password)
        signInEmail = input("Enter Email: ")
        signInPassword = input("Enter Password: ")
        for i in range(len(users)):
            if users[i]['email'] == signInEmail and users[i]["password"] == signInPassword:
                status = "Home"
                print("\n/***************************************/")
                print("Welcome " + users[i]["firstName"] + " " + users[i]["lastName"])
                print("/***************************************/")
                print("\nWelcome to My University\nPress\n[C]hange password\n[L]og out\n[E]xit")
                action = input("Action: ").upper()
                if action == "C":
                    change_pass(i)
                elif action == "L":
                    print("\"You have been log out.\"")
                    status = "Screen"
                    tries = 3
                elif action == "E":
                    action = "E"

        if status != "Home" and status != "Screen":
            tries += 1
            print("The email/password that you've entered is incorrect.")


def register():
    global status, firstName, lastName, email, password
    status = "Register"
    print("\nRegistration Page")
    firstName = input("Enter First name: ").lower()
    lastName = input("Enter Last name: ").lower()
    print("\n/***************************************/")
    print("Success! Please save the information below: ")
    print("First Name: " + firstName)
    print("First Name: " + lastName)
    print("Email: " + generate_email(firstName, lastName))
    print("Password: " + generate_password())
    print("/***************************************/")
    print("\nAccounts: ")
# now let's add objects
    x = {"email": email,
         "password": password,
         "firstName": firstName,
         "lastName": lastName}
    
    users.append(x)
    print(users)


def change_pass(i):
    newpassword = input("Enter newpassword: ").lower()
    users[i]["password"] = newpassword
    password = ("New password: " + newpassword)
    print(password)
    print("\nAccounts: ")
    print(users)

# generate_password()
def generate_password():

    random.shuffle(characters)

    p = []
    for i in range(8):
        p.append(random.choice(characters))

    random.shuffle(p)
    global password
    password = "".join(p)
    return password


def generate_email(fname,lname):
    global email
    email = fname+lname+"@university.com"
    return fname+lname+"@university.com"

global users
users = []

action = "S"

while action != "E":
    status = "Screen"
    print("\nWelcome to My University\nPress\n[R]egister\n[S]ign in\n[E]xit")
    action = input("Action: ").upper()
    if action == "S":
        sign_in()
    elif action == "R":
        register()
    elif action == "E":
        print("Sayonara.")
    else:
        print("Invalid Input")
