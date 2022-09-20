from tokenize import Number


my_list=[]

for i in range(10):
    number = int(input('enter your numbers:'))
    my_list.append(number)
print('list vared shode shoma:\n' , my_list)
for num in range (len(my_list)):
    for j in range (num+1 , len(my_list)):
        if my_list[num] > my_list[j]:
            my_list[num] , my_list[j] = my_list[j] , my_list[number]

print(' list moratab shode =' , my_list)

