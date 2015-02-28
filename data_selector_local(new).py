TOP = 25

# import MySQLdb
import sys
import numpy
import csv
import datetime
import os

relay_dic = {}
top_relay_dic = {} #for plotting storage. Store daily average dev for tops
Tops = []
Bottoms = []
# path = "/Users/dzq/Desktop/CS/PURE/tor_oct.csv"


def data_selecting(path):
	
	RS_max = 0
	RS_min = 0
	RS_median = 0
	RS_mean = 0.0
	RS_std = 0.0

	R_4_max = 0
	R_4_min = 0
	R_4_median = 0
	R_4_mean = 0.0
	R_4_std = 0.0
	R_4_Stat_List = []

	original = file(path, 'r')
	reader = csv.reader(original)

	for row in reader:

		if row[3] not in relay_dic:
			relay_dic[row[3]] = {}

		### server
		if row[1] not in relay_dic[row[3]]:
			relay_dic[row[3]][row[1]] = {} 

		### time for relay and server
		if row[2] not in relay_dic[row[3]][row[1]]:
			relay_dic[row[3]][row[1]][row[2]] = row[5:]


	for R_ID in relay_dic.keys():

		# print str(datetime.datetime.now())

		print "Currently at relay: "+R_ID

		num_of_servers = 0

		RS_max_list = []
		RS_min_list = []
		RS_median_list = []
		RS_mean_list = []
		RS_std_list = []

		for S_Name in relay_dic[R_ID].keys():

			print '   Now: '+R_ID+' and '+S_Name

			List_of_Positive_Dev = []
			List_of_Positive_points = []

			counter = 0
			for R_and_S in relay_dic[R_ID][S_Name].keys():

				counter+=1
				ad = int(relay_dic[R_ID][S_Name][R_and_S][0])
				re = int(relay_dic[R_ID][S_Name][R_and_S][1])
				Dev = ad - re

				if(Dev>0): #Dev>0
					### the top negative ones too
					List_of_Positive_Dev.append(Dev)
					# List_of_Positive_points.append([ad,re])

			print counter
			###point_dic[R_ID] = List_of_Positive_points###Don't use it. Too big!
			###For plotting, we want the points to be average of each day (24ish hours)

			if(len(List_of_Positive_Dev)>0):
				RS_max = numpy.amax(List_of_Positive_Dev)
				RS_min = numpy.amin(List_of_Positive_Dev)
				RS_median = numpy.median(List_of_Positive_Dev)
				RS_mean = numpy.mean(List_of_Positive_Dev)
				RS_std = numpy.std(List_of_Positive_Dev)

			RS_max_list.append(RS_max)
			RS_min_list.append(RS_min)
			RS_median_list.append(RS_median)
			RS_mean_list.append(RS_mean)	
			RS_std_list.append(RS_std)

		# print len(RS_mean_list)
		R_4_max = numpy.amax(RS_max_list)
		R_4_min = numpy.amin(RS_min_list)
		R_4_median = numpy.median(RS_median_list)
		R_4_mean = numpy.mean(RS_mean_list)
		R_4_std = numpy.std(RS_std_list)
		Relay_Stat = [R_ID, R_4_max, R_4_min, R_4_median, R_4_mean, R_4_std]
		R_4_Stat_List.append(Relay_Stat)
		# return

	Sorted_R_4_List = sorted(R_4_Stat_List, key=lambda item:item[4],reverse=True)
	Tops = Sorted_R_4_List[:TOP]
	# print Tops

# def building_top_relay_dic():

	# print Tops

	for Toppie in Tops:

		R_ID = Toppie[0]

		top_relay_dic[R_ID] = {}
		
		for S_Name in relay_dic[R_ID].keys():

			top_relay_dic[R_ID][S_Name] = {}

			for Time in relay_dic[R_ID][S_Name].keys():

				time_split = Time.split(' ')
				# print time_split[0].split('-')[1]
				if(time_split[0].split('-')[1]=='09'):
					continue
					# return

				if(time_split[0] not in top_relay_dic[R_ID][S_Name].keys()):

					top_relay_dic[R_ID][S_Name][time_split[0]] = [] #for one day
					
					#counter+=1#??? counter for each day
					
					ad = int(relay_dic[R_ID][S_Name][Time][0])
					re = int(relay_dic[R_ID][S_Name][Time][1])
					Dev = ad - re

					if(Dev>0): #Dev>0			
						top_relay_dic[R_ID][S_Name][time_split[0]].append(Dev)

				else:

					ad = int(relay_dic[R_ID][S_Name][Time][0])
					re = int(relay_dic[R_ID][S_Name][Time][1])
					Dev = ad - re

					if(Dev>0): #Dev>0			
						top_relay_dic[R_ID][S_Name][time_split[0]].append(Dev)

			# print top_relay_dic

			for Day in top_relay_dic[R_ID][S_Name].keys():

				if(top_relay_dic[R_ID][S_Name][Day]!=[]):

					# top_relay_dic[R_ID][S_Name][Day] = numpy.mean(top_relay_dic[R_ID][S_Name][Day])
					top_relay_dic[R_ID][S_Name][Day] = numpy.mean(top_relay_dic[R_ID][S_Name][Day])


				else:

					top_relay_dic[R_ID][S_Name][Day] = 0




	i = 0
	for R_ID in top_relay_dic.keys():

		foldername = './new/Top'+str(i)#+'_'+R_ID
		i+=1
		if not os.path.exists(foldername):
			os.makedirs(foldername)

		j=0
		for S_Name in top_relay_dic[R_ID].keys():

			filename = foldername+'/'+S_Name+'.csv'
			j+=1

			day_array = sorted(top_relay_dic[R_ID][S_Name], key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))

			dayer = []
			for ii in range(0,len(day_array)):
				dayer.append(day_array[ii][-2:])

			with open(filename, 'wb') as csvfile:
				spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
				for k in range(0,len(day_array)):
					spamwriter.writerow([dayer[k],top_relay_dic[R_ID][S_Name][day_array[k]],R_ID])

# def making_csv():

data_selecting()
# building_top_relay_dic()
# print '\n'
# print top_relay_dic
















