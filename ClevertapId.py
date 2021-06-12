import requests 
import mysql.connector
import json
from datetime import datetime, timezone


# Open database connection
#Enter the creds for prod dataset
db = mysql.connector.connect (host = "10.176.144.15",
                              user = "doctor_listing",
                              passwd = "I52kh7jC5MZkz2tGiB2p",
                              db = "doctor_listing",
                              port = 3306)

# prepare a cursor object using cursor() method
cursor = db.cursor()
API_ENDPOINT = "http://20.193.251.137/CreateClevertapId" #ENTER THE API

sql1 = "SELECT id,first_name,last_name, email_id, city_name, primary_contact_no, highest_degree FROM doctor_listing.doctor_profile where id=2"
print "1"
# Execute the SQL command
cursor.execute(sql1)
# Fetch all the rows in a list of lists.
results = cursor.fetchall()
for row in results:
  doctorId = row[0]
  firstName = row[1]
  lastName = row[2]
  emailId = row[3]
  cityName = row[4]
  contactNo = str(row[5])
  degree = row[6]

  sql2 = """SELECT doc_specialization_master_id FROM doctor_listing.doctor_specialization where doctor_id = %s"""
  cursor.execute(sql2,(doctorId,))
  temp = cursor.fetchall()
  doctorSpecializationId = temp[0][0]

  sql3 = """SELECT Speciality FROM  doctor_listing.doc_specialization_master where id=%s"""
  cursor.execute(sql3,(doctorSpecializationId,))
  resultsfinal = cursor.fetchall()

  data = {'emaidId':emailId, 'doctorName':firstName, 'location':cityName, 'doctorContactNo':contactNo, 'specialization':resultsfinal[0][0], 'degree':degree}
  app_json = json.dumps(data)
  headers={'Content-type':'application/json'}
  print '2'
  try:
    r = requests.post(url = API_ENDPOINT, data = app_json, headers=headers) 
  except:
    print ("Error for this Val")
  print ("Request Received")
  print(r.text)
  sql4 = "UPDATE doctor_listing.doctor_profile SET clever_tap_id = %s WHERE id = %s"
  val = (r.text, doctorId)
  cursor.execute(sql4, val)
  
  dt = datetime.datetime.now() 
  utc_time = dt.replace(tzinfo = timezone.utc())
  utc_timestamp = utc_time.timestamp() 
  sql5 = "UPDATE doctor_listing.doctor_profile SET modified_date = %s WHERE id = %s"
  val = (utc_timestamp, doctorId)
  cursor.execute(sql5, val)
try:
# Execute the SQL command
# Commit your changes in the database
  db.commit()
except:
# Rollback in case there is any error
  db.rollback()

# disconnect from server
db.close()

