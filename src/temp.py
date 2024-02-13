list1 = [6,0.9,0,0.5,2,4,2,1,3,1.5,2.5]
list2 = [0,10.1,10.6,10.4,8.6,6.3,8.5,9.9,7.7,9.3,8.3]
list3 = list()

print("gravity:")
for i in list1:
    print(60*9.8*i)
    list3.append(60*9.8*i)

print("velocity")
x= 0
for i in list2:
    print(0.5*60*i*i)
    list3[x] = list3[x] + 0.5*60*i*i
    x+=1

print("total:")
for i in list3:
    print(i)

