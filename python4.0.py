#data is deleted review first 10 mint of apnacollege
std={
    "name":"hafsa",
    "subject":{
        "math":12,
        "physics":15
    }
}
print (std)
print(std.keys())
print(len(list(std.keys())))
print(len(std))
print(std.values())#this also can convert in list
print(list(std.values()))
print(std.items())
#we can also aces any valuas in dic indiviually
pairs=list(std.items())
print(pairs[0])

#print(std.get("name2"))#in this type the wrong value if i write like name its name this will give us "none"
print(std["name"])#this type (is which wrong value will give error)

new_dic={"city":"karachi"}
std.update(new_dic)
print(std)
