hrs1 = int(input('HRS_1: '))
while hrs1 < 0:
	hrs1 = int(input('HRS_1: '))

min1 = int(input('MIN_1: '))
while min1 < 0:
	min1 = int(input('MIN_1: '))
while min1 > 59:
	min1 = int(input('MIN_1: '))

#operation = input('Operation (+/-): ')

hrs2 = int(input('HRS_2: '))
while hrs2 < 0:
	hrs2 = int(input('HRS_2: '))

min2 = int(input('MIN_2: '))
while min2 < 0:
	min2 = int(input('MIN_2: '))
while min2 > 59:
	min2 = int(input('MIN_2: '))

hrs = hrs1 + hrs2
min = min1 + min2
mod = min % 60

if min >= 60:
	hrs += 1


print(hrs, ':', mod, " hrs")

input('')