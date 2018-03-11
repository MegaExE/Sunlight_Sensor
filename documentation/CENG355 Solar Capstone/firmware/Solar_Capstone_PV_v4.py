#Retrieving from PV1, PV2, PV4
#Working on retrieving from PV3
#Solar Capstone
#Johnson, Raphael & Adrian
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request
import threading #Loop
import time
from ctypes import c_short
from ctypes import c_byte
from ctypes import c_ubyte
from time import sleep
#Module for push data to firebase
import pyrebase

#Config for connecting to the Firebase
config = {
  "apiKey": "AIzaSyB_inMZruQbJUzueOSRqf0-zwbYoUnZqDA",
  "authDomain": "solar-capstone.firebaseapp.com",
  "databaseURL": "https://solar-capstone.firebaseio.com/",
  "storageBucket": "solar-capstone.appspot.com",
  #"serviceAccount": "path/to/serviceAccountKey.json"
}


#====================================================================================================
#Send the data to firebase database every 30 minutes.
#PV1
def SendtoFirebasePV1(db, Date, Power, Dailyyield, Totalyield):
  PV1 = {"Date": Date, "Power": Power, "Daily_yield": Dailyyield, "Total_yield": Totalyield}
  PV1_result = db.child("PV1").push(PV1)
  return;

#PV2
def SendtoFirebasePV2(db, Date, Power, Dailyyield, Totalyield):
  PV2 = {"Date": Date, "Power": Power, "Daily_yield": Dailyyield, "Total_yield": Totalyield}
  PV2_result = db.child("PV2").push(PV2)
  return;
  
#PV3  
  
#PV4
def SendtoFirebasePV4(db, Date, Power, Dailyyield, Totalyield):
  PV4 = {"Date": Date, "Power": Power, "Daily_yield": Dailyyield, "Total_yield": Totalyield}
  PV4_result = db.child("PV4").push(PV4)
  return;

#====================================================================================================
def GetAuthorized(firebase):
  auth = firebase.auth()
  return '';
  
#====================================================================================================
#This function execute every hour to retrieve data from all solar panels
def repeatEveryHourly():
	firebase = pyrebase.initialize_app(config)
	#runs the code every 30mins or replace the timer with 
	threading.Timer(1800.0, repeatEveryHourly).start()
	#grabs the current date and time
	currentTime = datetime.now()
	print(currentTime.strftime("\n%Y/%m/%d %I:%M %p\n"))
	date = currentTime.strftime("%Y/%m/%d %I:%M %p")
	
	
	#requesting to open this html for reading
	PV1 = urllib.request.urlopen("http://10.116.25.7/home.htm").read()
	PV2 = urllib.request.urlopen("http://10.116.25.5/production?locale=en").read()
	#PV3
	PV4 = urllib.request.urlopen("http://10.116.25.6/home.htm").read()
	

	#uses the BeautifulSoup function to process xml and html in Python.
	PV1_data = BeautifulSoup(PV1,'lxml')
	PV2_data = BeautifulSoup(PV2, 'lxml')
	PV4_data = BeautifulSoup(PV4, 'lxml')

	#used the find() function to find all html tags consisting with <table> with an id of "OvTb1"
	#PV1
	PV1_table = PV1_data.find('table', id="OvTbl") 
	PV1table_row = PV1_table.find_all('tr')
	#PV2
	PV2_table = PV2_data.find_all('table')
	#PV4
	PV4_table = PV4_data.find('table', id="OvTbl")
	PV4table_row = PV4_table.find_all('tr')

	#Global variables for string comparison
	power = "Power:"
	daily = "Daily yield:"
	total = "Total yield:"
	#PV2 global variables for string comparison	
	power_2 = "Currently"
	daily_2 = "Today"
	total_2 = "Since Installation"
	
	#Variables for PV1
	PV1_power = ""
	PV1_daily = ""
	PV1_total = ""
	#Variables for PV2
	PV2_daily = ""
	PV2_power = ""
	PV2_total = ""
	#Variables for PV4
	PV4_power = ""
	PV4_daily = ""
	PV4_total = ""
	
	#Display the info
	print("Solar Panel PV1")
	for tr in PV1table_row:
		td = tr.find_all('td')
		row = [i.string for i in td]
		print(row[0] + " " + row[1])
		if power == row[0]:
			PV1_power = row[1]
			#print(PV1_power)
		if daily == row[0]:
			PV1_daily = row[1]
			#print(PV1_daily)
		if total == row[0]:
			PV1_total = row[1]
			#print(PV1_total)
	
	print("\nSolar Panel PV2")
	for tr in PV2_table:
		td = tr.find_all('td')
		row = [i.text for i in td]
		#Testing
		#print("\n Row0: "+row[0]) 
		#print("\n Row1: "+row[1])
		#print("\n Row2: "+row[2])
		#print("\n Row3: "+row[3]) 
		#print("\n Row4: "+row[4])
		#print("\n Row5: "+row[5])
		#print("\n Row6: "+row[6])
		#print("\n Row7: "+row[7])
		#print("\n Row8: "+row[8])
		if power_2 == row[1]:
			PV2_power = row[2]
			print("Power:"+PV2_power)
		if daily_2 == row[3]:
			PV2_daily = row[4]
			print("Daily yield: "+PV2_daily)
		if total_2 == row[7]:
			PV2_total = row[8]
			print("Total yield:"+PV2_total)
	
	print("\nSolar Panel PV4")
	for tr in PV4table_row:
		td = tr.find_all('td')
		row = [i.text for i in td]
		print(row[0] + " " + row[1])
		if power == row[0]:
			PV4_power = row[1]
			#print(PV4_power)
		if daily == row[0]:
			PV4_daily = row[1]
			#print(PV4_daily)
		if total == row[0]:
			PV4_total = row[1]
			#print(PV4_total)
			
			
	#Calls to push the data to the firebase
	SendtoFirebasePV1( firebase.database(), date, PV1_power, PV1_daily, PV1_total)
	SendtoFirebasePV2( firebase.database(), date, PV2_power, PV2_daily, PV2_total)
	SendtoFirebasePV4( firebase.database(), date, PV4_power, PV4_daily, PV4_total)

#====================================================================================
#Main program
def main():		
	repeatEveryHourly()	
	return
	
if __name__ == "__main__":
	main()