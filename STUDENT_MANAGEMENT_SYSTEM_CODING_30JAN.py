print("PYTHON PROJECT :-")
print()
print("<<<<<<<<<'STUDENT MANAGEMENT SYSTEM'>>>>>>>>>>")
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
print("You can perform the following functions:-")
print("a. Enter 1 for ENTERING THE RECORDS.")
print("b. Enter 2 for DISPLAYING ALL THE RECORDS.")
print("c. Enter 3 for SERACHING THE RECORDS.")
print("d. Enter 4 for UPDATING THE RECORDS.")
print("e. Enter 5 for DELETING A RECORD.")
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
print("\n")
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
print("****NOTE:-Records here are saved in the database 'PYTHON_PROJECTZ' in MySQL****")
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")

import mysql.connector as a

pas=input("ENTER THE PASSWORD : ")


def stud_database_create():
    con=a.connect(host="localhost", user="root", password=pas)
    cur=con.cursor()
    query="create database PYTHON_PROJECTZ"
    cur.execute(query)
    con.commit()

def stud_table_create():
    con=a.connect(host="localhost", user="root", password=pas,database="PYTHON_PROJECTZ")
    cur=con.cursor()
    cur.execute("Create table Student_Management_System(Admission_No integer(5) primary key,\
            Roll_No integer(8), Student_Name varchar(20), Father_Name varchar(20),\
                Mother_Name varchar(20), D0B date, Class varchar(4), Stream varchar(14),\
                    Additional_Subject varchar(12), Fees float, Club_or_House varchar(13),\
                        Gender varchar(10), Caste varchar(15), Category varchar(8),\
                            BMI varchar(5), Blood_Group varchar(5), Address varchar(22),\
                                Aadhar_Card varchar(12), Email_Address varchar(30),\
                                    Phone_No varchar(10))")
    con.commit()
    
    if con.is_connected():
        print("Connection Established Successfully")
    else:
        print("Connection failed!!!!")
        print("Please Try Again.")
            
def stud_insert():
    while True:
        adm=int(input("ENTER ADMISSION NO. : "))
        r=int(input("ENTER ROLL NO. : "))
        n=input("ENTER STUDENT'S NAME : ")
        f=input("ENTER FATHER'S NAME : ")
        m=input("ENTER MOTHER'S NAME : ")
        d=input("ENTER STUDENT'S DATE OF BIRTH(YYYY-MM-DD) : ")
        c=input("ENTER CLASS : ")
        s=input("ENTER STREAM : ")
        ads=input("ENTER ADDITIONAL SUBJECT : ")
        fe=float(input("ENTER FEES : "))
        h=input("ENTER STUDENT'S HOUSE/CLUB : ")
        g=input("ENTER STUDENT'S GENDER : ")
        caste=input("ENTER STUDENT'S CASTE : ")
        ca=input("ENTER STUDENT'S CATEGORY : ")
        bmi=input("ENTER STUDENT'S BMI(BODY MASS INDEX) : ")
        blg=input("ENTER STUDENT'S BLOOD GROUP : ")
        add=input("ENTER STUDENT'S ADDRESS : ")
        ac=input("ENTER STUDENT'S AADHAR CARD NO. : ")
        e=input("ENTER STUDENT'S EMAIL ADDRESS : ")
        p=input("ENTER PHONE NO. : ")
        con=a.connect(host="localhost", user="root", password=pas, database="PYTHON_PROJECTZ")
        cur=con.cursor()
        
        query="Insert into Student_Management_System values({},{},'{}','{}','{}','{}',\
            '{}','{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}','{}',\
                '{}')".format(adm,r,n,f,m,d,c,s,ads,fe,h,g,caste,ca,bmi,blg,add,ac,e,p)
        cur.execute(query)
        con.commit()
        
        print("Records inserted successfully")
        
        print("\n")
        print("Do you want to continue?")
        print("--------------------------------------------------------------")
        print("****Enter any letter/number/symbol to continue****")
        print("****Enter 'no' to stop****")
        print("--------------------------------------------------------------")
        ch=input("Enter here : ")
        if ch=="no":
            break

def stud_display():
    print("-"*130)
    con=a.connect(host="localhost", user="root", password=pas,database="PYTHON_PROJECTZ")
    cur=con.cursor()
    query1="select *from Student_Management_System"
    cur.execute(query1)
    data1=cur.fetchall()
    for i in data1:
        print(i)
    print("Total No. of Records : ",cur.rowcount)
    print("-"*130)
    
    
def stud_search_adm():
    print("-"*80)
    con=a.connect(host="localhost", user="root", password=pas,database="PYTHON_PROJECTZ")
    cur=con.cursor()
    adm=int(input("Enter the Admission No : "))
    query2="select *from Student_Management_System where Admission_No={}".format(adm)
    cur.execute(query2)
    data2=cur.fetchall()
    for i in data2:
        print(i)
    print("Total no. of records displayed : ",cur.rowcount)
    print("-"*80)
    
