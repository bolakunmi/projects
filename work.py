def tictactoe():
    winner = ' '
    entry_list={'a':' ','b':' ','c':' ','d':' ','e':' ','f':' ','g':' ','h':' ','i':' '}
    player_x='X'
    player_o='O'
    board_tutorial="""

                a_|_b_|_c
                d_|_e_|_f     
                g | h | i 
                
                """
    board_play="""

                %s_|_%s_|_%s, 
                %s_|_%s_|_%s,      
                %s | %s | %s 
                """
    
    #DPLAY DEFINITIONS
    def choice(player_x):
        entry_list_convert=[]
        print (board_tutorial)
        val=str(input('player "X" turn:')).lower()
        while entry_list[val]==' ':
            entry_list[val]=player_x      

                #conversion of dictionary keys to tuple   
            for k in entry_list.values():
                entry_list_convert.append(k)
            print (board_play%(tuple(entry_list_convert)))

            #VICTORY CHECK
            if ((entry_list['a'] == entry_list['b'] == entry_list['c']=='X')) or\
             ((entry_list['d'] == entry_list['e'] == entry_list['f']=='X')) or\
             ((entry_list['g'] == entry_list['h'] == entry_list['i']=='X')) or\
             ((entry_list['a'] == entry_list['d'] == entry_list['g']=='X')) or\
             ((entry_list['b'] == entry_list['e'] == entry_list['h']=='X')) or\
             ((entry_list['c'] == entry_list['f'] == entry_list['i']=='X')) or\
             ((entry_list['a'] == entry_list['e'] == entry_list['f']=='X')) or\
             ((entry_list['f'] == entry_list['e'] == entry_list['g']=='X')):
                winner = 'x'
                return ("""player X wins!""")
        
        if (val!=entry_list.values()) or (entry_list[val]!=' '):
            print ("""              bakayaro!
                        
                no vex me ooo, pick again.  
                                                    """)


    def choice(player_o):
        entry_list_convert=[]
        print (board_tutorial)
        val=str(input('player "O" turn:')).lower()
        while entry_list[val]==' ':
            entry_list[val]=player_o      

                #conversion of dictionary keys to tuple   
            for k in entry_list.values():
                entry_list_convert.append(k)
            print (board_play%(tuple(entry_list_convert)))

            #VICTORY CHECK
            if ((entry_list['a'] == entry_list['b'] == entry_list['c']=='O'))\
            or ((entry_list['d'] == entry_list['e'] == entry_list['f']=='O'))\
            or ((entry_list['g'] == entry_list['h'] == entry_list['i']=='O'))\
            or ((entry_list['a'] == entry_list['d'] == entry_list['g']=='O'))\
            or ((entry_list['b'] == entry_list['e'] == entry_list['h']=='O'))\
            or ((entry_list['c'] == entry_list['f'] == entry_list['i']=='O'))\
            or ((entry_list['a'] == entry_list['e'] == entry_list['f']=='O'))\
            or ((entry_list['f'] == entry_list['e'] == entry_list['g']=='O')):
                winner='o'
                return ("""player O wins!""")
        
        if (val!=entry_list.values()) or (entry_list[val]!=' '):
            print ("""          bakayaro!
                        
                no vex me ooo, pick again.  
                                                    """)

                    
    #GAME BEGINS
    print("""welcome to the TIC-TAC-TOA
            get ready for battle soldier!
                    HAJIME!                    
                                        """)

    player_1=str(input("who goes first? X or O?")).lower()
    while player_1=='x' or player_1=='o':
        if player_1=='x':
            while winner!='x' or winner !='o':
                choice(player_x)
                choice(player_o)
                #for key in list(entry_list.values):
                 #   if entry_list[key] != ' ':
                  #      print('it is a tie')
                #break
            print('shobu ari')
        elif player_1=='o':
            while winner!='x' or winner !='o':
                choice(player_o)
                choice(player_x)
                #for key in list(entry_list.values):
                 #   if entry_list[key] != ' ':
                  #      print('it is a tie')
                #break
            print('shobu ari')
        
    else:
        print('you no dey read instruction?')
    
#sort out when its a tie
#victory check isnt working yet
#first player isnt working well.
tictactoe() 
