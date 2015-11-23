# #Open a file:
# global test
# test = open('test.txt')
# print test
# #search a file
# for search in test:
    # search = search.rstrip()
    # if search.startswith('I'):
        # print search
# #break a str into two lines, note that \n is counted as one character
# stuff = 'big\nballs'
# print stuff
# print len(stuff)

# #read each line in file that was opened in test variable, print each 
# # line while counting how many lines, finally print total number of lines counted
# test = open('test.txt')
# count = 0
# for line in test:
    # print line
    # count = count +1 
# print count

# #search for line containing
# test = open('test.txt')
# for line in test:
    # line = line.rstrip()
    # if not 'python' in line:
        # continue
    # print line
    
# #prompt for file
# filename = raw_input('Enter file name:  ')
# try:
    # file = open(filename)
# except:
    # print 'bad filename'
    # exit()
# file = open(filename)
# count = 0
# for line in filename:
    # line = line.rstrip()
    # if 'python' in line:
        # count = count + 1
# print 'There were',count,'lines continaing python in file',filename

# Use words.txt as the file name
# fname = raw_input("Enter file name: ")
# fh = open(fname)
# for line in fh:
    # line = line.rstrip()
    # print str.upper(line)
    
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
average = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    line = line.rstrip()
    line = line.lstrip('X-DSPAM-Confidence:')
    average = average + float(line)
print 'Average spam confidence:',(average / count)