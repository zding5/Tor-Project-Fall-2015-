import string
import MySQLdb


### 1. read file
### 2. choose to use or not
### 3. extract items
### 4. format(parse?)
### 5. send to database


### the wrapper function for all

def the_data_handler(file_name, ip, user, pw, database):
	wholetext = read_the_file(file_name)
	if(is_useful(wholetext)):
		table_list = mining(wholetext)
		parsing(table_list)



### read from file

def read_the_file(file_name):### return the whole vote file as a string

	file_object = open(file_name, "r")
	wholetext = file_object.read()
	file_object.close()
	return wholetext

### decide usefulness of the file

def is_useful(wholetext):
	
	if "Measured" not in wholetext:
		return False
	return True

### extract

def mining(wholetext):
	
	table_list=[]
	Time_String = ""
	Server_Name = ""
	Server_ID = ""
	linelist = wholetext.split('\n')
	
	for linectr in range(0, len(linelist)):
		### exit when hit signature part
		cur_line = linelist[linectr]

		### extract time
		if cur_line.startswith('published'):
			Time_String = cur_line[10:]

		### extract server ID and name
		if cur_line.startswith('dir-source'):
			templist = cur_line.split(' ')
			Server_Name = templist[1]
			Server_ID = templist[2]

		### extract relay info (ID, name, abw, rbw)
		if cur_line.startswith('r '): ### find a way to jump block
			if "Measured" not in linelist[linectr+3]:
				continue
			templist = cur_line.split(' ')
			Relay_Name = templist[1]
			Relay_ID = templist[2] ### not sure about 3
			if linelist[linectr+3].startswith("w "):

				cur_plus_three = linelist[linectr+3]
				Relay_Advertised = int(cur_plus_three[(cur_plus_three.find("h=")+2):cur_plus_three.find(" M")])
				Relay_Real = int(cur_plus_three[(cur_plus_three.find("d=")+2):])#cur_plus_three.find("\n")])

			### put data in a list
			block_list = [Server_ID, Server_Name, Time_String, Relay_ID, Relay_Name, Relay_Advertised, Relay_Real]
			table_list.append(block_list)

	return table_list

### parsing data into database

def parsing(table_list, ip, user, pw, database):

	db = MySQLdb.connect(ip,user,pw,database)
	cursor = db.cursor()
	for i in range(0, len(table_list)):
		cursor.execute("INSERT INTO tor_oct (ServerID, Server_Name, Time, RelayID, Relay_Name, Advertised_BW, Measured_BW) VALUES(%s, %s, %s, %s, %s, %s, %s)", (table_list[i][0], table_list[i][1], table_list[i][2], table_list[i][3], table_list[i][4], table_list[i][5], table_list[i][6]))
	db.commit()
	db.close()









