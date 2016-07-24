def SampleFunction():
	print 'asadsasa'

def VowelCount(a):
	count = 0
	for char in a:
		if char in 'aeiou':
			count = count + 1
	return count


if __name__ == '__main__':
	#when direct running
	print 'I am being directly run'
	SampleFunction()
else:
	print 'I am being imported'