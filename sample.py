def unique(l):
	'''
	This function generate a list of unique values from l
	'''
	mylst = []
	for i in l:
		if i not in mylst:
			mylst.append(i)
	return mylst


def reverse(s):
	'''
	This function generates the reverse of s. s can be a string or a list. It returns the type given to it
	'''
	new_list = []
	another_list = []
	final_string = ""

	if type(s) == str:
		for i in s:
			new_list.append(i)
		length = len(new_list)

		while length > 0:
			another_list.append(new_list[length - 1])
			length -= 1
		for i in another_list:
			final_string += i

		return final_string
	
	else:
		for i in s:
			new_list.append(i)
		length = len(new_list)

		while length > 0:
			another_list.append(new_list[length - 1])
			length -= 1

		return another_list


def intersection(a,b):
	'''
	This function returns the intersection of a and b - A list of common elements between a and b
	'''
	mylst2 = []

	for item in a:
		if item in b:
			mylst2.append(item)

		return mylst2

def generate(steps):
	pass

def parse_csv(csv_string):
	'''
	This function parses a CSV string as a list. The specification demands that the first row of data represents the column names
	'''
	pass

def frequency(needle, haystack):
	'''
	This function returns the number of times needle appears in haystack
	'''
	

def sort(l):
	'''
	This function returns a sorted version of l
	'''
	pass