input_string='Private funds for new climate think tank to keep public informed'
string2='People smuggler ridicules Scott Morrison silence on boat arrivals'

#set1=set(i_s)
#print set1
set1=set(input_string.lower())
set2=set(string2.lower())
in_common=set1.intersection(set2)
count=len(in_common)
print in_common
#count=len(set(input_string.lower()))
print count
print len(set1) - in_common
