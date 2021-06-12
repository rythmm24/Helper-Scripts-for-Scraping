import xlrd 
import requests 
import mysql.connector
import json
import xlwt
from xlutils.copy import copy

db = mysql.connector.connect (host = "10.176.144.15",
                              user = "doctor_listing",
                              passwd = "I52kh7jC5MZkz2tGiB2p",
                              db = "doctor_listing",
                              port = 3306)
cursor = db.cursor()
  
loc = ("Tele_4Nov.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)  
'''wb = copy(sheet) # a writable copy (I can't read values out of this, only write to it)
w_sheet = wb.get_sheet(0)
num_rows=sheet.nrows'''
for i in range(1, 3):
	print(sheet.row_values(i)[17])
	emailId = sheet.row_values(i)[17]

	sql1 = "SELECT id FROM doctor_listing.doctor_profile where email_id = %s"
	cursor.execute(sql1,(emailId,))
	docId = cursor.fetchall()

	if(len(docId)==1):
		print(docId[0][0])
		sql2 = "SELECT id FROM doctor_listing.doctor_supplier_mapping where doctor_id = %s";
		cursor.execute(sql2,(docId[0][0],))
		supId = cursor.fetchall()
		print(supId)

		if(len(supId)==1):
			print("Fees")
			sql3 = "SELECT original_fees FROM doctor_listing.doctor_supplier_mapping where doctor_id = %s"
			cursor.execute(sql3,(docId[0][0],))
			Fees = cursor.fetchall()
			print("Teleconsultation")

			sql4 = "SELECT Teleconsultation FROM doctor_listing.doctor_profile where id = %s"
			cursor.execute(sql4,(docId[0][0],))
			Tele = cursor.fetchall()

			print(Fees[0][0])
			print(Tele[0][0])
			print("\n")
		


'''


for i in range(1,2):
	doctorOpId = sheet.row_values(i)[3]
	emailId = sheet.row_values(i)[1]
	doctorName = sheet.row_values(i)[0]
	print(doctorOpId)
	print(emailId)

	sql1 = "SELECT id FROM doctor_listing.doctor_profile where SFDC_id2 = %s";
	cursor.execute(sql1,(doctorOpId,))
	docId = cursor.fetchall()
	print(docId[0][0])
    
    
	if(len(docId) != 1):
		sql2 = "SELECT id FROM doctor_listing.doctor_profile where email_id = %s";
		cursor.execute(sql2,(emailId,))
		docId = cursor.fetchall()	
		print(docId)

	if(len(docId)==1):
		sql3 = "SELECT id, original_fees, payee_id FROM doctor_listing.doctor_supplier_mapping where doctor_id = %s"
		cursor.execute(sql3,(docId[0][0],))
		temp= cursor.fetchall()
		print(temp[0][0])

		sql4 = "UPDATE doctor_listing.doctor_supplier_mapping SET isDOP = 1,isGOP= 1 WHERE id = %s"
		cursor.execute(sql4,(temp[0][0],))
		print("executed")
	
	else:
		print "ERROR"

	params = {'doctorMappingId':temp[0][0]}
	r = requests.post(url = API_ENDPOINT, params= params) 
	print(r.text)
	    

try:
# Execute the SQL command
# Commit your changes in the database
  db.commit()
except:
# Rollback in case there is any error
  db.rollback()

# disconnect from server
db.close()'''
