import functions
import pandas as pd
from datetime import datetime
from IPython.display import display


lh = input("Enter Your LocalHost Name : ")
rn = input("Enter Your Root Name : ")
pw = input("Enter Your Password : ")
cource_name = input("Enter Cource Name : ")
cource_name = cource_name.capitalize()
connection = functions.create_server_connection(lh, rn, pw)


print("<--WELCOME TO SHYAM COMPUTER ACADEMY-->")
print("1. For Creating Database")
print("2. For Storing Details")
print("3. For Check Fee Status")
print("4. For Updating Details")
print("5. For Deleting Details")
print("6. For Check All Data in Database")


n = int(input("Select and Enter : "))
if n == 1:  # OK
    cn = input("Enter Student Name : ")
    cn = cn.lower()
    create_databse_query = f"Create database {cn}"
    functions.create_database(connection, create_databse_query)
    connection = functions.create_db_connection(lh, rn, pw, cn)
    ct = f"""
    create table {cn}(
    admn_no int,
    student_name varchar(30) not null,
    class varchar(3) not null,
    fee_paid int);"""
    functions.exe_query(connection, ct)
elif n == 2:  # OK
    n1 = int(input("Enter Number Of Students : "))
    for i in range(n1):
        sdt_nm = input("Enter Student Name : ")
        admn_no = int(input("Enter Admission Number : "))
        cls = input("Enter Class Of Student : ")
        fee = int(input("Enter Fee Paid  : "))
        data_store = f"""
        insert into {sdt_nm} values
        ({admn_no},"{sdt_nm}","{cls}","{fee}")
        """
    connection = functions.create_db_connection(lh, rn, pw, sdt_nm)
    functions.exe_query(connection, data_store)
elif n == 3:  # OK
    tf = int(input(f"Enter Total Fee of {cource_name} Cource : "))
    cn = input("Enter Student Name : ")
    q1 = f"""
    select fee_paid from {cn};
    """
    connection = functions.create_db_connection(lh, rn, pw, cn)
    results = functions.read_query(connection, q1)
    sum = 0
    for i in results:
        l = list(i)
        sum += l[0]
    rm = tf-sum
    if sum == tf:
        print("Total Fee Paid.")
    else:
        print(f"Remaining Fee Is ₹{rm}")
        print("It Is Requested To Student To Pay Fee As Soon As Possible.")
elif n == 4:  # NOT TESTED BUT OK
    print("['name','class']")
    s = input("Select And Enter : ")
    cn = input("Enter Student  Name : ")
    if s.lower() == "name":
        s1 = input("Enter New Name : ")
        n1 = int(input("Enter Admission Number : "))
        update = f"""
        update {cn}
        set student_name = {s1}
        where admn_no = {n1}"""
        functions.exe_query(connection, update)
    elif s.lower() == "class":
        s1 = input("Enter New Class : ")
        n1 = int(input("Enter Admission Number : "))
        update = f"""
        update {cn}
        set class = {s1}
        where admn_no = {n1}"""
        functions.exe_query(connection, update)
    else:
        print("Select And Enter Form ['name','class']")
elif n == 5:  # OK
    print("Do You Want To Delete Database??")
    i = input("[Y/N]")
    if i in "Yy":
        cn = input("Enter Student Name : ")
        admn_no = int(input("Enter Admission Number : "))
        delete = f"""
        delete from {cn}
        where admn_no = {admn_no};"""
        try:
            connection = functions.create_db_connection(lh, rn, pw, cn)
            functions.exe_query(connection, delete)
            print("Sucessfully Deleted...")
        except:
            print("Deletion Unsucessfull...")
    else:
        pass
elif n == 6:  # OK
    try:
        lh = input("Enter Your LocalHost Name : ")
        rn = input("Enter Your Root Name : ")
        pw = input("Enter Your Password : ")
        connection = functions.create_server_connection(lh, rn, pw)
        print("Authicated Admin...Login Sucessfull...")
        v = 1
    except:
        v = 0
        print("Login Unsucessfull...")
    if v != 0:
        cn = input("Enter Student Name : ")
        q1 = f"""
        select * from {cn};
        """
        connection = functions.create_db_connection(lh, rn, pw, cn)
        results = functions.read_query(connection, q1)
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
        date_time = datetime.fromtimestamp(1887639468)
        content = f.write(
            f"Logged in at {date_time} \t For Creating Database\n")
    elif n == 2:
        date_time = datetime.fromtimestamp(1887639468)
        content = f.write(f"Logged in at {date_time} \t For Storing Details\n")
    elif n == 3:
        date_time = datetime.fromtimestamp(1887639468)
        content = f.write(
            f"Logged in at {date_time} \t For Check Fee Status\n")
    elif n == 4:
        date_time = datetime.fromtimestamp(1887639468)
        content = f.write(
            f"Logged in at {date_time} \t For Updating Details\n")
    elif n == 5:
        date_time = datetime.fromtimestamp(1887639468)
        content = f.write(
            f"Logged in at {date_time} \t For Deleting Details\n")
    elif n == 6:
        date_time = datetime.fromtimestamp(1887639468)
        content = f.write(
            f"Logged in at {date_time} \t  For Check All Data in Database\n")
    else:
        date_time = datetime.fromtimestamp(1887639468)
        content = f.write(f"\nLogged in at {date_time} \t Just Logged in...")





print(" >_< THANK YOU >_< ")