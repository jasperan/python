def exploder(num):
	if (num != 1):
	 num = num * exploder(num-1)
	 return num
	else:
	 return num

num = 200
result = exploder(num)
print result