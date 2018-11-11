class admin(employee):
    def __init__(self,salary=None):
        self.salary=salary

    def login_check(self,admin_id,admin_password):
        flag=0
        while 1:
            sql = "SELECT * FROM admin where admin_id=" + admin_id + "and admin_password=" + admin_password
            a = cursor.execute(sql)
            row = cursor.fetchone()
            shs.commit()
            if row is not None:
                print("Login successful")
            else:
                print("Wrong credentials, please enter again.")

    def setadmin(self):
        id="ADM"# +count no of admins and add the sum+1 to "ADM"
        password=id+#count generated from above
        #store id and password
        print(id)
        print("\n"+password)


    def getdoctor(self,id):
        cursor=shs.cursor()
        while 1:
                cursor.execute("SELECT * FROM doctor WHERE id_no="+id)
                row=cursor.fetchone()
                shs.commit()

                if row is not None:
                    print("Doctor details are:\n")
                    cursor.execute("SELECT * FROM doctor WHERE id_no="+id)
                    shs.commit()
                    break
                else:
                    print("Enter valid ID number")

    def getpatient(self,pat_id):
        cursor=shs.cursor()
        while 1:
                cursor.execute("SELECT * FROM patient WHERE id_no="+pat_id)
                row=cursor.fetchone()
                shs.commit()

                if row is not None:
                    print("Doctor details are:\n")
                    cursor.execute("SELECT * FROM doctor WHERE id_no="+pat_id)
                    shs.commit()
                    break
                else:
                    print("Enter valid ID number")