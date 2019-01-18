list1 = ['Phan Thanh Thao']

list2 =['Female',1997]

list3=list1+list2

print("Person:")

print list3


index = 0 

length = len(list3)

while index < length:
    print(index, 'stands for', list3[index])
    index += 1 