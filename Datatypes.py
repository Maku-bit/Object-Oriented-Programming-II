#There are about 8 data types;none(null),numeric,lists,tuple,set,string,range,dictionary
#None- is a variable that does not have any value otherwise known as null
#Numeric we have multiple(number) types ie int,float,complex,bool
#int
num=6
print(num)
print(type(num))
#float
num=2.5
print(type(num))
#complex a+bj is the standard formula
num= 6+9j
print(type(num))
#To convert float to int
a=6.7
b=int (a)
print(b)
#To convert to complex
a=3
j=4
s=complex(a,j)
print(s)

#bool
j>a
print(j>a)
#int(true)=0,int(false)=1

#lists
lst=[23,45,21,12]
print(type(lst))
#tuples
tup=(34,23,66,33,21)
print(type(tup))
#set
s={21,33,44,55,77,66}
print(type(set))

#string
st= 'Alexis'
print(type(str))

#range-gives a range
range(20)
print(range(20))

print(list(range(20)))

#to print even numbers in a range
print(list(range(2,20,2)))
#multiples of 3
range(45)
print(list(range(3,45,3)))

#Dictionaries/Maps
#used when you have large amounts of data
#it uses keys instead of indexing,every value has a key
#We use curly brackets{} because keys must not repeat and and sets are the only ones that dont replicate values
d={'alexis':'iphone8','daisy':'iphone11pro','camisha':'iphone6','faith':'iphone7plus'}
d.keys
print(d.keys())
print(d.values())
#To fetch idividual values
d['daisy']
print(d['daisy'])
#or
d.get('alexis')
print(d.get('alexis'))


