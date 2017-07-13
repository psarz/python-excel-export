numbers = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennie', 2, 'dimes', 3, 'quartes']

for num in numbers:
    print "this is count %d" % num

for fruit in fruits:
    print "A fruit of type: %s" % fruit

for i in change:
    print "I got %r" % i

elements = []

for i in range(0, 6):
    print "Adding %d to the list" % i
    elements.append(i)

for i in elements:
    print "Elements was: %d" % i


