cursor=shs.cursor()

class person:
    def __init__(self, personname=None,personage=None,persongender=None,personcontact=None):
        self.personname = personname
        self.personage=personage
        self.persongender=persongender
        self.personcontact=personcontact
        self.personpassword=personpassword



    def setdoctor(self,name,specialization,contact,address,mail_id,age,gender,experience,type):
        cursor=shs.cursor()
        id_no=contact
        password=input("Enter password:")
        sql="INSERT INTO doctor VALUES(name,specialization,contact,address,mail_id,age,gender,experience,type,id_no,password)"
        cursor.execute(sql)
        shs.commit()

    def setpatient(self,name,contact,address,mail_id,age,gender,type,blood,patient_id,patient_password):
        cursor=shs.cursor()
        id_no=contact
        password=input("Enter password:")
        sql="INSERT INTO patient VALUES(name,specialization,contact,address,mail_id,age,gender,experience,type,blood,patient_id,patient_password)"
        cursor.execute(sql)
        shs.commit()
