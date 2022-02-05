entry_list={'a':' ','b':' ','c':' ','d':' ','e':' ','f':' ','g':' ','h':' ','i':' '}
player_x='X'
player_o='O'

def choice(player_x):
    entry_list_convert=[]
    print (entry_list.keys())
    print ("""
            a_|_b_|_c
            d_|_e_|_f     
            g | h | i """)
    val_x=str(input('player "x" turn:'))
    val_x.lower()
    while val_x in entry_list:
        
        if val_x in entry_list:
            entry_list[val_x]=player_x      
            print (entry_list.values())
            #print (new_list.append(val_index))
                            #not append, look for a function that can replace
            
            for options in entry_list.values():
                entry_list_convert.append(options)
            print ("""
            %s_|_%s_|_%s, 
            %s_|_%s_|_%s,      
            %s | %s | %s 
            """
            %(tuple(entry_list.values()))
            )
            
        if val_x not in entry_list:
            print ('pick again:')
            continue
      
 
choice(player_x)