#--Google-Foobar-Challenge 
#----------------------1.1
#-----------solar-doomsday

from math import sqrt, floor  

def isPerfect(N):
    if (sqrt(N) - floor(sqrt(N)) != 0): 
        return False
    return True

if __name__=="__main__":
    n = int(input())
    t = n
    ans=""
    while(t>0 and n>0):
        if(isPerfect(n)):
            ans+=(str(n)+" ")
            t-=n
            n = t
            continue
        n-=1
    print(ans)