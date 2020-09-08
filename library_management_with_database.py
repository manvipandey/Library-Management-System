import os,datetime,sys,mysql.connector
def addbook():
    conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
    cursor=conn.cursor()
    bname=input('ENTER BOOK NAME:')
    aname=input("ENTER AUTHOR's NAME:")
    cat=input('CATEGORY:')
    n=input("NO. OF COPIES:")
    str=("INSERT INTO book(book_name,author_name,category,copies)VALUES(%s,%s,%s,%s)")
    args=(bname,aname,cat,n)
    cursor.execute(str,args)
    conn.commit()
    print("\n\t\t\t\t\t\t\t\t\tBOOK ADDED SUCCESSFULLY!")
    cursor.close()
    conn.close()
def search():
    select=input("\n\t\t\t\t\t\t\t\t\t1.SEARCH BY BOOK TITLE\n\t\t\t\t\t\t\t\t\t2.SEARCH BY AUTHOR'S NAME\n\t\t\t\t\t\t\t\t\t3.SEARCH BY ID\n\t\t\t\t\t\t\t\t\t4.SEARCH BY CATEGORY\n\t\t\t\t\t\t\t\t\t5.VIEW ALL BOOKS\n\n\t\t\t\t\t\t\t\t\t>>PRESS ANY OTHER KEY TO EXIT\n\n>>ENTER YOUR CHOICE:")
    if select=="1":
        conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
        cursor=conn.cursor()
        bname=input("ENTER BOOK NAME:")
        cursor.execute("SELECT * FROM book WHERE book_name='{}'".format(bname))
        row=cursor.fetchone()
        if row is not None:
            print("\nBOOK DETAILS:-")
            print("\t\tBOOK ID : {}".format(row[0]))
            print("\t\tAUTHOR'S NAME : {}".format(row[2]))
            print("\t\tCATEGORY : {}".format(row[3]))
            print("\t\tCOPIES LEFT : {}".format(row[4]))
        else:
            print("n\t\t\t\t\t\t\t\t\t\tNO BOOK FOUND!")
        cursor.close()
        conn.close()
    elif select=="2":
        conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
        cursor=conn.cursor()
        aname=input("ENTER AUTHOR'S NAME:")
        cursor.execute("SELECT * FROM book WHERE author_name='{}'".format(aname))
        row=cursor.fetchall()
        if row is not None:
            print("FOLLOWING ARE THE BOOKS BY {}".format(aname))
            for books in row:
                print("\nBOOK DETAILS:-")
                print("\t\tBOOK ID : {}".format(books[0]))
                print("\t\tBOOK NAME : {}".format(books[1]))
                print("\t\tCATEGORY : {}".format(books[3]))
                print("\t\tCOPIES LEFT : {}".format(books[4]))
        else:
            print("n\t\t\t\t\t\t\t\t\t\tNO BOOK FOUND!")
        cursor.close()
        conn.close()
    elif select=="3":
        conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
        cursor=conn.cursor()
        i=input("ENTER BOOK ID:")
        cursor.execute("SELECT * FROM book WHERE id='{}'".format(i))
        row=cursor.fetchone()
        if row is not None:
            print("\nBOOK DETAILS:-")
            print("\t\tBOOK ID : {}".format(row[0]))
            print("\t\tBOOK NAME : {}".format(row[1]))
            print("\t\tAUTHOR'S NAME : {}".format(row[2]))
            print("\t\tCATEGORY : {}".format(row[3]))
            print("\t\tCOPIES LEFT : {}".format(row[4]))
        else:
            print("\n\t\t\t\t\t\t\t\t\t\tNO BOOK FOUND!")
        cursor.close()
        conn.close()
    elif select=="4":
        conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
        cursor=conn.cursor()
        cat=input("ENTER THE CATEGORY:")
        cursor.execute("SELECT * FROM book WHERE category='{}'".format(cat))
        row=cursor.fetchall()
        if row is not None:
            print("\nFOLLOWING ARE THE BOOKS UNDER {} CATEGORY:-".format(cat))
            for books in row:
                print("\nBOOK DETAILS:-")
                print("\t\tBOOK ID : {}".format(books[0]))
                print("\t\tBOOK NAME : {}".format(books[1]))
                print("\t\tAUTHOR'S NAME : {}".format(books[2]))
                print("\t\tCOPIES LEFT : {}".format(books[4]))
        else:
            print("\n\t\t\t\t\t\t\t\t\t\tNO BOOK FOUND!")
        cursor.close()
        conn.close()
    elif select=="5":
        conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM book")
        row=cursor.fetchall()
        print("\nFOLLOWING ARE THE BOOKS :-")
        for books in row:
            print("\nBOOK DETAILS:-")
            print("\t\tBOOK ID : {}".format(books[0]))
            print("\t\tBOOK NAME : {}".format(books[1]))
            print("\t\tAUTHOR'S NAME : {}".format(books[2]))
            print("\t\tCATEGORY : {}".format(books[3]))
            print("\t\tCOPIES LEFT : {}".format(books[4]))
        cursor.close()
        conn.close()
    else:
        print("\n\n\t\t\t\t\t\t\t\t\t\tWRONG CHOICE!")
    

