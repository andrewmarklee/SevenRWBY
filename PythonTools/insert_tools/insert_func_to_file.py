# insert_func_to_file
#	rwby_file.il
#	rwby_insertion_beg
#	rwby_insertion_end
#	vs_file.il
#	vs_func_header
#	vs_func_footer
#	output_file.il

# Opens vs_file, and identifies function to be inserted
# Opens rwby_file, and determines place to be inserted
# Function is inserted, and entire resulting string stored

#import re
#from sys import argv

#cmd, rwby_file, rwby_func_header, rwby_func_footer, \
#	vs_file, vs_insertion_beg, vs_insertion_end, \
#	output_file = argv

def insertFuncIntoStr(funcFileStr, funcHead, funcFoot, \
		insertToMe, firstHalfEnd, secondHalfBeg) :
	
	funcStartNdx = funcFileStr.find(funcHead)
	funcEndNdx = funcFileStr.find(funcFoot);
	if funcStartNdx == -1 :
		print('Error: No function header found in RWBY library:\n' + funcHead)
		exit()
	if funcEndNdx == -1 :
		print('Error: No function footer found in RWBY library:\n' + funcFoot)
		exit()
	funcTxt = funcFileStr[funcStartNdx : funcEndNdx + len(funcFoot)]

	
	firstHalfNdx = insertToMe.find(firstHalfEnd)
	secondHalfNdx = insertToMe.find(secondHalfBeg);
	if firstHalfNdx == -1 :
		print('Error: No first half found in assembly:\n' + firstHalfEnd);
		exit()
	if secondHalfNdx == -1 :
		print('Error: No second half found in assembly:\n' + secondHalfBeg);
		exit()
	firstHalfTxt = insertToMe[0:firstHalfNdx + len(firstHalfEnd)]
	secondHalfTxt = insertToMe[secondHalfNdx:-1]

	preCom = "\n// sevenvolts insertion begin\n"
	postCom = "\n// sevenvolts insertion end\n"
	return firstHalfTxt + preCom + funcTxt + postCom + secondHalfTxt

with open('j.txt','r') as j :
	jTxt = j.read()
jHead = "Speaker Paul Ryan resigned "
jFoot = "collapse and an economic downturn."

with open('k.txt','r') as k :
	kTxt = k.read()
kHalfEnd = "What are people supposed to do, just stop trying to lose weight? Well, yeah, maybe. "
kHalfBeg = "Accepting a weight you're"

oTxt = insertFuncIntoStr(jTxt, jHead, jFoot, kTxt, kHalfEnd, kHalfBeg)

with open('o.txt','w') as o :
	o.write(oTxt)