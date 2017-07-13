def tiger():
    print "wow,the fastest animal.\n"
def cat():
    print "The cutest animal\n"
def monkey():
    print "The smartest animal\n"
def dog():
    print"The most loyal animal\n"
def horse():
    print "The royal animal\n"


print "#####Welcome to Short GK ! \n"
print "Animals are the dearest creation of god\n"
print "Here are 5 animals listed below.\n"
print "1. Tiger\n"
print "2. Cat\n"
print "3. Monkey\n"
print "4. Dog\n"
print "5. Horse\n"

print "Choose one of them.\n"

animal = input("> ")

if animal == 1:
    tiger()
elif animal == 2:
        cat()
elif animal == 3:
        monkey()
elif animal == 4:
        dog()
else:
    horse()

