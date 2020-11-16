income = int(input('Please write your daily income($): '))
if income >= 1000:
	print('You can buy a new car')
elif income < 1000 and income >= 100:
	print('You can buy a new laptop')
else:
	print('Just put the raise into savings')
