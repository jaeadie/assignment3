# -*- coding: iso-8859-1 -*-
#script to parse the serprot_pairs.out file

#open the input file and assign it to a variable
infile=open('serprot_pairs.out')

#read each line in the input file
init=infile.readline()

#while there is an index number on the line, continue 
while init[:6] !='     I':
#read the lines
	init=infile.readline()
#define the column names for the output table
colnames=['I', 'J', 'ILEN', 'JLEN', 'MATCH', 'NGAPS', 'NALIG', 'NIDENT', '%IDENT', 'NAS', 'NASAL', 'NRANS', 'RMEAN', 'STEDEV', 'SCORE', 'NUMBER']
#assign the output table to a variable
filename='serprot_file.txt'
#open the output file for writing
file=open(filename, 'w')
#add tabs between each column name and writing to output file
for c in colnames:
        file.write(c + '\t')
# for each line of the input file do...
for line in infile.readlines():
# start a try to catch errors
	try:
#if the first two letter of the line is  T then continue
		if line[:2]==' T':
# keep going
			continue
# #select the approiate parts of each line for each variable
		I=line[1:6]
		J=line[7:11]
		ILEN=line[12:16]
		JLEN=line[17:21]
 		MATCH=line[22:31]
		NGAPS=line[32:38]
 		NALIG=line[39:45]
		NIDENT=line[46:52]
		IDEN=line[53:62]
		NAS=line[63:72]
		NASAL=line[73:82]
		NRANS=line[83:89]
		RMEAN=line[90:99]
		STDEV=line[100:109]
		SCORE=line[110:119]
		NUMBER=line[120:126]
#write each columns variable into the table tabbing so that it is in the right place
		file.write('\n' + I + '\t' + J + '\t' + ILEN + '\t' + JLEN + '\t' + MATCH + '\t' + NGAPS + '\t' + NALIG + '\t' + NIDENT + '\t' + IDEN + '\t' + NAS + '\t' + NASAL + '\t' + NRANS + '\t' + RMEAN + '\t' + STDEV + '\t' + SCORE + '\t' + NUMBER)
# if there is nothing in the line move to the next line 
	except:
		pass
#close the output file
file.close()
