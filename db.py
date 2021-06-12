import os
import json
import mysql.connector

directory = r'/Users/tanmay/Desktop/medplusmart_dump'
j=0
db = mysql.connector.connect (host = "10.176.144.15",
                              user = "devmedstore",
                              passwd = "uapL6{9h?",
                              db = "dev",
                              port = 3306)

cursor = db.cursor(buffered=True)

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        filename = os.path.join(directory, filename)
        json_data=open(filename).read()
        json_obj = json.loads(json_data)
    try:
        for i in json_obj['data']:
            sql = "INSERT INTO dev.medplus_mart (product_name) VALUES (%s)"
            print(i)
            cursor.execute(sql,(i,))
    except: continue
    else:
        continue


try:
# Execute the SQL command
# Commit your changes in the database
  db.commit()
except:
# Rollback in case there is any error
  db.rollback()

# disconnect from server
db.close()


