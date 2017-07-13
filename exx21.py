def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
def subs(a, b):
    print "SUBSTRACTING %d - %d" % (a, b)
    return a - b
def multi(a, b):
    print "MULTIPLY %d * %d" % (a, b)
    return a * b
def divid(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Lets do some math with just fucntions!"

age = add(30, 5)
height = subs(78, 4)
weight = multi(90, 2)
iq = divid(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle"

what = add(age, subs(height, multi(weight, divid(iq, 2))))
print "That becomes: ", what, "can you do it by hand?"
