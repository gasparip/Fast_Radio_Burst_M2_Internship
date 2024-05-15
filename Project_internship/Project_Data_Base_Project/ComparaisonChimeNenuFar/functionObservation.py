# coding=utf-8
import json
import sys
from datetime import datetime, timedelta
import os


def NbrIsDAteChimeData(nbr): 
	try:
  		value = int(nbr)
  		if (((int(nbr[0:2])) in range(15,40 ))and len(str(value))==6):
  			return(True)
  		else:
  			return(False)
	except ValueError:
   		return(False)

#NbrIsDAteChimeData(nbr), verify than a data is a date, use to obtain some information in the Chime data base

def FunListActFrb(dateDetection, TimeFRBactivity_day): #dateDetection en Y-M-D
	listDate = []
	format_date = '%Y-%m-%d'
	date_obj = datetime.strptime(dateDetection, format_date)
	for i in range(-TimeFRBactivity_day,TimeFRBactivity_day+1):
		nouvelle_date_obj = date_obj + timedelta(days=i)
		nouvelle_date = nouvelle_date_obj.strftime(format_date)
		listDate += [nouvelle_date]
	return listDate

#FunListActFrb(dateDetection, TimeFRBactivity_day): This function takes two inputs: a date string in the format "Y-M-D" and an integer TimeFRBactivity_day. It creates a list of dates that includes the input date as well as TimeFRBactivity_day days before and after the input date. The output is a list of date strings in the format "Y-M-D".

def TimeHMS_to_TimeS(TimeHMS):  ## TimeHMS, format 10:12:10.00000
	ListeTimeHMS=[] 
	ListeTimeHMS = TimeHMS.split(':')
	ListeTimeHMS[2].replace('.',',')
	return(float(ListeTimeHMS[2])+float(ListeTimeHMS[1])*60+float(ListeTimeHMS[0])*3600)

#TimeHMS_to_TimeS(TimeHMS): This function takes a time string in the format "H:M:S.MS" and converts it to seconds (as a float). The input time string is first split into a list of three elements (hours, minutes, seconds), and then converted to a float by multiplying the number of hours by 3600, the number of minutes by 60, and adding the number of seconds.

