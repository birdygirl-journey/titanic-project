#this  is lecture 3 in which we are going to study list and tuple 

#list  in python

marks = [9.9,3.4,3.25,213.5,32.5,]
print(type(marks))
print(marks)
print(marks[1])
print(marks[3])
print(marks[2])
print(marks[4])
print(len(marks))#len=lenght
#in list can store integer ,string ,name ,number any thing
student=["hafsa",22,2008,"class=10th class"]
print(student)
print(student[0])
student[0]="ashir"
print(student)


# list slicing 
marks1=[22,3,54,43,32]#last number is not included means 32 is not included,22=0 not 1 it is not first number.
print(marks1[1:4])
print(marks[1:])#that how we can include last value

#list method
#no.1          list.append(it is also called mutating mean changing like add substrat)
list=[1,2,3]
list.append(4)
print(list)
#no.2 and no.3  ascending the number is sort
print(list.sort(reverse=True))#reverse=true mean descending
print(list)#in this method we can use alphabet or number or word any
#no.4        insert mean adding value between or centre or end 
list1=[1,2,3,4]
list.insert(1,5)
print(list)

#no.5 list remove and pop both is used to remove a number difference pop remove specific and remove first number
list2=[2,6,8,0,9]
list2.remove(2)
#print(list2)
#list2.pop(6.2)
#print(list2)


#tuple 


#no.1
tup=(1,2,3,4,)
print(tup)
print(type(tup))

#slicing tuple
print(tup[1:3])#1 is not included start will with 2
print(tup.index(1))#index method
print(tup.count(2))


#lets practice
#movie1=(input("enter name of ur fvt movie"))
#movie2=(input("enter name of ur fvt movie"))
#movie3=(input("enter name of ur fvt movie"))
#ist=(movie1,movie2,movie3)
#print(list)


#no.2 
list76=[1,2,4]
list77=[1,2,3]
copy_list76= list76.copy()
copy_list76.reverse()
if(copy_list76 == list76):
    print("palindrome")
else:
    print("non palindrome")

#no.3
grade=["A","B","A",]
grade.sort()
print(grade)