print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good Job!"
    elif bear == "2":
        print "The bear eats your legs off. Good Job!"
    else:
        print "well, doing %s is probably better. Bear runs away." % bear


elif door == "2":
    print "you stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. yellow jacket clothespins."
    print "3. understanding revolvers yelling melodies."


    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "your body survives powered by a mind jello. Good Job!"
    else:
        print "The insanity rots your eyes into a pool muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good Job!"

