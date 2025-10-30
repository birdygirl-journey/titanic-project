#this a leacture 2 of python "string and conditional statements."

#type of string .

str1="this is double code string."
str2='this is single code string.'
str3="""this is triple code string."""

#so this \n is use to skip a line.
str4="this a string. \n in which i am using two line to write my code"
print(str4)

#for using space like starting a new paragraph we use this \t
str5="i love writing code \t so i use visual code to write cose."
print(str5)

#basic contenation.

#no.1 contenation(this is use to join 2 or 3 lines or word.for example joining surname and name like hafsa+ashir=hafsa ashir)
str6="hafsa"
str7="ashir"
print(str6+str7)

#we can also use final_str to store 2 or 3 string for example:final_str=str6+str7 then print(final_str)


#no.2 lenght of string (tell us how how many alphabet or number in one word)
str8="hafsa"
print(len(str8))

#if u want to give space between two words and join them in contenation and want to know there lenght,
str9="hafsa"
str10="ashir"
final_str=str9+" "+str10
print(len(final_str))

#no.3  index (this mean want to know the number 5 or 4 or any alphabet and number for example hafsa i want to know 2 number alphabet that is f .in index it start from 0 to any num.)
str11="hafsa"
ch=str11[4]
print(ch)
print(str11[3])

#no.4 slicing wanting a part of string like i have hafsa name and i want fsa from it so i use this
str12="hafsaashir"
print(str12[2:5])
#if a want from starting word like h from hafsa so empty space is equal to 0.
print(str12[ :4])
#i want to 0 to last index 
print(str12[0: ])

#no.5 negetive index (mean starting from -1 to endless number .)
str13="hafsa"
print(str13[-3:-1])

#no.6 str.endwith(ege).it is used to know it this for exapmle like i write hafsa it end with fsa right so hat is true it write we hat false.
str14="hafsaashir"
print(str14.endswith("shir"))
#if i write wrong they will not answer me or give error.

#no.7 str.capitalize()
str15="hafsa"
print(str15.capitalize())

#no.8 str.replace("o","a")
str16="hufsa"
print(str16.replace("a","d"))

#no.9 str.find("?")
str17="i love writing code"
print(str17.find("v"))

#no.10 str.count("love")
str18="i love writing code bcz i love it yayayayyay."
print(str18.count("love"))

#pratice (input name and measure its lenght){this is in green but later remove hastag and play it.}
#str19=input("enter your name")
#print("this is the lenght of your name",(len(str19)))

#count how many time $ come in string.
str20="i love money in $$$ dollar"
print(str20.count("$"))

#no.11 conditional statement if/ else /eliffor example of traffic light
light="purple"

if(light == "green"):
   print("u can go ")#and the space we give before is like for example jab mena html kiya waha ya wala sign{}mein use karti thi zyadi si statement ko combine karna kaliya wesa hi ya tab zyada si satement ko combine karna kaliya diya jata ha.

elif(light =="red"):
   print("stop")

elif(light =="yellow"):
   print("wait")

else:
   print("light is broken")

print("end of code")

#practice 

#marks =int(input("enter your number:"))
marks = 56#for using input remove # and this line then u can use this ok dont worry
if(marks >= 90):
    grade ="A"
elif(marks >= 80 and marks< 90):
    grade ="B"
elif(marks >= 70 and marks < 80):
    grade ="C"
else:
    print("D")

#print ("this is your result->",grade)

#no.12 nesting (iska matlb ha ka if ka ander if example dekho)

age =43

if(age >=18):
    if(age >= 80):
        print("cannot drive")
    print("can drive")
else:
    print("cannot drive")

#lets practice

      #question no.1 WAP which tell which number is odd or even look down
#to play this code remove#  from down line
#num =int(input("enter ur number:"))

#rem= num %2

#if(rem ==0):
  # print("even")
#else:
    # print("odd")


# check the greater number 
a=4
b=21
c=7
if(a>c and a>b):
    print("a")
elif(b>c):
    print("b")
else:
    print("c")

#check if 7 or any number is multiple of any
x=int(input("enter ur number:"))

if(x%7==0):
    print("true")
else:
    print("false")