def delbook():
    conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
    cursor=conn.cursor()
    name=input("ENTER YOUR NAME: ")
    cursor.execute("DELETE FROM book WHERE book_name='{}'".format(name))
    print("\n\t\t\t\t\t\t\tBOOK DELETED SUCCESSFULLY!".format(name))
    conn.commit()
    cursor.close()
    conn.close()

    
def addrec():
    print("ADD RECORD OF:-\n")
    s=input("\n\n\t\t\t\t1.EMPLOYEE\t\t\t\t\t\t\t\t\t2.STUDENT\n\n\t\t\t\t\t\t\t\t\t>>ENTER YOUR CHOICE:")
    if s=="1":
        conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
        cursor=conn.cursor()
        i=input("ENTER EMPLOYEE ID:")
        ename=input("ENTER EMPLOYEE'S NAME:")
        pst=input('POST:')
        phoneno=input('PHONE NO.:')
        str=("INSERT INTO emprec(id,ename,post,phoneno)VALUES(%s,%s,%s,%s)")
        args=(i,ename,pst,phoneno)
        cursor.execute(str,args)
        conn.commit()
        print("\n\n\t\t\t\t\t\t\t*************** EMPLOYEE IS ADDED!****************\n")
        cursor.close()
        conn.close()

    elif s=="2":
        conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
        cursor=conn.cursor()
        i=input("ENTER STUDENT ID:")
        sname=input("ENTER STUDENT'S NAME:")
        cls=input('CLASS:')
        phoneno=input('PHONE NO.:')
        str=("INSERT INTO sturec(id,sname,class,phoneno)VALUES(%s,%s,%s,%s)")
        args=(i,sname,cls,phoneno)
        cursor.execute(str,args)
        conn.commit()
        cursor.close()
        conn.close()
        print("\n\n\t\t\t\t\t\t\t*************** STUDENT IS ADDED!****************\n")
    else:
        print("\nWRONG CHOICE.TRY AGAIN!")
def delrec():
    print("DELETE RECORD OF:-")
    s=input("\n\n\t\t\t\t1.EMPLOYEE\t\t\t\t\t\t\t\t\t2.STUDENT\n\n\t\t\t\t\t\t\t\t\t>>ENTER YOUR CHOICE:")
    if s=="1":
        conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
        cursor=conn.cursor()
        i=input("ENTER YOUR ID: ")
        name=input("ENTER YOUR NAME: ")
        cursor.execute("DELETE FROM emprec WHERE id='{}' AND ename='{}'".format(i,name))
        print("\n\t\t\t\t\t\t\tRECORD OF {} IS DELETED SUCCESSFULLY!".format(name))
        conn.commit()
        cursor.close()
        conn.close()
    elif s=="2":
         conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
         cursor=conn.cursor()
         i=input("ENTER YOUR ID: ")
         name=input("ENTER YOUR NAME: ")
         cursor.execute("DELETE FROM sturec WHERE id='{}' AND sname='{}'".format(i,name))
         print("\n\t\t\t\t\t\t\tRECORD OF {} DELETED SUCCESSFULLY!".format(name))
         conn.commit()
         cursor.close()
         conn.close()
    else:
         print("\nWRONG CHOICE.TRY AGAIN!")
