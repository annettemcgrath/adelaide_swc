import dnaContent
#commenting
#commenting again
#Sequence	Prefix	
test=[['ACGTGT', {'A':1, 'C':1, 'G':2, 'T':2}],
		['CAGGTT', {'A':1, 'C':1, 'G':2, 'T':2}]]
# Run and report    
passes = 0    
for (i, (seq, expected)) in enumerate(test):    
	if dnaContent.nucleotidecontent(seq) == expected:    
		passes += 1    
	else:    
		print('test %d failed' % i)    
    
print('%d/%d tests passed' % (passes, len(test)))

