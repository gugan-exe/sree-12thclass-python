import mysql.connector as mysql
mycon=mysql.connect(host="localhost",username="root",password="sreegugan",database="test_for_connection_of_mysql_to_python")
if mycon.is_connected():
    print("connected")
else:
    print("Try!Again")
hover=mycon.cursor()
print(hover.execute("SELECT * FROM "))
