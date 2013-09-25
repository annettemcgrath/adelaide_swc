
#Given a string 'filename', write a function which opens that file, iterates over all sequences and writes a bit of stats about each sequence:
#- print the name of each sequence
#- count of ns
#- gc content

#prints amount of sequences in the file

def sequence_info_stats(sequence_file):
	file1=open(sequence_file, 'r')
	line=file1.readline()
	n=0
	gc=0
	while line !='':
		if line.startswith('>'):
			name=line
			#print name
			print "The sequence has name " + name
			line=file1.readline()
		else:
			n+=line.count('N')
			gc +=line.count('G') + line.count('C')
			line=file1.readline()
			print "It has " + str(n) + " Ns and " + str(gc) + " GC content"
			#print gc, n
	
	

print sequence_info_stats('sequence.txt')

			
