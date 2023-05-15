# Password Authentication is the process of checking the identity of a user. dictionary of usernames with their
# passwords we will use the getpass module instead of the input function to make sure that the user doesnt get to see
# what he's writing

import getpass
database = {"shirin.labay": "123456", "labay.shirin": "456789"}
username = input("Enter your username: ")
password = getpass.getpass("Enter Your Password: ")
flag = 0
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter password again: ")
        break

print("verified!")
