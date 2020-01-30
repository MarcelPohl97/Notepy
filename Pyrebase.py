import pyrebase
from pprint import pprint

class Database:
    def __init__(self):
        self.config = {
        "apiKey": "AIzaSyAmyCuK6ZtTuJ4AeX8sGYA0CbVV2V-zr78",
        "authDomain": "trellpy.firebaseapp.com",
        "databaseURL": "https://trellpy.firebaseio.com",
        "projectId": "trellpy",
        "storageBucket": "trellpy.appspot.com",
        "messagingSenderId": "892327697068",
        "appId": "1:892327697068:web:79b2eb1444158d07fc5d09",
        "measurementId": "G-PR3LFLQBMG"
    }
        self.firebase = pyrebase.initialize_app(self.config)
        self.db = self.firebase.database()

    def login_details(self):
        self.company_name = input("Type in the company your working for")
        self.company_id = input("Type in your compandy id ")
        self.company_user = input("Type in your username")
        self.company_pw = input("Type in the company pw that your company has set")

    def database_querys(self):
        self.company_id_query = self.db.child("company").child(self.company_name).child("id").get()
        self.company_pw_query = self.db.child("company").child(self.company_name).child("company_pw").get()
        self.user_id_query = self.db.child("company").child(self.company_name).child("company_user").child(self.company_user).child("name").get()
        self.trellpy_pads_query = self.db.child("company").child(self.company_name).child("company_trellpypads").get()

    def add_new_trellpy_pad(self, trellpy_pad_title):
        self.data = {"example": "example"}
        self.db.child("company").child(self.company_name).child("company_trellpypads").child(trellpy_pad_title).set(self.data)

    def add_update_trellpy_pad_entry(self, trellpy_pad_title, trellpy_pad_listbox_entry):
        self.data = {trellpy_pad_listbox_entry: trellpy_pad_listbox_entry}
        self.db.child("company").child(self.company_name).child("company_trellpypads").child(trellpy_pad_title).update(self.data)

    def delete_trellpy_pad(self, trellpy_pad_title):
        self.db.child("company").child(self.company_name).child("company_trellpypads").child(trellpy_pad_title).remove()

    def delete_trellpy_pad_entry(self, trellpy_pad_title, trellpy_pad_listbox_entry):
        self.db.child("company").child(self.company_name).child("company_trellpypads").child(trellpy_pad_title).child(trellpy_pad_listbox_entry).remove()

    def login(self):
        if self.company_id == self.company_id_query.val() and self.company_pw == self.company_pw_query.val():
            print(f"Hello {self.user_id_query.val()} your logged in now")

    def get_trellpy_pads(self):
        self.trellpads = []
        for self.trellpypads in self.trellpy_pads_query:
            self.trellpads.append(self.trellpypads.key())
            #self.trellpy_pads_entry_query = self.db.child("company").child(self.company_name).child("company_trellpypads").child(self.trellpypads.key()).get()
            #for self.trellpypads_entry in self.trellpy_pads_entry_query.each():
                #self.trellpads.append(self.trellpypads_entry.val())
            print(self.trellpads)