def issuebook():
    select=input("\n\t\t\t\t\t\t\t\t\t1.EMPLOYEE\n\t\t\t\t\t\t\t\t\t2.STUDENT\n\n\t\t\t\t\t\t\t\t\t>>ENTER YOUR CHOICE:")
    if select=="1":
        conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
        cursor=conn.cursor()
        i=input("ENTER YOUR ID:")
        aname=input("ENTER YOUR NAME:")
        cursor.execute("SELECT * FROM emprec WHERE ename='{}' AND id='{}'".format(aname,i))
        row=cursor.fetchone()
        if row is not None:
            if row[4]<5:
                n=row[4]
                bname=input("BOOK YOU WANT TO ISSUE:")
                cursor.execute("SELECT * FROM book WHERE book_name='{}'".format(bname))
                row=cursor.fetchone()
                if row is not None: 
                    if row[4]>0:
                        bid=row[0]
                        bn=row[4]
                        d,m,y=map(int,input("ENTER ISSUE DATE:").split("/"))
                        date=datetime.date(y,m,d)
                        str="INSERT INTO issueemp(eid,ename,bid,bname,idate) VALUES(%s,%s,%s,%s,%s)"
                        args=(i,aname,bid,bname,date)
                        cursor.execute(str,args)
                        cursor.execute("UPDATE book SET copies={} WHERE book.book_name='{}'".format(bn-1,bname))
                        cursor.execute("UPDATE emprec SET booksissued={} WHERE emprec.ename='{}'".format(n+1,aname))
                        print("\n\n\t\t\t\t\t\t\t\tBOOK ISSUED SUCCESSFULLY!")
                    else:
                        print("\n\n\t\t\t\t\t\t\t\tBOOK CURRENTLY UNAVAILABLE!")
                else:
                    print("\n\n\t\t\t\t\t\t\t\tBOOK NOT AVAILABLE!")
            else:
                print("\n\t\t\t\t\t\t\t\t\t\tNOT ELIGIBLE TO ISSUE ANY BOOK!")
        else:
            res=input("\n\n\t\t\t\t\t\t\t\tNO SUCH EMPLOYEE FOUND!Do you want to add this employee?(yes/no):")
            if res=="yes":
                addrec()
            else:
                pass
        conn.commit()
        cursor.close()
        conn.close()
    elif select=="2":
        conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
        cursor=conn.cursor()
        i=input("ENTER YOUR ID:")
        aname=input("ENTER YOUR NAME:")
        cursor.execute("SELECT * FROM sturec WHERE sname='{}' AND id='{}'".format(aname,i))
        row=cursor.fetchone()
        if row is not None:
            if row[4]<3:
                n=row[4]
                bname=input("BOOK YOU WANT TO ISSUE:")
                cursor.execute("SELECT * FROM book WHERE book_name='{}'".format(bname))
                row=cursor.fetchone()
                if row is not None: 
                    if row[4]>0:
                        bid=row[0]
                        bn=row[4]
                        d,m,y=map(int,input("ENTER ISSUE DATE:").split("/"))
                        date=datetime.date(y,m,d)
                        str="INSERT INTO issuestu(sid,sname,bid,bname,idate)VALUES(%s,%s,%s,%s,%s)"
                        args=(i,aname,bid,bname,date)
                        cursor.execute(str,args)
                        cursor.execute("UPDATE book SET copies={} WHERE book.book_name='{}'".format(bn-1,bname))
                        cursor.execute("UPDATE sturec SET booksissued={} WHERE sturec.sname='{}'".format(n+1,aname))
                        print("\n\n\t\t\t\t\t\t\t\tBOOK ISSUED SUCCESSFULLY!")
                    else:
                        print("\n\n\t\t\t\t\t\t\t\tBOOK CURRENTLY UNAVAILABLE!")
                else:
                    print("\n\n\t\t\t\t\t\t\t\tBOOK NOT AVAILABLE!")
            else:
                print("\n\t\t\t\t\t\t\t\t\t\tNOT ELIGIBLE TO ISSUE ANY BOOK!")
        else:
            res=input("\n\n\t\t\t\t\t\t\t\tNO SUCH STUDENT FOUND!Do you want to add this student?(yes/no):")
            if res=="yes":
                addrec()
            else:
                pass
        conn.commit()
        cursor.close()
        conn.close()

    else:
        print("\n\nWRONG CHOICE!")

