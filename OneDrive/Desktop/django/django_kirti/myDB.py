import pymysql

dataBase = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
)

#prepare a cursor object
cursorObject = dataBase.cursor()


#Create the database
cursorObject.execute("CREATE DATABASE myDBPy")

print("All done")