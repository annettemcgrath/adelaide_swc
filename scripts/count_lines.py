#Read the content of the file line by line
#Get the length of each line and sum it
#get the total number of lines in a file

file1= open("pg76.txt", "r")
line = file1.readline()
total=0
count =0

while line != '':
	total += len(line)
	count +=1
	line = file1.readline()
reader.close()
	

print "total length:" + str(total) + ',' + "line count:" + str(count)

