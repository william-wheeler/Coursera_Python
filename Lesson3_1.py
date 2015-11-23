#45 hours
#10.5 per hour

hrs = raw_input("Enter Hours: ")
h = float(hrs)
rate = raw_input("Enter Rate: ")
r = float(rate)
if h > 40:
    ot = h - 40
    pp = r * 1.5
    print (r * 40)+(ot * pp)
else: 
    print h * r