class patient(person):
    def __init__(self,patientid=None,patientsickness=None,patientbloodgroup=None):
        self.patientid=patientid
        self.patientsickness=patientsickness
        self.patientbloodgroup=patientbloodgroup

    def updatedetails(self,id):
        choice=int(input("Enter:\n1. Update name\n2. Update contact\n3. Update address\n4.Update email-id\n5. Change password"))
        if choice==1:
            name=input("Enter new name:")
            sql="SELECT name FROM patient WHERE patient_id="+ id
            a=cursor.execute(sql)
            row=cursor.fetchone()
            shs.commit()
            if row is not None:
                sq="UPDATE patient SET name= %s where patient_id= %s"
                b=(name, id)
                cursor.execute(sq, b)
                shs.commit
            else:



        elif choice==2:
            contact=int(input("Enter new contact number:"))

        elif choice==3:
            address=input("Enter new address separated by ; :")

        elif choice==4:
            mail=input("Enter new email-id:")

        elif choice==5:
            password=input("Enter new password:")