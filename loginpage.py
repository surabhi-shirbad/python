def login():
    while True:
        username=input("enter your name")
        password=input("enter your password")
        if username ==password:
         print("login successfully")
        else:
            print("invaild credentail")
    
login()            