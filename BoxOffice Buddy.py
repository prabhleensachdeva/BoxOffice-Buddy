import mysql.connector as msc
#-------------------------------------------------------------UPDATE-----------------------------------------------------------------------------
def update(rs): 
    choice = input("Do you want to change your password? (yes/no): ").strip().lower()
    if choice == "yes":
        while True:
            new_pass = input("Enter new password: ")
            recheck = input("Retype new password: ")
            if new_pass != recheck:
                print("New Password does not match the Retyped Password! TRY AGAIN.")
            else:
                break
    else:
        new_pass = rs[1]

    choice = input("Do you want to change your name? (yes/no): ").strip().lower()
    if choice == "yes":
        name = input("Enter new name: ")
    else:
        name = rs[2]

    choice = input("Do you want to change your phone number? (yes/no): ").strip().lower()
    if choice == "yes":
        phone = input("Enter new phone number: ")
    else:
        phone = rs[3]

    choice = input("Do you want to change your email ID? (yes/no): ").strip().lower()
    if choice == "yes":
        email = input("Enter new email ID: ")
    else:
        email = rs[4]

    choice = input("Do you want to change your city? (yes/no): ").strip().lower()
    if choice == "yes":
        city = input("Enter new city: ")
    else:
        city = rs[7]

    confirm = input("Are you sure you want to update your data? (yes/no): ").strip().lower()
    if confirm == "yes":
        Q = """
        UPDATE registration 
        SET password = '{}', Name = '{}', phone_no = '{}', email_id = '{}', city = '{}' 
        WHERE login_id = '{}'
        """.format(new_pass, name, phone, email, city, rs[0])
        
        mycon = msc.connect(host="localhost", user="root", password="prabhleen", database="project")
        mycursor = mycon.cursor()
        mycursor.execute(Q)
        mycon.commit()
        mycon.close()
        print("\nYour data has been successfully updated.")
    else:
        print("\nYour data has not been updated.")

    
    
