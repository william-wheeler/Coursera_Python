def computepay(h,r):
    ot = h - 40
    pp = r * 1.5
    return (r * 40)+(ot * pp)

hrs = raw_input("Enter Hours: ")
h = float(hrs)
rate = raw_input("Enter Rate: ")
r = float(rate)
if h > 40:
    p = computepay(h,r)
else: 
    p = h * r
print p