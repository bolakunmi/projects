sample1=[1,4,6,2,5,4,3,7,0,7,5]
sample1.sort()
numbers=[]
print(sample1)
x=0
y=len(sample1) - 1
while x<y:
    
    if sample1[x] + sample1 [y] < 10 :
        x+=1
    if sample1[x]==sample1[x+1]:
        if sample1[x] + sample1[y] == 10:
            print ('%s,%s' %(sample1[x],sample1[y]))
            x+=1
    if sample1[x] + sample1 [y] > 10 :
        y-=1
    if sample1[y]==sample1[y-1]:
        if sample1[x] + sample1[y] == 10:
            print ('%s,%s' %(sample1[x],sample1[y]))
            y-=1
    
    if sample1[x] + sample1[y] == 10:
        if x==y:
            pass
        else:
            print ('%s,%s' %(sample1[x],sample1[y]))
            x+=1
        

    #infinite loop error

#print ('%d,%d' %(sample1[x],sample1[y]))


