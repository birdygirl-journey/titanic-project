#part 2 of lecture 5 (for)
list=[1,3,4,6,7,8,]#for use in list but num(el)
for el in list:
    print(el)
list2=["apple","banana"]#for use in list but value like alphabet
for val in list2:
    print(val)
tup=(1,2,3,4,5)#for use in tuple
for num in tup:
    print(num)
str="hafsaashir"
for char in str:
    if(char == 'r'):
        print ("found")
        break
    print(char)
else:
    print("end of code")

#pratice question
#print the element of list by using loop
list3=[1,2,3,4.5,6,7,8,9]
for el3 in list3:
    print(el3)

#search for number x in tuple using loop
num2=(1,2,3,4,5,9,8,9)#the process use in searching in this question is called"linear search"
x=9
idx =0
for el4 in num2:
    if(el4 == 9):
        print("number is found",idx)
    idx+=1
#(RANGE)
seq=range(5)
for i in seq:
    print(i)

for w in range(10):#range condition(stop)
    print(w)
print ("stoop")
for s in range(2,7):#range condition(start,stop)
    print(s)
print("hehehehe")
for h in range(2,10,2):#range condition(start,stop,step)
    print(h)


#pratice
#1print num from 1 to 100
for j in range(1,101):
    print(j)
print("stop")
#2print num from 100 to 0
for o in range(100,0,-1):
    print(o)
#3print multiplication num of n
#n=int(input("enter the number:"))
#for b in range(1,11):
 #   print(n*b)


#PASS IN LOOP means null empty
for k in range(8):
    pass
print("empty")
#practice
#WAP to find the sum of first n number(by using while)
s=5
sum=0
i=1
while i <=s:
    sum+=i
    i+=1

print("total sum =",sum)

#WAP to find a first fractional of n number(while,for)
u=5
fact=1
i=1
while i <=u:
    fact*=i
    i+=1

print("total sum =",fact)
#using (for)
n=5
fact=1
for c in range(1,n+1):
    fact*=c
print("factorial=",fact)


print("the end of leacture 5")