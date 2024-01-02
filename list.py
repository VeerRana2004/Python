range(20)
L=list(range(20))  #take 1-19 list
print(L)
L[11]='CSPIT'      #add CSPIT at 11 index
print(L)
print(L[2:15:4])   #add slicer
L.append(500)      #add 500 at end of list
print(L)
L.insert(3,'Charusat')  #add Charusat at 3 index
print(L)
L.remove('CSPIT')  #remove CSPIT from list
print(L)
a,b,*c=L          #assign a=0,b=1,c=exiting list
print(a,b,c)
a,b,*c,d,e=L      #assign a=0,b=1,c=exiting list,d=n-1,e=n
print(a,b,c,d,e)
L.append(10)
print(3 in L)     #check if 3 in list
print(L.count(10))  #count total 10 form list 
print(L.count(100))
L.reverse()        #set list in reverse order
print(L)
L.remove('Charusat')
print(L)
L.sort()          #sort list in esending
print(L)
L.sort(reverse=True)  #sort list in desending 
print(L)
list1= [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana",
"orange"]]
print(list1)
print(list1[4][0],list1[8][2])  #ans=python,orange
L=[10,20,30,20,10]
S=set(L)       #convert list into set
print(S)