#To create lists in python we use []
names= ['Alex','Brian','Keiran','Kate']
names
print (names)
nums= [21,14,5,15,30]
print (nums)

#you can input two lists in one list
den= [names,nums]
print (den)

#lists are mutable ie you can change the values or edit them
#various functions to edit lists include:Append,clear,copy,count,extend,index,insert,pop,remove,reverse
#appending a list adds the appended number to the end of the list

nums.append(55)
print (nums)

#Clear clears the entire list
#syntax is nums.clear

#copy copies the entire list
#syntax is nums.copy

#insert inserts the value at the specified index
nums.insert(3,35)
print(nums)

#remove deletes a specified value from the list
nums.remove(5)
print(nums)

#pop deletes a value from a specified index
nums.pop(0)
print(nums)

#with the pop function if you dont specify an index it uses the last in first out(LIFO)concept of stacks in data structures
#nums.pop() will remove '55'
nums.pop()
print(nums)

#To delete multiple values we use del
del nums[2:]
print(nums)

#To add multiple values we use extend
nums.extend([25,5,40,55,15,10])
print(nums)


#there are also some inbuilt python functions to perform on lists such as; max,sum, min
#Max find the highest value in the list
print (max(nums))

#min finds the minimum value
print (min(nums))

#sums sums up thje whole list
print(sum(nums))


#you can also sort lists by using  sort
nums.sort()
print(nums)