def TimeS_to_TimeHMS(TimeS): 
	heure=str(int(TimeS//3600))
	minute= str(int((TimeS%3600)//60))
	if len(minute)==1: 
		minute ='0' + minute
	seconde = str((TimeS%3600)%60)
	return(heure+':'+minute+':'+seconde)

#TimeS_to_TimeHMS(TimeS): This function takes a time in seconds (as a float) and converts it to a time string in the format "H:M:S". The input time in seconds is first converted to hours, minutes, and seconds using integer and float division, and then formatted into a string with the correct format.

def Name_Frb_Chime_To_Frb_Nenufar(frb):
	frb_nenufar = 0 	
	if int(frb[3:7])<2020: 
		frb_nenufar = frb[:3]+frb[5:]
		frb_nenufar = frb_nenufar[:-1]
	elif int(frb[3:7])>=2022 : 
		frb_nenufar=frb
	else : 
		frb_nenufar = frb[:-1]
	return frb_nenufar

#Name_Frb_Chime_To_Frb_Nenufar(frb): This function takes a string frb and converts it from the CHIME naming convention to the NenuFAR naming convention. The input string frb is first checked to see if it represents an FRB detected before 2020 or after 2022. If it does, the function returns the input string frb unchanged. Otherwise, it removes the last character of the input string frb.

def FrbToObservation_Duration(frb_nenufar):	
	cmd_strES = "psredit /databf/nenufar-pulsar/ES05/*/*/"+frb_nenufar+"*.fits | grep -E 'tsamp|nsblk|nrows|stt_date|stt_time' | colrm 1 67 > /home/pgaspari/Documents/Test/Observation_" + frb_nenufar +".txt"
	print(cmd_strES)
	os.system('GREPDB="'+cmd_strES+'"; /bin/bash -c "$GREPDB"')
	cmd_strLT = "psredit /databf/nenufar-pulsar/LT05/*/*/"+frb_nenufar+"*.fits | grep -E 'tsamp|nsblk|nrows|stt_date|stt_time' | colrm 1 67 >> /home/pgaspari/Documents/Test/Observation_" + frb_nenufar +".txt"
	print(cmd_strLT)
	os.system('GREPDB="'+cmd_strLT+'"; /bin/bash -c "$GREPDB"')
	fichier = open ("/home/pgaspari/Documents/Test/Observation_" + frb_nenufar +".txt","r")
	lines = fichier.readlines()
	date=[]
	time=[]
	duration=[]	
	for i in range(len(lines)//5):
		date += [lines[i*5].replace('\n','')]
		time += [lines[i*5+1].replace('\n','')]
		duration += [float(lines[i*5+2].replace('\n',''))*float(lines[i*5+3].replace('\n',''))*float(lines[i*5+4].replace('\n',''))]
	return date,time,duration

#FrbToObservation_Duration(frb_nenufar): This function takes a string frb_nenufar in the NenuFAR naming convention and computes the observation duration for all files containing this FRB. The function first creates two command strings cmd_strES and cmd_strLT to extract metadata from two different directories and then runs them using subprocess.run. The function then opens a text file containing the metadata and extracts the observation start date, time, and duration for each file that contains the FRB. Finally, the function returns three lists containing the start dates, start times, and observation durations, respectively.

def FrbToDetectionChime(frb_chime,filenamejson):
	with open(filenamejson, 'r') as f:
		data = json.load(f)
		liste_Date_TIME_FRB=[]
		for cle,valeur in data[frb_chime].items():
			ObservationTime = []
			if NbrIsDAteChimeData(cle):
				liste_Date_TIME_FRB+=[valeur["timestamp"]["value"]]
		return liste_Date_TIME_FRB


# FrbToDetectionChime(frb_chime,filenamejson): This function takes two arguments: frb_chime, a string that represents the name of a CHIME/FRB object, and filenamejson, a string that represents the name of a JSON file. The function opens the JSON file and reads its contents using the json.load() method, which returns a Python dictionary. The function then iterates over the items in the dictionary corresponding to the frb_chime key and extracts the values associated with timestamps that satisfy a certain condition using the NbrIsDAteChimeData() function. Finally, the function returns a list of these timestamps.

def FindCorrelationBtwObservationAndDetection(dateNenufar,hoursNenufar,DurationNenufar,dateChime,PeriodActivity): 
	listCorrelation = []
	for detectionDay in dateChime:
		detection = True
		for indiceObservation in range(len(dateNenufar)):
			if dateNenufar[indiceObservation] in FunListActFrb(detectionDay.split()[0],PeriodActivity):
				if detection : 
					listCorrelation += [[detectionDay]]
					detection = False	
				listCorrelation[-1] += [[dateNenufar[indiceObservation],hoursNenufar[indiceObservation],DurationNenufar[indiceObservation]]]
				
	return listCorrelation

# This function takes in several parameters: dateNenufar: a list of dates of observations made by the NenuFAR radio telescope. hoursNenufar: a list of times (in hours) of observations made by the NenuFAR radio telescope. DurationNenufar: a list of durations (in seconds) of observations made by the NenuFAR radio telescope. dateChime: a list of dates on which an FRB was detected by the CHIME radio telescope.PeriodActivity: an integer representing the number of days before and after a CHIME detection date during which the NenuFAR observatory could have observed the same FRB.
#The function starts by creating an empty list listCorrelation to store the correlations found between NenuFAR observations and CHIME detections. Then, for each date in dateChime, the function loops through all the observations made by NenuFAR and checks if the observation date falls within the PeriodActivity window around the CHIME detection date. If an observation falls within this window, the function appends a new sublist to listCorrelation containing the CHIME detection date, and then appends another sublist to this new sublist containing the date, time, and duration of the NenuFAR observation. Finally, the function returns the listCorrelation containing all the correlations found between NenuFAR observations and CHIME detections.


def FrbToObservation_Duration_tf(frb_nenufar):	
	cmd_str = "find /databf/nenufar-tf/??05/ -name '*"+frb_nenufar+"*.parset' > /home/pgaspari/Documents/Test/Observation_Path_"+frb_nenufar+"_tf.txt"
	print(cmd_str)
	os.system('GREPDB="'+cmd_str+'"; /bin/bash -c "$GREPDB"')
	fichier_path = open ("/home/pgaspari/Documents/Test/Observation_Path_"+frb_nenufar+"_tf.txt","r")
	lines_path = fichier_path.readlines()
	cmd_str2="echo > /home/pgaspari/Documents/Test/Observation_"+frb_nenufar+"_tf.txt"
	print(cmd_str2)
	os.system('GREPDB="'+cmd_str2+'"; /bin/bash -c "$GREPDB"')
	for line_path in lines_path:
		cmd_str3 = "cat "+line_path.replace('\n','')+"| grep -E \"Observation.startTime|Observation.stopTime\" | cut -d'=' -f2 >>/home/pgaspari/Documents/Test/Observation_"+frb_nenufar+"_tf.txt"
		print(cmd_str3)
		os.system('GREPDB="'+cmd_str3+'"; /bin/bash -c "$GREPDB"')
	fichier = open ("/home/pgaspari/Documents/Test/Observation_"+frb_nenufar+"_tf.txt","r")
	lines = fichier.readlines()[1:]
	date=[]
	time=[]
	time2=[]
	duration=[]
	listeDateHours=[]	
	for i in range(len(lines)//2) : 
		listeDateHours = lines[i*2].split('T')
		date += [listeDateHours[0].replace('\n','')]
		time += [listeDateHours[1].replace('\n','')[:-1]]
		duration += [(TimeHMS_to_TimeS(lines[i*2+1].split('T')[1].replace('\n','')[:-1])-TimeHMS_to_TimeS(listeDateHours[1].replace('\n','')[:-1]))]

	
	#	time += [lines[i*5+1].replace('\n','')]
	#	duration += [float(lines[i*5+2].replace('\n',''))*float(lines[i*5+3].replace('\n',''))*float(lines[i*5+4].replace('\n',''))]
	# return date,time,duration

	return date,time,duration

