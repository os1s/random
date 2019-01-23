#!/usr/bin/python3
import os.path
import sys
import statistics as st

def calculator(filen, task):
	"""calculates the user defined task"""
	numbers = []
	fp = open(filen, 'r')
	for x in fp:
		numbers.append(float(x))
	if task == 'sum':
		result = sum(numbers)
		print('Sum is: ' +str(result))
	elif task == 'avg':
		result = st.mean(numbers)
		print('Average is: '+str(result))
	elif task == 'median':
		result = st.median(numbers)
		print('Median is: '+str(result))
	else:
		print('Could not recognize the task')
	fp.close()
	#checks for optional parameters
	if len(sys.argv) == 5 and 'result' in locals():
		optionalcalc(sys.argv[3], sys.argv[4], result)

def optionalcalc(task, comparison, task1result):
	"""calculates the optional task if needed"""
	comparison = float(comparison)
	if task == 'gt':
		if task1result > comparison:
			print(str(task1result)+ ' is greater than '+str(comparison))
		else:
			print(str(task1result)+ ' is not greater than '+str(comparison))
	elif task == 'lt':
		if task1result < comparison:
			print(str(task1result)+ ' is less than '+str(comparison))
		else:
			print(str(task1result)+ ' is not less than '+str(comparison))
	elif task == 'eq':
		if task1result == comparison:
			print(str(task1result)+ ' is equal to '+str(comparison))
		else:
			print(str(task1result)+ ' is not equal to '+str(comparison))
	else:
		print('Could not recognize the optional task')

#checks that the user defined file exists
if os.path.isfile(sys.argv[1]):
	calculator(sys.argv[1], sys.argv[2])
else:
	print('The file '+sys.argv[1]+' does not exist')
