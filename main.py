import os
import datetime
import functions
import pandas as pd  # pip install pandas
from IPython.display import display  # pip install display


pw = input("Enter Server Password : ")
cource_name = (input("Enter Cource Name : ").capitalize())
connection = functions.create_server_connection(pw)
# Fee Structures:
if cource_name == "Python":
    tf = 10000
elif cource_name == "Java":
    tf = 10000
elif cource_name == "C/C++":
    tf = 9000
else:
    tf = None

print("\t\t\t\t\t<--WELCOME TO SHYAM COMPUTER ACADEMY-->\n\n")
while True:
    print("Enter 1. For Creating Student Data in Server")
    print("Enter 2. For Storing Student & Fee in Server")
    print("Enter 3. To Check Fee Status")
    print("Enter 4. For Updating Details")
    print("Enter 5. For Deleting Details")
    print("Enter 6. For Check All Data in Server")
    n = int(input("Select and Enter : "))

    if n == 1:  # OK
        os.system('color 6')
        student_name = (input("Enter Student Name : ").lower())
        create_databse_query = f"Create database {cource_name}"  # SQL CODE
        functions.create_database(
            connection, create_databse_query)  # FUNCTION CALL
        connection1 = functions.create_db_connection(
            pw, cource_name)  # FUNCTION CALL
        # SQL CODE
        ct = f"""
        create table {student_name}(
        admn_no int,
        student_name varchar(30) not null,
        class varchar(3) not null,
        fee_paid int);"""
        functions.exe_query(connection1, ct)  # function call
        print("SucessFully Created Database")

    elif n == 2:  # OK
        sn = input("Did You Created Student data in Database [Y/N] :\n")
        if sn in "Yy":
            sdt_nm = input("Enter Student Name : ").lower()
            admn_no = int(input("Enter Admission Number : "))
            cls = input("Enter Class Of Student : ")
            fee = int(input("Enter Fee Paid  : "))
            # SQL CODE
            use_db = f"use {cource_name}"
            data_store = f"""
            insert into {sdt_nm} values
            ({admn_no},"{sdt_nm}","{cls}","{fee}")
            """
            connection = functions.create_db_connection(pw, cource_name)
            functions.exe_query(connection, use_db)
            functions.exe_query(connection, data_store)
        elif sn in "Nn":
            print(
                "please use option 1.\nStep 1:First create Table using Option 1.\nStep 2: Then use option 2")
        else:
            print("Enter [Y/N]")
            pass

    elif n == 3:  # OK
        try:
            if tf != None:
                print(f"Total Fee of {cource_name} is ₹{tf}")
                student_name = input("Enter Student Name : ").lower()
                # SQL CODE
                use_db = f"use {cource_name}"
                q1 = f"""
                select fee_paid from {student_name};
                """

                connection = functions.create_db_connection(pw, cource_name)
                results = functions.exe_query(connection, use_db)
                results = functions.read_query(connection, q1)
                # CALCULATING FEE AMOUNT
                try:
                    sum = 0
                    for i in results:
                        l = list(i)
                        sum += l[0]
                    rm = tf-sum
                    if sum >= tf:
                        print("Total Fee Paid.")
                    else:
                        print(f"Remaining Fee Is ₹{rm}")
                        print(
                            "It Is Requested To Student To Pay Fee As Soon As Possible.")
                except:
                    print("Student Details Not Found")
                    pass
            else:
                print(f"Total Fee Of {cource_name} is not defined.")
        except:
            print("Please Create Data of Student In Database")
            pass

    elif n == 4:  # OK
        os.system('color 4')
        print("1.change student name\n2.change student class\n3.change student admission number")
        s = int(input("Select And Enter : "))
        student_name = input("Enter Student Name : ")
        student_name = student_name.lower()
        connection = functions.create_db_connection(pw, cource_name)
        if s == 1:
            new_student_name = input("Enter New Name of Student : ")
            admn_no = int(input("Enter Admission Number : "))
            # SQL CODE
            use_db = f"use {cource_name}"
            update = f"""
            update {student_name}
            set student_name = "{new_student_name}"
            where admn_no = {admn_no};"""
            functions.exe_query(connection, use_db)
            functions.exe_query(connection, update)
            print("Sucessfully Updated!")

        elif s == 2:
            s1 = input("Enter New Class : ")
            admn_no = int(input("Enter Admission Number : "))
            # SQL CODE
            use_db = f"use {cource_name}"
            update = f"""
            update {student_name}
            set class = {s1}
            where admn_no = {admn_no};"""
            functions.exe_query(connection, use_db)
            functions.exe_query(connection, update)
            os.system('color 2')
            print("Sucessfully Updated!")

        elif s == 3:
            admn_no = int(input("Enter Old Admission Number : "))
            new_admn_no = input("Enter New Admission Number : ")
            use_db = f"use {cource_name}"
            update = f"""
            update {student_name}
            set admn_no = {new_admn_no}
            where admn_no = {admn_no};"""
            print(
                f"Remember New Admission Number \nNew Admission Number is : {new_admn_no}")
            functions.exe_query(connection, use_db)
            functions.exe_query(connection, update)
            os.system('color 2')
            print("Sucessfully Updated!")

        else:
            print("Select And Enter Form name/class/admission number")

    elif n == 5:  # OK
        os.system('color 4')
        print("Warning!! \nThis deletes all data of student in server")
        i = input("[Y/N]")
        if i in "Yy":
            student_name = input("Enter Student Name : ")
            student_name = student_name.lower()
            use_db = f"use {cource_name}"
            delete = f"""drop table {student_name}"""
            try:
                connection = functions.create_db_connection(pw, cource_name)
                functions.exe_query(connection, use_db)
                functions.exe_query(connection, delete)
                os.system('color 2')
                print("Sucessfully Deleted...")
            except:
                print("Deletion Unsucessfull...")
        else:
            pass

    elif n == 6:  # OK
        os.system('color 6')
        try:
            pw = input("Enter Server Password Again : ")
            connection = functions.create_server_connection(pw)
            os.system('color 2')
            print("Authicated..Login Sucessfull...")
            v = 1
        except:
            v = 0
            print("Login Unsucessfull...")
        if v != 0:
            use_db = f"use {cource_name}"
            cn = input("Enter Student Name : ")
            q1 = f"""
            select * from {cn};
            """
            connection = functions.create_db_connection(pw, cource_name)
            results = functions.exe_query(connection, use_db)
            results = functions.read_query(connection, q1)
            os.system('color 2')
            db = []
            for rst in results:
                res = list(rst)
                db.append(res)
            columns = ["admn_no", "student_name", "class", "fee_paid"]
            df = pd.DataFrame(db, columns=columns)
            display(df)

    else:
        print("Please Select and Enter From [1/2/3/4/5/6]")

    with open("__pycache__/log.txt", "a") as f:
        if n == 1:
            date_time = datetime.datetime.now()
            content = f.write(
                f"Logged in at {date_time} \t For Creating Student data in Server\n")
        elif n == 2:
            date_time = datetime.datetime.now()
            content = f.write(
                f"Logged in at {date_time} \t For Storing Details in Server\n")
        elif n == 3:
            date_time = datetime.datetime.now()
            content = f.write(
                f"Logged in at {date_time} \t To Check Fee Status\n")
        elif n == 4:
            date_time = datetime.datetime.now()
            content = f.write(
                f"Logged in at {date_time} \t For Updating Details in Server\n")
        elif n == 5:
            date_time = datetime.datetime.now()
            content = f.write(
                f"Logged in at {date_time} \t For Deleting Details in Server\n")
        elif n == 6:
            date_time = datetime.datetime.now()
            content = f.write(
                f"Logged in at {date_time} \t  For Check All Data in Server\n")
        else:
            date_time = datetime.datetime.now()
            content = f.write(
                f"\nLogged in at {date_time} \t Just Logged in...")

        bk = input("Do You Want To Continue [Y/N]: ")
        if bk in "Nn":
            break

print(" >_< THANK YOU >_< ")
print(" © Copyright Content")
print("Developed By SCA")
