import mysql.connector as my

#########For Connecting to the Database###########################
db=my.connect(
                 host="127.0.0.1",     ## Local Host
                 user="root",           ## UserName
                 password="root",   ## Password
                 database="shs"        ##Database Name
               )

print(db)