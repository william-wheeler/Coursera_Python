grade = raw_input("Enter Grade between 0.0 and 1.0: ")
try:
    g = float(grade)   
    if g > 1:
        print "Cannot have grade greater than 1.0"
    elif g >= 0.9:
        print "A"
    elif g >= 0.8:
        print "B"
    elif g >= 0.7:
        print "C"
    elif g >= 0.6:
        print "D"
    elif g < 0.6:
        print "F"
except:
    print "Only enter an number betweeen 0.0 and 1.0"        