#--------------------------------------------------NEW BOOKING -------------------------------------------------------------------------------------
def newbooking(rs):
    mycon = msc.connect(host="localhost", user="root", password="prabhleen", database="project")
    mycursor = mycon.cursor()
    mycursor.execute("SELECT * FROM movies;")
    result = mycursor.fetchall()

    print("\n" + "="*130)
    print(" AVAILABLE MOVIES ".center(130, "="))
    print("="*130)

    for i, row in enumerate(result, 1):
        print(f"{i}. {row[0]} ({row[1]}) - {row[2]}")  

    while True:
        choice = input("\nEnter your movie choice (1–{}): ".format(len(result)))
        if choice.isdigit() and 1 <= int(choice) <= len(result):
            selected_movie = result[int(choice) - 1]
            moviename = selected_movie[0]
            theatrename = selected_movie[4] 
            break
        else:
            print("Invalid choice. Please try again.")

    while True:
        date = input("Enter Date (DD-MM-YYYY): ")
        if len(date) == 10 and date[2] == '-' and date[5] == '-':
            days = int(date[:2])
            month = int(date[3:5])
            year = int(date[-4:])
            if 1 <= days <= 31 and 1 <= month <= 12 and year == 2024:
                break
        print("Please enter a valid date in DD-MM-YYYY format for year 2024.")

    print("\nChoose a show time:")
    print("1. 9:00 AM to 12:00 PM")
    print("2. 1:00 PM to 3:00 PM")
    print("3. 5:00 PM to 7:00 PM")
    print("4. 9:00 PM to 12:00 AM")

    show_times = {
        "1": "9:00 AM to 12:00 PM",
        "2": "1:00 PM to 3:00 PM",
        "3": "5:00 PM to 7:00 PM",
        "4": "9:00 PM to 12:00 AM"
    }

    while True:
        choice = input("Select show timing (1–4): ")
        if choice in show_times:
            time = show_times[choice]
            break
        else:
            print("Invalid selection. Try again.")

    nseat = int(input("\nEnter number of seats to book: "))

    print("\nChoose seat type:")
    print("\n1. Diamond - $25")
    print("2. Premium - $20")
    print("3. Gold - $15")
    print("4. Regular - $10")

    seat_types = {
        "1": ("diamond", 25),
        "2": ("premium", 20),
        "3": ("gold", 15),
        "4": ("regular", 10)
    }

    while True:
        choice = input("\nSelect seat type (1–4): ")
        if choice in seat_types:
            seat, rate = seat_types[choice]
            break
        else:
            print("Invalid seat option. Try again.")

    total = rate * nseat

    print("\n" + "="*130)
    print(" BOOKING SUMMARY ".center(130, "="))
    print("="*130)
    print(f"Movie Name      : {moviename}")
    print(f"Theatre         : {theatrename}")
    print(f"Date of Show    : {date}")
    print(f"Show Time       : {time}")
    print(f"Seat Type       : {seat}")
    print(f"Number of Seats : {nseat}")
    print(f"Rate per Ticket : ${rate}")
    print(f"Total Amount    : ${total}")
    print("="*130)

    ans = input("\nDo you want to confirm your booking? (yes/no): ").strip().lower()

    if ans == "yes":
        status = "Booked"
        print("\nBooking confirmed. Confirmation email has been sent.\n")
    else:
        status = "Cancel"
        print("\nBooking cancelled.\n")

    Q = """INSERT INTO booking 
    (login_id, Name, phone_no, email_id, dateofshow, time, typeofseat, theatrename, no_of_tickets, amount_per_ticket, total, status, movie_name)
    VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
        rs[0], rs[2], rs[3], rs[4], date, time, seat, theatrename, nseat, rate, total, status, moviename
    )

    mycursor.execute(Q)
    mycon.commit()
    mycon.close()
    print("-" * 130)


#------------------------------------------------------------VIEW-BOOKING---------------------------------------------------------------------------
def viewbooking(rs):
    mycon=msc.connect(host="localhost",user="root", password="prabhleen",database="project",auth_plugin="mysql_native_password")
    mycursor=mycon.cursor()
    Q="Select * from booking where login_id='{}'".format(rs[0])
    mycursor.execute(Q)
    result=mycursor.fetchall()
    if result==[]:
        print("No booking found of the given login_id:",rs[0])
    else:
        print("\nYOUR BOOKING DETAILS ARE:")
        for row in result:
            print("\n" + "-" * 130)
            print(" BOOKING DETAILS ".center(130,"-"))
            print("-" * 130)
            print(f"Login ID        : {row[0]}")
            print(f"Name            : {row[1]}")
            print(f"Phone Number    : {row[2]}")
            print(f"Email ID        : {row[3]}")
            print(f"Date of Show    : {row[4]}")
            print(f"Time            : {row[5]}")
            print(f"Seat Type       : {row[6]}")
            print(f"Theatre         : {row[7]}")
            print(f"No. of Tickets  : {row[8]}")
            print(f"Price per Ticket: {row[9]}")
            print(f"Total Amount    : {row[10]}")
            print(f"Status          : {row[11]}")
            print(f"Movie Name      : {row[12]}")
            print("-" * 130)
#-----------------------------------------------------------LOGIN-----------------------------------------------------------------------------------   
def login():
    userid=input("\nENTER LOGIN ID : ")
    password=input("ENTER PASSWORD : ")
    mycon=msc.connect(host="localhost",user="root", password="prabhleen",database="project",auth_plugin="mysql_native_password")
    mycursor=mycon.cursor()
    mycursor.execute("select * from registration where login_id ='{}' and password = '{}'".format(userid,password))
    rs=mycursor.fetchone()
    if(rs==None ):
        print("\nYOU HAVE ENTERED INVALID LOGIN ID AND PASSWORD ")
        print("TRY AGAIN!")
    else:
        print("\nWELCOME ",rs[2]," FOR ONLINE TICKET BOOKING SYSTEM\n ")
        while(True):
            print("PRESS 1. TO UPDATE PROFILE ")
            print("PRESS 2. FOR NEW BOOKING ")
            print("PRESS 3. VIEW PAST BOOKING ")
            print("PRESS 4. LOGOUT ")
            choice=int(input("\nENTER YOUR CHOICE OUT OF 1 TO 4 : "))
            if(choice==1):
                update(rs)
            elif(choice==2):
                newbooking(rs)
            elif(choice==3):
                viewbooking(rs)
            elif(choice==4):
                print("THANK YOU FOR USING OUR APP ")
                print("YOU ARE SUCCESSFULLY LOGGED OUT:)")
                print("-" * 130)
                break
            else:
                print("WRONG CHOICE ENTERED! ")

    
        
#------------------------------------------------------------REGISTRATION---------------------------------------------------------------------
def registration():
    Name=input("ENTER FIRST NAME : ")
    while(True):
        phoneno=input("ENTER PHONE NUMBER : ")
        if(len(phoneno)==10):
            break
        else:
            print("YOU HAVE ENTERED INVALID PHONE NUMBER!!TRY AGAIN ")
        
    while(True):
        Emailid=input("ENTER EMAIL ID : ")
        if("@" in Emailid):
            break
        else:
            print("PLEASE CHECK THE EMAIL ID THAT YOU HAVE ENTERED") 

    age=input("ENTER AGE : ")
    gender=input("ENTER GENDER OUT OF F/M : ")
    city=input("ENTER CITY : ")
    userid=input("ENTER USER ID : ")
    password=input("ENTER YOUR PASSWORD : ")
    while(True):
        retype=input("RETYPE YOUR PASSWORD : ")
        if(password==retype):
            print("\nPASSWORD MATCHED ")
            break
        else:
            print("RETYPED PASSWORD DOES NOT MATCH WITH PASSWORD ")
            print("TRY AGAIN ")
    
    mycon=msc.connect(host="localhost",user="root", password="prabhleen",database="project",auth_plugin="mysql_native_password")
    mycursor=mycon.cursor()
    mycursor.execute("insert into registration values('{}','{}','{}','{}','{}','{}','{}','{}')".format(userid,password,Name,phoneno,Emailid,age,gender,city))
    print("\nYou have registered successfully and confirmation mail has been sent to your email id",Emailid)
    mycon.commit()
    mycon.close()
    mycursor.close()
    input("\nPRESS ENTER KEY TO MAKE LOGIN ")
    login()
    

#-----------------------------------------------------------MAIN MENU --------------------------------------------------------------------------                    
print("=================================================WELCOME TO BOXOFFICE BUDDY====================================================")
while(True):
    print("\nHi there! Welcome to BoxOffice Buddy🎬")
    print("\nWe're glad you're here, Let's get you started!\n")
    print("=" * 130)
    print("\nPLEASE CHOOSE AN OPTION:\n")
    print("\nPRESS 1 FOR LOGIN ")
    print("\nPRESS 2 FOR REGISTRATION/NEW USER ")
    print("\nPRESS 3 FOR QUIT ")
    choice=int(input("\nENTER YOUR CHOICE : "))
    print("\n")
    print("=" * 130)
    if(choice==1):
        login()
    elif(choice==2):
        print("\nWELCOME HERE NOW PRESS ENTER PROCEED REGISTRATION")
        input()
        registration()
    elif(choice==3):
        break
    else:
        print("NOT A VALID CHOICE ENTERED")
