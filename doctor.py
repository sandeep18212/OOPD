class doctor:
    def __init__(self, doctorid=None,doctorname=None,doctoraddress=None,doctorcontact=None,doctordepartment=None,doctorofficetime=None):
        self.doctorid=doctorid
        self.doctorname = doctorname
        self.doctoraddress=doctoraddress
        self.doctorcontact=doctorcontact
        self.doctordepartment=doctordepartment
        self.doctorofficetime=doctorofficetime

    def login_check(self,doctor_id,doctor_password):
        flag=0
        while 1:
            sql="SELECT * FROM doctor where doctor_id="+ doctor_id + "and doctor_password="+ doctor_password
            a = cursor.execute(sql)
            row = cursor.fetchone()
            shs.commit()
            doctorlogincheck=False
            if row is not None:
                doctorlogincheck=True
                print("Login successful")
                return doctorlogincheck
            else:
                print("Wrong credentials, please enter again.")
                return doctorlogincheck
