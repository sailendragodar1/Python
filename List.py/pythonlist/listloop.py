#Loop List

#following numbers are questions numbers
#--and below hash numbers are there answers....

#1.   Loop through a list
#2.   Loop Through the Index Numbers
#3.   Using a While Loop
#4.  Looping Using List Comprehension

 #1
 lists=["kxa",2,3,"ram"]
for x in lists: #printing all the items from a list one by one!
  print(x)

  #code
ram=["RAM","BABU",23,34,35,56,67,78]
for x in ram:
  print(x)
  print(ram)
 
 
 
  #2
#you can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.


List=["ram","babu",23,"Ghimire"]
for i in range(len(List)):  #LOOPING through index numbers
  print(List[i])


#3
List=["ram","babu",23,"Ghimire"]
i=0
while i < len(List):
  print(List[i])
  i=i+1

#4
#Looping Using List Comprehension

List=["ram","babu",23,"Ghimire"]
[print(x) for x in List]

