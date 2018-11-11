import copy

from oopd.project.doctor import doctor
from oopd.project.department import department
from oopd.project.hospital import hospital
from oopd.project.patient import patient
from oopd.project.person import person
from oopd.project.HOD import HOD
from oopd.project.employee import employee
from oopd.project.admin import admin

cursor=shs.cursor()





while (1):

    print("Enter\n1.New patient registration:")
    print("\n2.Doctor login")
    print("\n3.Old patient login")
    print("\n4.Admin login")
    try:
        x = int(input())
        if (x == 1):
            patient_name = input("Enter name:")
            patient_gender=input("Enter gender:")
            patient_age=int(input("Enter age:"))
            patient_contact=int(input("Enter your contact number:"))
            patient_mail_id=input("Enter mail id: ")
            patient_blood=input("Enter Blood Group:")
            patient_password = input("Enter password:")
            patient_address=input("Enter Address separated by ; : ")
            patient_type=input("Enter type of admission as OPD or Local: ")
            patient_sickness=int(input("Enter Sickness:\n1. Eye Related\n2. Stomach Related\n3. Lung Related\n4. Tumor Related\n5. Heart Related\n6. General physician\n7. Ortho "))
            if patient_sickness==1:
                patient_id="EYE"+str(patient_contact)
            elif patient_sickness==2:
                patient_id="STO"+str(patient_contact)
            elif patient_sickness==3:
                patient_id="LNG"+str(patient_contact)
            elif patient_sickness==4:
                patient_id="TMR"+str(patient_contact)
            elif patient_sickness==5:
                patient_id="HRT"+str(patient_contact)
            elif patient_sickness==6:
                patient_id="GEN"+str(patient_contact)
            elif patient_sickness==7:
                patient_id="ORT"+str(patient_contact)
            print("Please note your ID:"+patient_id)
            patient_obj= patient()
            patient_obj.setpatient(patient_name,patient_contact,patient_address,patient_mail_id,patient_age,patient_gender,patient_type,patient_blood,patient_id,patient_password)

        elif (x == 2):
            doctor_id = input("Enter your ID:")
            doctor_password = input("Enter password:")
            doctor_object=doctor()
            doctorlogincheck=doctor_object.login_check(doctor_id,doctor_password)
            if(doctorlogincheck== True)








            else:
                print("please enter correct details")


        elif (x == 3):
            patient_old_id = input("Enter ID:")
            patient_old_password = input("Enter password:")
            patient_old_object = patient()
            patient_old_object.login_check(patient_old_id, patient_old_password)
            pat_opt=int(input("Enter:\n1. To edit profile\n2. To view doctor's profile"))

            if pat_opt==1:
                patient_old_object.updatedetails(patient_old_id)

            elif pat_opt==2:
                pat_choice=int(input("Enter search criteria:\n1. Doctors id\n2. Doctors name\n3. Specialization"))
                if pat_choice==1:
                    while 1:
                        doc_id=input("Enter id:")
                        cursor.execute("SELECT * FROM doctor WHERE id_no=" + doc_id)
                        row = cursor.fetchone()
                        shs.commit()

                        if row is not None:
                            print("Doctor details are:\n")
                            cursor.execute("SELECT * FROM doctor WHERE id_no=" + doc_id)
                            shs.commit()
                            break
                        else:
                            print("Enter valid ID number")

                elif pat_choice==2:
                    while 1:
                        doc_name=input("Enter name:")
                        cursor.execute("SELECT * FROM doctor WHERE name=" + doc_name)
                        row = cursor.fetchone()
                        shs.commit()
                        if row is not None:
                            print("Doctor details are:\n")
                            cursor.execute("SELECT * FROM doctor WHERE name=" + doc_name)
                            shs.commit()
                            break
                        else:
                            print("Enter valid name")

                elif pat_choice==3:
                    while 1:
                        doc_spec=input("Enter specialization:")
                        cursor.execute("SELECT * FROM doctor WHERE specialization=" + doc_spec)
                        row = cursor.fetchone()
                        shs.commit()
                        if row is not None:
                            print("Doctor details are:\n")
                            cursor.execute("SELECT * FROM doctor WHERE specialization=" + doc_spec)
                            shs.commit()
                            break
                        else:
                            print("Enter valid specialization")


        elif (x == 4):
            admin_id= input("Enter your ID:")
            admin_password = input("Enter password:")
            admin_object=admin()
            admin_object.login_check(admin_id,admin_password)
            operation=int(input("Enter: \n1. To add new doctor\n2. To remove a doctor\n3. To view List of doctors\n4. To view patients"))

            if operation==1:
                doc_name=input("Enter the Doctor's name:")
                doc_spec=input("Enter Specialization:")
                doc_contact=int(input("Enter Contact number:"))
                doc_address=input("Enter address separated by ;")
                doc_mail=input("Enter mail id:")
                doc_age=int(input("Enter age:"))
                doc_gender=input("Enter Gender:")
                doc_exp=int(input("Enter experience in years:"))
                doc_type=input("Enter the doctor type:")
                admin_object.setdoctor(doc_name.doc_spec,doc_contact,doc_address,doc_mail,doc_age,doc_gender,doc_exp,doc_type)
            elif operation==2:
                cursor.execute("SELECT * FROM doctor")
                shs.commit()
                doc_delete=input("Enter doctor ID to delete:")
                cursor.execute("SELECT * FROM doctor WHERE contact="+doc_delete)
                row=cursor.fetchone()
                while 1:
                    if row is not None:
                        cursor.execute("DELETE FROM doctor WHERE contact="+doc_delete)
                        shs.commit()
                        print("Successfully deleted")
                        break
                    else:
                        print("Record not in database.so can not delete")


            elif operation==3:
                doc_view=input("Enter doctor id:")
                admin_object.getdoctor(doc_view)

            elif operation==4:
                pat_view=input("Enter patient id:")
                admin_object.getpatient(pat_view)








    except Exception as e:
        print('exception occured',e)