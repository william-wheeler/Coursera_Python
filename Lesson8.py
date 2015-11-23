# Lists
# A List is a kind of collection
# A collection allows us to put many values in a single variable
# A collection is nice because we carry all many values around in one convenient package
# Variables have one value 
# List constants are surrounded by square brakets and elements in the list are separated by commas.
# A list element can be any Python object - even another list
# A list can be empty
# Strings are immutable
# Lists are mutable
# len gives characters in a string
# len gives elements in a list
# the range function returns a list of numbers

# friends = ["Bill", "Bob", "Mary"]
# for i in range(len(friends)):
    # friend = friends[i]
    # print 'happy new year:', friend
    
# stuff = list()
# stuff.append('book')
# stuff.append(99)
# print stuff

# # Built in functions and lists
# nums = [1,2,3,4,6,77,9,4,2]
# print len(nums)
# print max(nums)
# print min(nums)
# print sum(nums)
# print sum(nums)/len(nums)

# numlist = list()
# while True:
    # inp = raw_input('Enter a number:')
    # if inp =='done':break
    # value = float(inp)
    # numlist.append(value)
    
# average = sum(numlist)/len(numlist)
# print 'average:', average

# fname = raw_input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
    # value = line.rstrip().split()
    # for word in value:
        # if word in lst:
            # pass
        # else:
            # lst.append(word)
# print sorted(lst)

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
lst = list()
count = 0
for line in fh:
    if not line.startswith("From ") : continue
    value = line.split()
    lst.append(value[1])
    count = count + 1
for add in lst:
    print add
print "There were", count, "lines in the file with From as the first word"
