class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserList:
    def __init__(self, filename):
        self.user_list = []
        self.filename = filename

    def read_user_file(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                username, password = line.strip().split(',')
                self.user_list.append(User(username, password))

    def write_user_file(self):
        with open(self.filename, 'w') as file:
            for user in self.user_list:
                file.write(f"{user.username},{user.password}\n")

    def display_user_list(self):
        print("Username        Password")
        print("-"*15,  "-"*15 )
        for user in self.user_list:
            print(f"{user.username.ljust(15)} {user.password}")

    def find_username(self, username):
        for i, user in enumerate(self.user_list):
            if user.username == username:
                return i
        return -1

    def change_password(self, username, password):
        index = self.find_username(username)
        if index != -1:
            self.user_list[index].password = password
            print("Password Changed")
        else:
            print("Username Not Found")

    def add_user(self, username, password):
        if self.find_username(username) == -1:
            self.user_list.append(User(username, password))
            print("User Added")
        else:
            print("Username Already Exists")

    def delete_user(self, username):
        index = self.find_username(username)
        if index != -1:
            del self.user_list[index]
            print("User Deleted")
        else:
            print("Username Not Found")

    
    def strength(password):
        strength = 0
        if len(password) >= 8:
            strength += 1
        if re.search(r"[A-Z]", password):
            strength += 1
        if re.search(r"[a-z]", password):
            strength += 1
        if re.search(r"[0-9]", password):
            strength += 1
        if re.search(r"[~!@#$%^&*()_+|-={}[\]:;<>?/]", password):
            strength += 1
        return strength


file_name = "Final Project Passwords.txt"
user_list = UserList(file_name)
user_list.read_user_file()


print("1) Add a New User")
print("2) Delete an Existing User")
print("3) Change Password on an Existing User")
print("4) Display All Users")
print("5) Save Changes to File")
print("6) Quit")

choice = input("Enter Selection: ")

    if choice == '1':
        username = input("Enter username: ")
        if user_list.find_username(username) != -1:
            print("Username Already Exists")
        else:
            password = input("Enter password: ")
            while user_list.strength(password) < 5:
                print("This password is weak")
                password = input("Enter a stronger password: ")
            user_list.add_user(username, password)

    elif choice == '2':
        username = input("Enter username: ")
        user_list.delete_user(username)

    elif choice == '3':
        username = input("Enter username: ")
        if user_list.find_username(username) != -1:
            password = input("Enter new password: ")
            while user_list.strength(password) < 5:
                print("This password is weak")
                password = input("Enter a stronger password: ")
            user_list.change_password(username, password)
        else:
            print("Username Not Found")

    elif choice == '4':
         user_list.display_user_list()

    elif choice == '5':
        user_list.write_user_file()
        print("Changes Saved")

    elif choice == '6':
        break

    else:
        print("Invalid Selection")