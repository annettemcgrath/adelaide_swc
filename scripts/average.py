#Exercise 2
#read 'pitching.csv' line by line
#Extract the 'IPouts' value per line, sum it and determine th average.
#The average value must be a float.

file1= open("Pitching.csv", "r")
line = file1.readline()
line=file1.readline()
IPout= 0

total=0
count =0

while line != '':
	array=line.split(',')
	IPout = array[12]
	total += float(IPout)
	count +=1
	line=file1.readline()

total_average = total/count
print total_average
	

