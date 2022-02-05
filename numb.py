
d={'a':' ','b':'a','c':' ','d':' ','e':' ','f':' ','g':' ','h':' ','i':' '}

entry_list_1=[]
for k in d.values():
    entry_list_1.append(k)
print(tuple(entry_list_1))
#print( 'works, %s' %d.values(2)
print ('%s, "free me" , %s, %s,%s,%s,%s,%s,%s,%s' %(tuple(entry_list_1)))