def stud_search_rno():
    print("-"*80)
    con=a.connect(host="localhost", user="root", password=pas,database="PYTHON_PROJECTZ")
    cur=con.cursor()
    rno=int(input("Enter the Roll No. : "))
    query3="select *from Student_Management_System where Roll_No={}".format(rno)
    cur.execute(query3)
    data3=cur.fetchall()
    for i in data3:
        print(i)
    print("Total no. of records displayed :",cur.rowcount)
    print("-"*80)
    
def stud_search_class():
    print("-"*80)
    con=a.connect(host="localhost", user="root", password=pas,database="PYTHON_PROJECTZ")
    cur=con.cursor()
    clas=input("Enter Class : ")
    query4="select *from Student_Management_System where Class='{}'".format(clas)
    cur.execute(query4)
    data4=cur.fetchall()
    for i in data4:
        print(i)
    print("Total no. of records displayed : ",cur.rowcount)
    print("-"*80)

def stud_search_fees_greater():
    print("-"*80)
    con=a.connect(host="localhost", user="root", password=pas,database="PYTHON_PROJECTZ")
    cur=con.cursor()
    fee1=float(input("Enter Fees : "))
    query5="select Admission_No, Roll_No, Student_Name, Class, Fees, Address, Phone_No \
        from Student_Management_System where Fees>{}".format(fee1)
    cur.execute(query5)
    data5=cur.fetchall()
    for i in data5:
        print(i)
    print("Total no. of records displayed : ",cur.rowcount)
    print("-"*80)
    
def stud_search_fees_smaller():
    print("-"*80)
    con=a.connect(host="localhost", user="root", password=pas,database="PYTHON_PROJECTZ")
    cur=con.cursor()
    fee2=float(input("Enter Fees : "))
    query6="select Admission_No, Roll_No, Student_Name, Class, Fees, Address, Phone_No \
        from Student_Management_System where Fees<{}".format(fee2)
    cur.execute(query6)
    data6=cur.fetchall()
    for i in data6:
        print(i)
    print("Total no. of records displayed : ",cur.rowcount)
    print("-"*80)

def stud_search_fees():
    print("-"*80)
    con=a.connect(host="localhost", user="root", password=pas,database="PYTHON_PROJECTZ")
    cur=con.cursor()
    fee3=float(input("Enter Fees : "))
    query7="select Admission_No, Roll_No, Student_Name, Class, Fees, Address, Phone_No \
        from Student_Management_System where Fees={}".format(fee3)
    cur.execute(query7)
    data7=cur.fetchall()
    for i in data7:
        print(i)
    print("Total no. of records displayed : ",cur.rowcount)
    print("-"*80)

def stud_delete():
    print("-"*80)
    con=a.connect(host="localhost", user="root", password=pas,database="PYTHON_PROJECTZ")
    cur=con.cursor()
    adm2=int(input("Enter the Admission No. of the Student: "))
    query8="Delete from Student_Management_System where Admission_No={}".format(adm2)
    cur.execute(query8)
    print("Record deleted successfully.")
    print("-"*80)
    con.commit()
    
