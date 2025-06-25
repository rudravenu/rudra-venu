# 1.	Access the value 200 from this nested tuple?
t = (10, 20, (30, 40, (100, 200)), 50)
print(type(t))
print(t[2][2][1])
# 2.	Access the value 70 from the nested structure?
data = (10, (20, 30, (40, 50, (60, 70))), 80)
print(type(data))
print(data[1][2][2][1])

# 3.	Convert   j=(10,20,30,40,50)  tuple data type to list data type?
j=(10,20,30,40,50)
k=[]
for i in j:
    k.append(i)
print(type(k))    
print(k)    
# 4.	Find Common Elements Between Two Tuples
touple_1 = (1, 2, 3, 4)
touple_2=(3,4,5,6)
for i in touple_1:
    for j in touple_2:
      if  i==j:
         print(i)