def returnbook():
    select=input("\n\t\t\t\t\t\t\t\t\t1.EMPLOYEE\n\t\t\t\t\t\t\t\t\t2.STUDENT\n\n\t\t\t\t\t\t\t\t\t>>ENTER YOUR CHOICE:")
    if select=="1":
        conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
        cursor=conn.cursor()
        i=input("ENTER YOUR ID:")
        aname=input("ENTER YOUR NAME:")
        bname=input("ENTER BOOK NAME:")
        d,m,y=map(int,input("ENTER RETURN DATE(DD/MM/YYYY):").split("/"))
        rdate=datetime.date(y,m,d)
        cursor.execute("SELECT * FROM issueemp WHERE ename='{}' AND bname='{}'".format(aname,bname))
        row=cursor.fetchone()
        idate=row[4]
        cursor.execute("SELECT * FROM book WHERE book_name='{}'".format(bname))
        row=cursor.fetchone()
        c=row[4]+1
        cursor.execute("SELECT * FROM emprec WHERE ename='{}' AND id='{}'".format(aname,i))
        row=cursor.fetchone()
        bn=row[4]-1
        cursor.execute("UPDATE issueemp SET status='{}',rdate='{}' WHERE issueemp.ename='{}' AND issueemp.bname='{}'".format("RETURNED",rdate,aname,bname))
        cursor.execute("UPDATE book SET copies='{}' where book.book_name='{}'".format(c,bname))
        cursor.execute("UPDATE emprec SET booksissued='{}' WHERE emprec.ename='{}' AND emprec.id='{}'".format(bn,aname,i))
        print("\n\n\t\t\t\t\t\t\t\t\tBOOK RETURNED SUCCESSFULLY!")
        diff=abs(rdate.day-idate.day)
        if diff>20:
            print("\n\n\t\t\t\t\t\t\t\tISSUE PERIOD EXTENDED!FINE CHARGED OF RS",diff*30)
        conn.commit()
        cursor.close()
        conn.close()
    elif select=="2":
        conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
        cursor=conn.cursor()
        i=input("ENTER YOUR ID:")
        aname=input("ENTER YOUR NAME:")
        bname=input("ENTER BOOK NAME:")
        d,m,y=map(int,input("ENTER RETURN DATE(DD/MM/YYYY):").split("/"))
        rdate=datetime.date(y,m,d)
        cursor.execute("SELECT * FROM issuestu WHERE sname='{}' AND bname='{}'".format(aname,bname))
        row=cursor.fetchone()
        idate=row[4]
        cursor.execute("SELECT * FROM book WHERE book_name='{}'".format(bname))
        row=cursor.fetchone()
        c=row[4]+1
        cursor.execute("SELECT * FROM sturec WHERE sname='{}' AND id='{}'".format(aname,i))
        row=cursor.fetchone()
        bn=row[4]-1
        cursor.execute("UPDATE issuestu SET status='{}',rdate='{}' WHERE issuestu.sname='{}' AND issuestu.bname='{}'".format("RETURNED",rdate,aname,bname))
        cursor.execute("UPDATE book SET copies='{}' where book.book_name='{}'".format(c,bname))
        cursor.execute("UPDATE sturec SET booksissued='{}' WHERE sturec.sname='{}' AND sturec.id='{}'".format(bn,aname,i))
        print("\n\n\t\t\t\t\t\t\t\t\tBOOK RETURNED SUCCESSFULLY!")
        diff=abs(rdate.day-idate.day)
        if diff>10:
            print("\n\n\t\t\t\t\t\t\t\tISSUE PERIOD EXTENDED!FINE CHARGED OF RS",diff*30)
        conn.commit()
        cursor.close()
        conn.close()
    else:
        print("\n\n\t\t\t\t\t\t\tWRONG CHOICE !")
