class User:
    def __init__(self, username, password):
        self.Username = username
        self.Password = password

class UserList:
    def __init__(self, filename):
        self.user_list = []
        self.filename = filename

    def read_user_file(self):
        finalproject = open(self.filename, 'r')
        y = finalproject.readline()
        while y != "":
                username, password = y.split(",")
                user = User(username.strip(),  password.strip())
                self.user_list.append(user)
                y = finalproject.readline()
        finalproject.close()    

    def write_user_file(self):
        finalproject = open(self.filename, "w")
        for i in range (len(self.user_list)):
                finalproject.write(self.user_list[i].Username + "," + self.user_list[i].Password + "\n")

    def display_user_list(self):
        #print("Username        Password")
        print("{:>15s} {:>15s}".format("Username", "Password"))
        print("{:>15s} {:>15s}".format("-"*15, "-"*15))
        #print("-"*15,  "-"*15 )
        for i in range(len(self.user_list)):
            print("{:>15s}{:>15s}".format(self.user_list[i].Username, self.user_list[i].Password))

    def find_username(self, username):
        for i in range (len(self.user_list)):
            if self.user_list[i].Username == username:
                return i
        return -1

    def change_password(self, username, password_change):
        index = self.find_username(username)
        if index != -1:
            strength = self.strength(password_change)
            if strength >= 5:
            
                self.user_list[index].Password = password_change
                print("Password Changed")
            else:
                print("Password is weak")
        
        else:
            print("Username Not Found")

    def add_user(self, username, password):
        if self.find_username(username) == -1:
            strength = self.strength(password)
            if strength >= 5:
                new_user = User(username, password)
                self.user_list.append(new_user)
                print("User Added")
            else:
                print("This password is weak -3")
        else:
            print("Username Already Exists")

    def delete_user(self, username):
        index = self.find_username(username)
        if index != -1:
            del self.user_list[index]
            print("User Deleted")
        else:
            print("Username Not Found")

    
    def strength(self, password):
        power = 0
        specialcharacter = "~!@#$%^&*()_+|-={}[]:;<>?/"
        number = "0123456789"
        if len(password) >= 8:
            power += 1
        lowercasefound = False
        uppercasefound = False 
        specialcharacterfound = False
        numbersfound = False
        #if re.search(r"[A-Z]", password):
           # strength += 1
        #if re.search(r"[a-z]", password):
           # strength += 1
       # if re.search(r"[0-9]", password):
           # strength += 1
       # if re.search(r"[~!@#$%^&*()_+|-={}[\]:;<>?/]", password):
           # strength += 1
        #return strength

        for i in range(len(password)):
            if password[i].islower():
                lowercasefound = True
            if password[i].isupper():
                uppercasefound = True
            for j in range (len(specialcharacter)):
                if password[i] == specialcharacter[j]:
                    specialcharacterfound = True
            for j in range (len(number)):
                if password[i] == number[j]:
                    numbersfound = True 
        if lowercasefound == True:
            power += 1
        if uppercasefound == True:
            power += 1
        if specialcharacterfound == True:
            power += 1
        if numbersfound == True:
            power += 1

        return power

userlist = UserList("Final Project Passwords.txt")
userlist.read_user_file()
print()

print("1) Add a New User")
print("2) Delete an Existing User")
print("3) Change Password on an Existing User")
print("4) Display All Users")
print("5) Save Changes to File")
print("6) Quit")

choice = input("Enter Selection: ")

while choice != "6":   
    if choice == "1":
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        userlist.add_user(username, password)
        

    elif choice == "2":
        username = input("Enter username to delete: ")
        userlist.delete_user(username)

    elif choice == "3":
        username = input("Enter username: ")
        password = input("Enter a new password: ")
        userlist.change_password(username, password)

    elif choice == "4":
         userlist.display_user_list()

    elif choice == "5":
        userlist.write_user_file()
        print("Changes Saved")

    elif choice == "6":
        userlist.write_user_file()
        print("Exited program")

    else:
        print("Invalid Selection")
    

    print("1) Add a New User")
    print("2) Delete an Existing User")
    print("3) Change Password on an Existing User")
    print("4) Display All Users")
    print("5) Save Changes to File")
    print("6) Quit")

    choice = input("Enter Selection: ")