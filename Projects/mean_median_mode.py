#Mean

list1 = [12,43, 87, 45, 65, 23, 37, 0]
mean = sum(list1)/len(list1)
print('Mean of {} is {}'.format(list1,mean))


#Median
list2 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list2.sort()

if len(list2) %2 == 0:
    m1 = list2[len(list2)//2]
    m2 = list2[len(list2)//2-1]
    median = (m1+m2)/2
else:
    median = list2[len(list2)//2]

print('Median of {} is {}'.format(list2,median))

#Mode 

list3 = [14, 18, 22, 24, 10, 28, 23, 25, 26, 22]
frequency = {}
mode = None
for i in list3:
    frequency.setdefault(i, 0)
    frequency[i] += 1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i

print('Mode of {} is {}'.format(list3, mode))