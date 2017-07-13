print "\n\t#### what you like iOS or Android Choose an option\n"
print "\t 1. iOS\n"
print "\t 2. Android\n"


# defined function for the first pros for ios
def _ios_pros():
    print "\n\t1. ios is better then android"
    _ios = raw_input("> ")

    if _ios == "yes":
        print " \t #### oh! are you apple fanboy?"
    else:
        print "\t ####You are fucking panaroid"

# defined the 1st function for pros android
def _andro_pro():
    print "\n \t 1. Android is open source.\n"
    andro = raw_input("> ")

    if  andro == "yes":
        print "\t #### you are smart\n"
    
    elif andro == "no":
        print "\t #### go, get some knowledge first\n "


    else:
        print "\t #### enter the correct keyword\n"
 

Choice = input("> ")
if Choice == 1:
    print "\t Do you agree with iOS, replay with yes or no \n"
    _ios_pros()
    

    

elif Choice == 2:
    print "\t pros of Android, if you agree, replay with yes or no\n"
    _andro_pro()

else:
    print "\tEnter the correct keywork\n"
