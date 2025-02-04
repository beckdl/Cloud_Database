import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('D:\Key\documentorganizer-ee4cc-2a8f378aed71.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

place = "users"
choice = 0

print("Hello welcome to my user database.\nThere is some pre-populated information but you can change that if you want.")

while(choice != "5"):
    choice = input(f"You are currently in '{place}'\n\nWhat would you like to do?\n\n1. Read\n2. Write\n3. Modify\n4. Delete\n5. Exit\n\n")

    if choice == "1":
        print("choice 1")
    elif choice == "2": 
        print("choice 2")
    elif choice == "3":
        print("choice 3")
    elif choice == "4":
        print("choice 4")
    elif choice == "5":
        print("")
        break
    else:
        print("What you have entered is incorrect. Please try again.\n")
        
end = input("Thank you for visiting! Press enter to exit")

#doc_ref = db.collection("users").document("alovelace")
#doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})
#
#doc_ref = db.collection("users").document("aturing")
#doc_ref.set({"first": "Alan", "middle": "Mathison", "last": "Turing", "born": 1912})

#users_ref = db.collection("users")
#docs = users_ref.stream()
#
#for doc in docs:
#    print(f"{doc.id} => {doc.to_dict()}")