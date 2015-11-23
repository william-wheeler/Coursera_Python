largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    try:
        if num == "done" : 
            break
        num = int(num)
        if smallest is None:
            smallest = num
        if largest is None:
            largest = num
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    except:
        print "Invalid input"

print "Maximum is", largest
print "Minimum is", smallest
    