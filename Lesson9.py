
#Dictionaries
# wii = dict()
# wii['Super Mario Galaxy'] = 1
# wii['Super Smash Bros'] = 2
# wii['Wii Fit'] = 3
# print wii

# count = dict()
# wii = ['Super Mario Galaxy','Super Smash Bros','Wii Fit']
# for game in wii:
    # count[game] = count.get(game,0) +1
# print count

# print count.items()
# print count.keys()
# print count.values()

# file = raw_input('Show me the file! ')
# handle = open(file,'r')
# read = handle.read()
# words = read.split()

# count = dict()
# for word in words:
   # count[word] = count.get(word,0) + 1

# bigcount = None
# bigword = None
# for word,count in count.items():
   # if bigcount is None or count > bigcount:
       # bigcount = count
       # bigword = word
# print bigword, bigcount

# stuff = dict()
# print stuff.get('candy',-1)

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name,'r')
count = dict()
for line in handle:
    if not line.startswith("From ") : continue
    value = line.split()
    value = value[1]
    count[value] = count.get(value,0) + 1

bigcount = None
bigword = None
for word,count in count.items():
   if bigcount is None or count > bigcount:
       bigcount = count
       bigword = word
       
print bigword, bigcount