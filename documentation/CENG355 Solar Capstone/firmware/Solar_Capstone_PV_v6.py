#Retrieving from PV1, PV2, PV4
#Working on retrieving from PV3
#Solar Capstone
#Johnson, Raphael & Adrian
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request
import threading #Loop
import calendar
import time
from ctypes import c_short
from ctypes import c_byte
from ctypes import c_ubyte
from time import sleep
#Module for push data to firebase
import pyrebase
import os

from apscheduler.schedulers.background import BackgroundScheduler

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
def SendtoFirebasePV1(db, Date, Epoch, Power, Dailyyield, Totalyield):
  PV1 = {"Date": Date,"Epoch": Epoch, "Power": Power, "Daily_yield": Dailyyield, "Total_yield": Totalyield}
  PV1_result = db.child("PV1").push(PV1)
  return;

#PV2
def SendtoFirebasePV2(db, Date, Epoch, Power, Dailyyield, Totalyield):
  PV2 = {"Date": Date, "Epoch": Epoch, "Power": Power, "Daily_yield": Dailyyield, "Total_yield": Totalyield}
  PV2_result = db.child("PV2").push(PV2)
  return;

#PV3

#PV4
def SendtoFirebasePV4(db, Date, Epoch, Power, Dailyyield, Totalyield):
  PV4 = {"Date": Date, "Epoch": Epoch, "Power": Power, "Daily_yield": Dailyyield, "Total_yield": Totalyield}
  PV4_result = db.child("PV4").push(PV4)
  return;

#====================================================================================================
def GetAuthorized(firebase):
  auth = firebase.auth()
  return '';

#====================================================================================================
def deletes():
    firebase = pyrebase.initialize_app(config)
    delete(firebase.database())

#Retrieving the epoch time from the PV's to check which log to be deleted
def delete(db):
    #Current epoch time
    print(calendar.timegm(time.gmtime()))
    currentepoch = calendar.timegm(time.gmtime())
    #Current time minus 30 days
    deleteepoch = currentepoch - 2592000
    print(deleteepoch)
	
	#PV1
    #Save 30 days of logs
    PV1 = db.child("PV1").order_by_child("Epoch").start_at(1).end_at(deleteepoch).get()
    #key = db.child("PV1").order_by_child("Epoch").start_at(f).end_at(e).get()
    #print(key.key())
    #print (results.val())
    print("PV1")
    for PV1data in PV1.each():
        print(PV1data.key())
        pv1id = PV1data.key()
        print(PV1data.val())
        db.child("PV1").child(pv1id).remove()
        #print(user)
       
    #PV2
    PV2 = db.child("PV2").order_by_child("Epoch").start_at(1).end_at(deleteepoch).get()
    print("PV2")
    for PV2data in PV2.each():
        print(PV2data.key())
        pv2id = PV2data.key()
        print(PV2data.val())
        db.child("PV2").child(pv2id).remove()
        #print(user)

	#PV3
    #PV3 = db.child("PV3").order_by_child("Epoch").start_at(1).end_at(deleteepoch).get()
    #print("PV3")
    #for PV3data in PV3.each():
        #print(PV3data.key())
        #pv3id = PV3data.key()
        #print(PV3data.val())
        #db.child("PV3").child(pv3id).remove()
        #print(user)
    
    #PV4    
    PV4 = db.child("PV4").order_by_child("Epoch").start_at(1).end_at(deleteepoch).get()
    print("PV4")
    for PV4data in PV4.each():
        print(PV4data.key())
        pv4id = PV4data.key()
        print(PV4data.val())
        db.child("PV4").child(pv4id).remove()
        #print(user)
#====================================================================================================
#This function execute every hour to retrieve data from all solar panels
def repeatEveryHourly():
	firebase = pyrebase.initialize_app(config)
	#runs the code every 30mins or replace the timer with 
	#to = threading.Timer(5.0, repeatEveryHourly)
	#to1 = threading.Timer(10.0, delete(firebase.database()))
	#to.start()
	#to1.start()
	#print(threading.Timer)
	
	#grabs the current date and time
	currentTime = datetime.now()
	print(currentTime.strftime("\n%Y/%m/%d %I:%M %p\n"))
	date = currentTime.strftime("%Y/%m/%d %I:%M %p")
	epoch = int(time.time())
	print("\nEpoch Time:" ,  epoch)
	
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
	SendtoFirebasePV1( firebase.database(), date, epoch, PV1_power, PV1_daily, PV1_total)
	SendtoFirebasePV2( firebase.database(), date, epoch, PV2_power, PV2_daily, PV2_total)
	SendtoFirebasePV4( firebase.database(), date, epoch, PV4_power, PV4_daily, PV4_total)
	
#====================================================================================
def killLogger():
    scheduler.shutdown()
    print ("Scheduler Shutdown....")
    exit()
    
#=====================================================================================    
#Main program
def main():
        scheduler = BackgroundScheduler()
        
        #Schedule every 30 minutes
        scheduler.add_job(repeatEveryHourly, 'interval', seconds=1800)
        #scheduler.add_job(repeatEveryHourly, 'interval', seconds=5)
        #scheduler the delete every 30 days
        scheduler.add_job(deletes, 'interval', seconds=2592000)
        
        scheduler.start()
        scheduler.print_jobs()
        
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

        try:
        	# This is here to simulate application activity (which keeps the main thread alive).
            while True:
                time.sleep(2)
        except (KeyboardInterrupt, SystemExit):
        	# Not strictly necessary if daemonic mode is enabled but should be done if possible
            scheduler.shutdown
        return

if __name__ == "__main__":
	main()

