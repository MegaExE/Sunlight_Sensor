#Retrieving from PV1, PV2, PV3, PV4
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
#PV3
import json


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

#PV3a
def SendtoFirebasePV3a(db, Date, Epoch, VACin, VACout, BatteryV):
  PV3a = {"Date": Date, "Epoch": Epoch, "VACin": VACin, "VACout": VACout, "BatteryVolt": BatteryV}
  PV3a_result = db.child("PV3a").push(PV3a)
  return;
  
#PV3b
def SendtoFirebasePV3b(db, Date, Epoch, Power, BatteryV, VACin):
  PV3b = {"Date": Date, "Epoch": Epoch, "Power": Power, "BatteryVoltage": BatteryV, "VACin": VACin}
  PV3b_result = db.child("PV3b").push(PV3b)
  return;

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

	#PV3a
    PV3a = db.child("PV3a").order_by_child("Epoch").start_at(1).end_at(deleteepoch).get()
    print("PV3a")
    for PV3adata in PV3a.each():
        print(PV3adata.key())
        pv3aid = PV3adata.key()
        print(PV3adata.val())
        db.child("PV3a").child(pv3aid).remove()
        #print(user)
	#PV3b
    PV3b = db.child("PV3b").order_by_child("Epoch").start_at(1).end_at(deleteepoch).get()
    print("PV3b")
    for PV3bdata in PV3b.each():
        print(PV3bdata.key())
        pv3bid = PV3bdata.key()
        print(PV3bdata.val())
        db.child("PV3b").child(pv3bid).remove()
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
	
	#Global variables for string comparison
	power = "Power:"
	daily = "Daily yield:"
	total = "Total yield:"
	
	try:
		#requesting to open this html for reading
		PV1 = urllib.request.urlopen("http://10.116.25.7/home.htm").read()
		
		#uses the BeautifulSoup function to process xml and html in Python.
		PV1_data = BeautifulSoup(PV1,'lxml')
		
		#used the find() function to find all html tags consisting with <table> with an id of "OvTb1"
		#PV1
		PV1_table = PV1_data.find('table', id="OvTbl") 
		PV1table_row = PV1_table.find_all('tr')
		
		#Variables for PV1
		PV1_power = ""
		PV1_daily = ""
		PV1_total = ""
		
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
		
		#Calls to push the data to the firebase
		SendtoFirebasePV1( firebase.database(), date, epoch, PV1_power, PV1_daily, PV1_total)		
	except urllib.error.URLError:
		print("Solar Panel PV1 is offline")
		SendtoFirebasePV1( firebase.database(), date, epoch, "0", "0", "0")	
		
	try:
		#requesting to open this html for reading
		PV2 = urllib.request.urlopen("http://10.116.25.5/production?locale=en").read()
		
		#uses the BeautifulSoup function to process xml and html in Python.
		PV2_data = BeautifulSoup(PV2, 'lxml')
		PV2_table = PV2_data.find_all('table')
		
		#PV2 global variables for string comparison	
		power_2 = "Currently"
		daily_2 = "Today"
		total_2 = "Since Installation"
		
		#Variables for PV2
		PV2_daily = ""
		PV2_power = ""
		PV2_total = ""
		
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
		
		#Calls to push the data to the firebase
		SendtoFirebasePV2( firebase.database(), date, epoch, PV2_power, PV2_daily, PV2_total)
	except urllib.error.URLError:
		print("Solar Panel PV2 is offline")
		SendtoFirebasePV2( firebase.database(), date, epoch, "0", "0", "0")
		
	try:
		#requesting to open this html for reading
		#PV3a
		PV3_website1 = urllib.request.urlopen("http://10.116.25.8/Dev_batt.cgi").read()
		#PV3b
		PV3_website2 = urllib.request.urlopen("http://10.116.25.8/Dev_status.cgi?&Port=0").read()
		
		#uses the BeautifulSoup function to process xml and html in Python.
		#Dve_batt
		PV3_data1 = BeautifulSoup(PV3_website1, 'lxml')
		PV3_Dve_batt=json.loads(str(PV3_data1.text))
		#Dve_status
		PV3_data2 = BeautifulSoup(PV3_website2, 'lxml')
		PV3_Dve_status=json.loads(str(PV3_data2.text))
		print("\n Solar Panel PV3")
		sys_battery = PV3_Dve_batt['sys_battery']
		today_min_batt = sys_battery['today_min_batt']
		today_max_batt = sys_battery['today_max_batt']
	
		devstatus = PV3_Dve_status['devstatus']
		ports = devstatus['ports']
		port1 = ports[0]
		port2 = ports[1]
		#print(port1)
		#Port 1 Inverter variables
		print("Port 1")
		VAC_in = port1['VAC_in']
		VAC_out = port1['VAC_out']
		battery_voltage = port1['Batt_V']
		print("AC Input Voltage: {}V" .format(VAC_in));
		print("AC Output Voltage: {}V" .format(VAC_out));
		print("Battery Voltage: {}V" .format(battery_voltage));
	
		print("Port 2")
		#Port 2 Charger variables
		cbattery_voltage = port2['Batt_V']
		out_power = port2['Out_kWh']
		input_voltage = port2['In_V']
		print("Battery Voltage: {}V" .format(cbattery_voltage));
		print("Power: {}" .format(out_power));
		print("Input Voltage {}V" .format(input_voltage));
		#print(port2)
		
		#Calls to push the data to the firebase
		SendtoFirebasePV3a(firebase.database(), date, epoch, VAC_in, VAC_out, battery_voltage);
		SendtoFirebasePV3b(firebase.database(), date, epoch, out_power, cbattery_voltage, input_voltage);
	except urllib.error.URLError:
		print("Solar Panel PV3 is offline")
		SendtoFirebasePV3a(firebase.database(), date, epoch, 0, 0, 0);
		SendtoFirebasePV3b(firebase.database(), date, epoch, 0, 0, 0);
		
	try:
		#requesting to open this html for reading
		PV4 = urllib.request.urlopen("http://10.116.25.6/home.htm").read()
		
		#uses the BeautifulSoup function to process xml and html in Python.
		PV4_data = BeautifulSoup(PV4, 'lxml')
		
		#used the find() function to find all html tags consisting with <table> with an id of "OvTb1"
		#PV4
		PV4_table = PV4_data.find('table', id="OvTbl")
		PV4table_row = PV4_table.find_all('tr')
		
		#Variables for PV4
		PV4_power = ""
		PV4_daily = ""
		PV4_total = ""
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
		SendtoFirebasePV4( firebase.database(), date, epoch, PV4_power, PV4_daily, PV4_total)
	except urllib.error.URLError:
		print("Solar Panel PV4 is offline")
		SendtoFirebasePV4( firebase.database(), date, epoch, "0", "0", "0")


	#Calls to push the data to the firebase
	
	
	
	
	
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

