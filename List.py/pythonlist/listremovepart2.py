thisislist =["kk",23,343,55,"ram",55]
print(thisislist)
thisislist.remove(23) #removing specific item from the list
thisislist.remove(55) #if same items then first one will me out
thisislist.pop(0) #removing specified index
print(thisislist)
thisislist.pop() #if index not specified then removes last item
print(thisislist)
thisislist1 =["kk",23,343,55,"ram",55]
del thisislist1[2]  #del method if index not specified then whole list
print(thisislist1)
# can be used "clear" or "del" for cut out the whole list