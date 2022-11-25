import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="test1"
)

mycursor = mydb.cursor()

with open("/home/mhr/Downloads/fakeuser data/temp.csv","r") as f:

    i = 0
    for line in f:
        if i == 0:
            i+=1
            continue

        value = line.split(",")
        sql = "INSERT INTO user VALUES (%s, %s, %s, %s, %s)"
        val = (value[0], value[1],value[2],value[3],value[4])
        mycursor.execute(sql, val)

        if i % 10 ==0:
            mydb.commit()
        i +=1

mydb.commit()
mycursor.close()
mydb.close()
print(mycursor.rowcount, "record inserted.")