def view_sturec():
    conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
    cursor=conn.cursor()
    name=input("ENTER STUDENT'S NAME:")
    i=input("STUDENT ID:")
    cursor.execute("SELECT * FROM sturec WHERE id='{}' AND sname='{}'".format(i,name))
    row=cursor.fetchone()
    if row is not None:
        print("\n\tPERSONAL DETAILS:-")
        print("\n\t\t{:20}{:20}{:20}{:20}{:20}".format("STUDENT ID","STUDENT NAME","CLASS","PHONE NO.","BOOKS ISSUED"))
        print("\n\t\t{:20}{:20}{:20}{:20}{:20}".format(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4])))
        cursor.execute("SELECT * FROM issuestu WHERE sid='{}' AND sname='{}'".format(i,name))
        rows=cursor.fetchall()
        if rows is not None:
            print("\nALL ISSUE AND RETURN RECORDS OF {}:-".format(name))
            print("\n\t\t{:20}{:20}{:20}{:20}{:20}{:20}{:20}".format("STUDENT ID","STUDENT NAME","BOOK ID","BOOK NAME","ISSUE DATE","STATUS","RETURN DATE"))
            for rec in rows:
                a,b,c,d,e,f,g=rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6]
                if g==None:
                    print("\n\t\t{:20}{:20}{:20}{:20}{:20}{:20}{:20}".format(str(a),str(b),str(c),str(d),str(e),str(f),"---"))
                else:
                    print("\n\t\t{:20}{:20}{:20}{:20}{:20}{:20}{:20}".format(str(a),str(b),str(c),str(d),str(e),str(f),str(g)))
        else:
            print("\n\n\t\t\t\t\t\t\t\tNO LIBRARY RECORDS FOUND!")
    else:
        print("\n\n\t\t\t\t\t\t\t\t\t\tNO RECORD FOUND!")
    cursor.close()
    conn.close()
def view_emprec():
    conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
    cursor=conn.cursor()
    name=input("ENTER EMPLOYEE'S NAME:")
    i=input("EMPLOYEE ID:")
    cursor.execute("SELECT * FROM emprec WHERE id='{}' AND ename='{}'".format(i,name))
    row=cursor.fetchone()
    if row is not None:
        print("\n\tPERSONAL DETAILS:-")
        print("\n\t\t{:20}{:20}{:20}{:20}{:20}".format("EMPLOYEE ID","EMPLOYEE NAME","POST","PHONE NO.","BOOKS ISSUED"))
        print("\n\t\t{:20}{:20}{:20}{:20}{:20}".format(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4])))
        cursor.execute("SELECT * FROM issueemp WHERE eid='{}' AND ename='{}'".format(i,name))
        rows=cursor.fetchall()
        if rows is not None:
            print("\nALL ISSUE AND RETURN RECORDS OF {}:-".format(name))
            print("\n\t\t{:20}{:20}{:20}{:20}{:20}{:20}{:20}".format("EMPLOYEE ID","EMPLOYEE NAME","BOOK ID","BOOK NAME","ISSUE DATE","STATUS","RETURN DATE"))
            for rec in rows:
                a,b,c,d,e,f,g=rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6]
                if g==None:
                    print("\n\t\t{:20}{:20}{:20}{:20}{:20}{:20}{:20}".format(str(a),str(b),str(c),str(d),str(e),str(f),"---"))
                else:
                    print("\n\t\t{:20}{:20}{:20}{:20}{:20}{:20}{:20}".format(str(a),str(b),str(c),str(d),str(e),str(f),str(g)))
        else:
            print("\n\n\t\t\t\t\t\t\t\tNO LIBRARY RECORDS FOUND!")
    else:
        print("\n\n\t\t\t\t\t\t\t\t\t\tNO RECORD FOUND!")
    cursor.close()
    conn.close()

def issues_returns():
    select=input("\n\t\t\t\t\t\t\t\t\t1.ISSUES BY EMPLOYEES\n\t\t\t\t\t\t\t\t\t2.ISSUES BY STUDENTS\n\n\t\t\t\t\t\t\t\t\t>>ENTER YOUR CHOICE:")
    if select=="1":
        conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM issueemp")
        rows=cursor.fetchall()
        print("\nALL ISSUE AND RETURN RECORDS OF EMPLOYEES:-")
        print("\n\t\t{:20}{:20}{:20}{:20}{:20}{:20}{:20}".format("EMPLOYEE ID","EMPLOYEE NAME","BOOK ID","BOOK NAME","ISSUE DATE","STATUS","RETURN DATE"))
        for rec in rows:
            a,b,c,d,e,f,g=rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6]
            if g==None:
                print("\n\t\t{:20}{:20}{:20}{:20}{:20}{:20}{:20}".format(str(a),str(b),str(c),str(d),str(e),str(f),"---"))
            else:
                print("\n\t\t{:20}{:20}{:20}{:20}{:20}{:20}{:20}".format(str(a),str(b),str(c),str(d),str(e),str(f),str(g)))

        
    elif select=="2":
        conn=mysql.connector.connect(host="localhost",database="lib",user="root",passwd="")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM issuestu")
        rows=cursor.fetchall()
        print("\nALL ISSUE AND RETURN RECORDS OF STUDENTS:-")
        print("\n\t\t{:20}{:20}{:20}{:20}{:20}{:20}{:20}".format("STUDENT ID","STUDENT NAME","BOOK ID","BOOK NAME","ISSUE DATE","STATUS","RETURN DATE"))
        for rec in rows:
            a,b,c,d,e,f,g=rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6]
            if g==None:
                print("\n\t\t{:20}{:20}{:20}{:20}{:20}{:20}{:20}".format(str(a),str(b),str(c),str(d),str(e),str(f),"---"))
            else:
                print("\n\t\t{:20}{:20}{:20}{:20}{:20}{:20}{:20}".format(str(a),str(b),str(c),str(d),str(e),str(f),str(g)))
    else:
        print("\n\t\t\t\t\t\t\t\t\t\t\tWRONG CHOICE!")
        
