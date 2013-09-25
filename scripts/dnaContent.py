def nucleotidecontent(dnaString):
	'''This function must return the contribution    
of nucleotides ATCG (as uppercase) from a given DNA     
string inside a dictionary, where each key refers to    
a nucleotide    
'''    
	#more changes to this script
	# don't know if they will work'
	dnaDict = {}    
	uniques=set(dnaString.upper())    
	for nucleotide in uniques:    
		dnaDict[nucleotide]=dnaString.count(nucleotide)    
    
	return dnaDict

