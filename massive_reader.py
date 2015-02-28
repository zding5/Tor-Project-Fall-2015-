#This py reads all the files in the votes directory
#(from sub folders) and calls the extractTor.py
import glob, extractTor,sys

def reader(parent_path, ip, user, pw, database):
	file_counter = 0
	for i in range(1,32):
		print i
		subfolder = ''
		if(i<10):
			subfolder = '0'+str(i)+'/*'
		else:
			subfolder = str(i)+'/*'
		# path = '/Users/dzq/Desktop/CS/PURE/votes/votes-2014-10/'+subfolder
		path=parent_path+subfolder
		files=glob.glob(path)
		for file in files:
			file_counter+=1
			f=open(file, 'r')
			extractTor.the_data_handler(f.name, ip, user, pw, database)
			f.close()
	print file_counter

if __name__ == '__main__':
	reader(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])