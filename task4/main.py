t = int(input())
if (t % 4 == 0) and (t % 100 !=0) or (t % 400 == 0):
print ('високосный')
else:
print('не високосный')