print("****************************************************************************LIBRARY MANAGEMENT SYSTEM***********************************************************************\n\n")
while True:
    print("LOGIN AS:-\n\n")
    s=input("\n\n1.LIBRARIAN\t\t\t\t\t\t\t\t\t2.EMPLOYEE\t\t\t\t\t\t\t\t\t3.STUDENT\n\n\t\t\t\t\t\t\t\t\t4.PRESS ANY OTHER KEY TO EXIT\n\n >>ENTER YOUR CHOICE:")
    if s=="1":
        if input("\n\n\t\t\t\t\t\t\t\t\t\tENTER PASSWORD:")=="PYTHON":
            while True:
                select=input("\t\t\t\t\t\t\t\t\t1.ADD BOOK\n\t\t\t\t\t\t\t\t\t2.SEARCH\n\t\t\t\t\t\t\t\t\t3.ISSUE BOOK\n\t\t\t\t\t\t\t\t\t4.RETURN BOOK\n\t\t\t\t\t\t\t\t\t5.DELETE BOOK\n\t\t\t\t\t\t\t\t\t6.ADD RECORD\n\t\t\t\t\t\t\t\t\t7.DELETE RECORD\n\t\t\t\t\t\t\t\t\t8.VIEW EMPLOYEE RECORD\n\t\t\t\t\t\t\t\t\t9.VIEW STUDENT RECORD\n\t\t\t\t\t\t\t\t\t10.VIEW ISSUES AND RETURNS\n\t\t\t\t\t\t\t\t\t>>PRESS ANY OTHER KEY TO EXIT\nENTER YOUR CHOICE:")
                if select=="1":
                    addbook()
                elif select=="2":
                    search()
                elif select=="3":
                    issuebook()
                elif select=="4":
                    returnbook()
                elif select=="5":
                    delbook()
                elif select=="6":
                    addrec()
                elif select=="7":
                    delrec()
                elif select=="8":
                    view_emprec()
                elif select=="9":
                    view_sturec()
                elif select=="10":
                    issues_returns()
                else:
                    break
        else:
            print("\n\n\t\t\t\t\t\t\t\t\tYOU HAVE ENTERED A WRONG PASSWORD!")
            sys.exit()
    elif s=="2":
        while True:
            select=input("\n\n\t\t\t\t\t\t\t\t\t1.SEARCH\n\t\t\t\t\t\t\t\t\t2.VIEW YOUR LIBRARY RECORDS\n\t\t\t\t\t\t\t\t\t3.EXIT\n\t\t\t\t\t\t\t\t\t>>ENTER YOUR CHOICE:")
            if select=="1":
                search()
            elif select=="2":
                view_emprec()
            else:
                break
    elif s=="3":
        while True:
            select=input("\n\n\t\t\t\t\t\t\t\t\t1.SEARCH\n\t\t\t\t\t\t\t\t\t2.VIEW YOUR LIBRARY RECORDS\n\t\t\t\t\t\t\t\t\t3.EXIT\n\t\t\t\t\t\t\t\t\t>>ENTER YOUR CHOICE:")
            if select=="1":
                search()
            elif select=="2":
                view_sturec()
            else:
                break
    else:
        sys.exit()

