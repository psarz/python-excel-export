class just4fun():
    def cricket():
        teams = raw_input('Can you name all the cricket teams?')
        print teams
        name = []
        for  x in range(0,4):
           print 'cricket team %d' %x
           x = raw_input('>')
           name.append(x)
        print name 
         
    cricket(name)

    def players():
        
        print 'Enter the players name in %r'
        pyl_name = []
        for y in range(1,11):
            y = raw_input('>')
            ply_name.append(y)
        print ply_name

    players() 

