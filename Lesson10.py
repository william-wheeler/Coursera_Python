#this is a test

#a tuple is a list that cannot be changed, it is immutable

#a tuple uses () vs lists that use [] vs dictionaries {}

#You can't sort a tuple .sort(reverse=True) or .sorted()

#Tuples are more effecient than lists

#The items() method in dictionaries returns a list of (key, values) tuples

#Tuples are comparable

#create a tuple
# a, b = (99, 98)
# #set variable to tuple
# c = a,b
# #print values of tuple
# print a
# print min(c)
# print a,b
# #show a list of attributes that can be used with tuples
# print dir(c)


# #change from dict it list then sort reversed and then iterate by k in list 
# d = {'Nintendo':1, 'Sega':2, 'Rare':3}
# t = d.items()
# print t
# t.sort(reverse=True)
# for k,v in sorted(d.items()):
    # print k,v
# print t

# x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
# y = x.items()
# print y

# c ={'Nintendo':1, 'Sega':2, 'Rare':3}
# tmp = list()
# for k, v in c.items() :
    # tmp.append( (v, k) )
# print tmp

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    if not line.startswith("From ") : continue
    value = line.split()
    value = value[5]
    value = value.split(':')
    value = value[0]
    count[value] = count.get(value,0) + 1
#print count
for k, v in sorted(count.items()):
    print k,v

 
