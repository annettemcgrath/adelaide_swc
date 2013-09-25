input_string="GACTACTCATCTACTACTACTCATCGATGCTGCATGCTAGCATCGAGCTAGCATG"

g= input_string.count('G')
a= input_string.count('A')
t= input_string.count('T')
c= input_string.count('C')
#print g,a,t,c
my_dict={'G':g,'A':a, 'T':t, 'C':c}
print my_dict

#length=len(input_string)
#print length
#print g+c
gc=(g+c)/float(len(input_string))*100
print gc
