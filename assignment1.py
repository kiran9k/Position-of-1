a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
i=0;
print "using linear search"
x=0
while (a[x]<>1):
    x=x+1
print x-1  # it gives the position of 1st array
################################################

""" the second method is much more effective than the first
It first searches the elements by raising the array index to power of 2 ,. i.e, indexed search. 
then it uses the binary search method . """

#######################################
print"using another method:" 
while(a[2**i]!=1):
    i=i+1
    print i
j=2**(i-1)
i=2**i
#print i,j
while(j<i):
    k=(i+j)/2
    print k
    if(a[k]==1):
        if(a[k-1]==0):
            print k
            break
        else:
            i=k-1
    else:
        j=k+1;

#print "hi"
print "value of index is:"
print k

