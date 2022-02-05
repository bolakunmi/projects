#MILESTONE!!!
from ast import Continue


def tik_tak_toe(x,o):
        entry_list=['a','b','c','d','e','f','g','h','i']
        new_list=[]
        board = """
        a_|_b_|_c
        d_|_e_|_f     
        g | h | i 
        """


        print(
        """
welcome to tic tak toe, may the best man win!
         _|_ _|_ 
         _|_ _|_      
          |   | 
                  
                """ )
        val=str(input("who starts? x or o"))
        def choice(val_x):
                while val_x in entry_list:      
                        val_x=str('your turn')
                        print (entry_list.remove(val_x))
                        print (new_list.append(val_x))
                        #not append, look for a function that can replace
                        print ("""
        a_|_b_|_c
        d_|_e_|_f     
        g | h | i 
        
        (a,b,c,d,e,f,g,h,i)"""
        
       """ 
        %s_|_%s_|_%s
        %s_|_%s_|_%s     
        %s | %s | %s
        """
        %(new_list)
        )
                else:
                        print('pick again')
                        Continue
