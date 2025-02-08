import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('D:\Key\documentorganizer-ee4cc-2a8f378aed71.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

# Initialization and constant variables
place = "todo"
choice = 0

print("Hello welcome to your To-Do List.\n\n")

# menu for user to choose what they want to do
while(choice != "5"):
    choice = input(f"What would you like to do? (Please type a number)\n\n1. List of to-do's\n2. Make new To-do\n3. Edit\n4. Delete\n5. Exit\n\n")
    print("")
    # print out the list of to-do's
    if choice == "1":
        print("Here are your to-do's:\n")
        todo_ref = db.collection(place)
        docs = todo_ref.stream()
        for doc in docs:
           print(f"{doc.to_dict()}")
        print("")
    # add a new to-do
    elif choice == "2": 
        title = input("What is the title of the to-do? (It must be one word)\n")
        description = input("What is the description of the to-do?\n")
        doc_ref = db.collection(place).document("start")
        doc_ref.set({title: description}, merge=True)
        print(f"\n{title} has been added to your to-do list.\n")
    # edit a to-do
    elif choice == "3": 
        print("choice 3")
        edittitle = input("What is the title of the to-do you would like to edit?\n")
        editdescription = input("What is the new description of the to-do?\n")
        doc_ref = db.collection(place).document("start")
        doc_ref.update({edittitle: firestore.DELETE_FIELD})
        doc_ref.set({edittitle: editdescription}, merge=True)
        print(f"\n{edittitle} has been edited in your to-do list.\n")
    # delete a to-do
    elif choice == "4":
        print("choice 4")
        deltitle = input("What is the title of the to-do you would like to delete?\n")
        doc_ref = db.collection(place).document("start")
        doc_ref.update({deltitle: firestore.DELETE_FIELD})
        print(f"\n{deltitle} has been deleted from your to-do list.\n")
    # exit the program
    elif choice == "5":
        print("")
        break
    # if the user enters an incorrect number
    else:
        print("What you have entered is incorrect. Please try again.\n")
        
end = input("Thank you for visiting! Press enter to exit")

