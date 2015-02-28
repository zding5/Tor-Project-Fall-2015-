import Gnuplot
import sys
import os

# for i in range(0,25):
# 	print i
# 	subfolder = 'top'+str(i)

# 	# gnuplot -e "relay='top0'" plot.plt
# 	gnucommand = '''gnuplot -e "relay=''' + "'"+subfolder+"'" + '"' + ' plot.plt'
# 	os.system(gnucommand)

		
for root, dirs, files in os.walk(sys.argv[1], topdown=False):
    # for name in files:
    #     print(os.path.join(root, name))
    #     if Top

    # for name in files:
    for name in dirs:
    	if "Top" in os.path.join(root,name):
    		# for files in os.walk(os.path.join(root,name), topdown=False):
				# for file_name in files:
			print os.path.join(root,name)
					# print(os.path.join(root, file_name))
			gnucommand = '''gnuplot -e "relay=''' + "'"+os.path.join(root,name)+"'" + '"' + ' plot.plt'
			# gnucommand = '''gnuplot -e "relay=''' + "'"+name+"'" + '"' + ' plot.plt'

			os.system(gnucommand)


