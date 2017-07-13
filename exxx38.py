# This is a yes no text based game (like zork of the adventure) for the beginers.
#psarz
print "\n\t ###### Which cell phone do you own? \n"
def _brandName_():
    b_name = raw_input("> ")
    model_no = raw_input("\t enter the model number\t")
    print "\t #### you have entered %r \n \t and model no. :" % b_name,  model_no
_brandName_()

def _spacs_():
    print "\t Enter the  spacification of your device\n"
    _ram = raw_input(" RAM :\n")
    _camera = raw_input(" Camera :\n")
    _battery = raw_input(" battery :\n")
    _storage = raw_input(" storage : \n")
    _screen = raw_input(" screenSize : \n")
    print "\n \n\t #### Your cell phone has following features"
    print ("\n RAM: %r\n camera: %r \nbattery: %r\n storage: %r\n screen: %r" %(  _ram, _camera, _battery, _storage, _screen))
_spacs_()