def stud_update():
    adm3=int(input("Enter the Admission No. to be searched : "))
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")
    print("PLEASE GO THROUGH THE FOLLOWING GUIDELINES.\n")
    print("1 for ROLL NO.")
    print("2 for STUDENT'S NAME")
    print("3 for FATHER'S NAME")
    print("4 for MOTHER'S NAME : ")
    print("5 for STUDENT'S DATE OF BIRTH(YYYY-MM-DD)")
    print("6 for CLASS")
    print("7 for STREAM")
    print("8 for ADDITIONAL SUBJECT")
    print("9 for FEES")
    print("10 for STUDENT'S HOUSE")
    print("11 for STUDENT'S GENDER")
    print("12 for STUDENT'S CASTE")
    print("13 for STUDENT'S CATEGORY")
    print("14 for STUDENT'S BMI(BODY MASS INDEX)")
    print("15 for STUDENT'S BLOOD GROUP")
    print("16 for STUDENT'S ADDRESS : ")
    print("17 for STUDENT'S AADHAR CARD NO.")
    print("18 for STUDENT'S EMAIL ADDRESS")
    print("19 for STUDENT'S PHONE NO.")
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")
    con=a.connect(host="localhost", user="root", password=pas,database="PYTHON_PROJECTZ")
    cur=con.cursor()
    #update
    choice=int(input("ENTER YOUR CHOICE : "))
    if choice==1:
        print("-"*80)
        rno=int(input("Enter New Roll No. : "))
        query="Update Student_Management_System set Roll_No={} where Admission_No={}".format(rno,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==2:
        print("-"*80)
        sname=input("Enter New Name : ")
        query="Update Student_Management_System set Student_Name='{}' where Admission_No={}".format(sname,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==3:
        print("-"*80)
        fname=input("Enter New Name : ")
        query="Update Student_Management_System set Father_Name='{}' where Admission_No={}".format(fname,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==4:
        print("-"*80)
        mname=input("Enter New Name : ")
        query="Update Student_Management_System set Mother_Name='{}' where Admission_No={}".format(mname,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==5:
        print("-"*80)
        dob=input("Enter New D.O.B.(YYYY-MM-DD) : ")
        query="Update Student_Management_System set D0B='{}' where Admission_No={}".format(dob,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==6:
        print("-"*80)
        clas=input("Enter New Class : ")
        query="Update Student_Management_System set Class='{}' where Admission_No={}".format(clas,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==7:
        print("-"*80)
        stm=input("Enter New Stream : ")
        query="Update Student_Management_System set Stream='{}' where Admission_No={}".format(stm,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==8:
        print("-"*80)
        ads=input("Enter New Additional Subject : ")
        query="Update Student_Management_System set Additional_Subject='{}' where Admission_No={}".format(ads,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==9:
        print("-"*80)
        fe=float(input("Enter Fees : "))
        query="Update Student_Management_System set Fees={} where Admission_No={}".format(fe,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==10:
        print("-"*80)
        club=input("Enter New House/Club : ")
        query="Update Student_Management_System set Club_or_House='{}' where Admission_No={}".format(club,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==11:
        print("-"*80)
        gdr=input("Enter New Gender : ")
        query="Update Student_Management_System set Gender='{}' where Admission_No={}".format(gdr,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==12:
        print("-"*80)
        cst=input("Enter Caste : ")
        query="Update Student_Management_System set Caste='{}' where Admission_No={}".format(cst,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==13:
        print("-"*80)
        ctg=input("Enter Category : ")
        query="Update Student_Management_System set Category='{}' where Admission_No={}".format(ctg,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==14:
        print("-"*80)
        bmi=input("Enter New BMI : ")
        query="Update Student_Management_System set BMI='{}' where Admission_No={}".format(bmi,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==15:
        print("-"*80)
        bg=input("Enter New Blood Group : ")
        query="Update Student_Management_System set Blood_Group='{}' where Admission_No={}".format(bg,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==16:
        print("-"*80)
        adr=input("Enter New Address : ")
        query="Update Student_Management_System set Address='{}' where Admission_No={}".format(adr,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==17:
        print("-"*80)
        adc=input("Enter New Aadhar Card No. : ")
        query="Update Student_Management_System set Aadhar_Card='{}' where Admission_No={}".format(adc,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==18:
        print("-"*80)
        email=input("Enter new Email Address : ")
        query="Update Student_Management_System set Email_Address='{}' where Admission_No={}".format(email,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)
    elif choice==19:
        print("-"*80)
        pno=input("Enter New Phone No. : ")
        query="Update Student_Management_System set Phone_No='{}' where Admission_No={}".format(pno,adm3)
        cur.execute(query)
        con.commit()
        print("Record updated successfully.")
        print("-"*80)
        print("Record after updation :- ")
        cur.execute("select *from Student_Management_System where Admission_No={}".format(adm3))
        data=cur.fetchall()
        for i in data:
            print(i)
        print("-"*80)

CHOICE="yes"
while CHOICE=="yes" or CHOICE=="YES" or CHOICE=="y":
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("You can perform the following functions:-")
    print("a. Enter 1 for ENTERING THE RECORDS.")
    print("b. Enter 2 for DISPLAYING ALL THE RECORDS.")
    print("c. Enter 3 for SERACHING THE RECORDS.")
    print("d. Enter 4 for UPDATING THE RECORDS.")
    print("e. Enter 5 for DELETING A RECORD.")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("\n")
    chi=input("ENTER YOUR CHOICE : ")
    if chi=="1":
        stud_insert()
    elif chi=="2":
        stud_display()
    elif chi=="3":
        print("YOU CAN SEARCH VIA THE GIVEN PARAMETERS :- ")
        print("a. Enter '10' for searching via Admission No.")
        print("b. Enter '11' for searching via Roll No.")
        print("c. Enter '12' for searching via Class.")
        print("d. Enter '14' for seaching via Fees.")
        chi_s=input("Enter your choice : ")
        if chi_s=="10":
            stud_search_adm()
        elif chi_s=="11":
            stud_search_rno()
        elif chi_s=="12":
            stud_search_class()
        elif chi_s=="14":
            print("YOU CAN SEARCH BY THREE WAYS VIA FEES.")
            print("a. Enter '20' for searching those records having fees less than given value.")
            print("b. Enter '21' for searching those records having fees greater than given value.")
            print("c. Enter '22' for searching those records having fees equal to given value")
            chi_s1=input("Enter you choice : ")
            if chi_s1=="20":
                stud_search_fees_smaller()
            elif chi_s1=="21":
                stud_search_fees_greater()
            elif chi_s1=="22":
                stud_search_fees()
    elif chi=="4":
        stud_update()
    elif chi=="5":
        stud_delete()
    elif chi=="9999":
        stud_database_create()
        stud_table_create()
    print("\n")
    print("DO YOU WANT TO PERFORM MORE FUNCTIONS?")
    print("-------------------------------------------------------------------")
    print("-------------------------------------------------------------------")
    print("****Enter 'yes' to continue****")
    print("****Enter 'no' to stop****")
    print("-------------------------------------------------------------------")
    print("-------------------------------------------------------------------")
    CHOICE=input("Enter your Choice (yes/no): ")
    


    
    
    



