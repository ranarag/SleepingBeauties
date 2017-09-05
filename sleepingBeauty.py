import numpy as np
import re
import sys

def findSleepingBeauty(filename=None):
    
	fp = open(filename, "r")
	sleepingBeautyIds = []    

	count = 0
	sb = 0
	dummy =0
	tot = 0
	same = 0

	for line in fp:
		if re.search(":",line):
			s = line.replace(":","")		    
			count +=1
		elif re.search(",",line):
			line1 = line[:-2]
			mylist = [int(x) for x in line1.split(',')]
		    
			count +=1

		if count % 2 == 0 and np.sum(mylist)>19:
			out = []
		    
		    
			year = 0
			tot += 1
		

			for i in range(len(mylist)):
				try:
					out.append((mylist[i]+mylist[i+1]+mylist[i+2]+mylist[i+3]+mylist[i+4])/5) # moving average with window length 5
				except:
					dummy = 1

			if len(out) > 0:
				maxval = np.max(out)
			else:
				continue
			if maxval > 0:
				nor_out = [float(x) / maxval for x in out]
			else:
				continue
			if len(nor_out) <= 10: # paper should be cited for atleast 11 years
				continue

			if reduce(lambda x,y: x and (y < 0.2),nor_out[0:10],True) is True:  # To seive normalized citations based on the following criteria
				sleepingBeautyIds.append(s)                                     # that atleast for 10 yrs norm citation count should be  < 0.2'''

	return sleepingBeautyIds



if __name__ == "__main__":
    sb_ids = findSleepingBeauty(sys.argv[1])
    with open('sb_ids.txt', 'w') as fid:
        fid.write(''.join(sb_ids))
    