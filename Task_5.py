import math

class Vertices(object):
    def __init__(self, n, dots):
        self.n=n
        self.dots=dots
    def Get_n(self):
        return self.n
    def Get_dot(self, i):
        return self.dots[i]  
    def Get_dots(self):
        return self.dots    
    
    
def Get_int(opened_file):
    f=0
    s=0
    x='0'
    while (x!=''):
        x=opened_file.read(1)
        if (x==' ' or x=='' or x=='\n') and (f!=0):
            return s*f
        if (x==''):
            return 'end'        
        if (x!=' '):
            try:
                x=int(x)
                s=s*10+x
                if (f==0):
                    f=1            
            except:
                if (x=='-'):
                    f=-1
                elif(x!='\n'):
                    print("Wrong data\n")
                    exit()

def Get_dots(opened_file):
    s=[]
    a=Get_int(opened_file)
    if(a=='end'):
        print("Empty file\n")
        exit()
    b=Get_int(opened_file)
    if(b=='end'):
        print("Wrong data\n")
        exit()
    s.append([a,b])
    k=1
    while(a!='end'):
        a=Get_int(opened_file)
        if(a!='end'):
            b=Get_int(opened_file)
            if(b=='end'):
                print("Wrong data\n")
                exit()
            s.append([a,b]) 
            k+=1
    s.sort(key =lambda n: n[1], reverse=True)
    s.sort()            
    V = Vertices(k, s)   
    return V
 
def Angle(dot1, dot2, dot3):
    a=math.atan2(dot2[1]-dot1[1],dot2[0]-dot1[0])
    b=math.atan2(dot3[1]-dot2[1],dot3[0]-dot2[0])
    pi=math.atan2(0,-1)
    if(abs(a-b)>pi):
        return (2*pi-abs(a-b))
    return abs(a-b)

def Dist(dot1, dot2):
     return math.sqrt((dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2)
    
def Get_next(s, n, num):
    d=Dist(s[num],s[0])
    a=Angle(s[num-1], s[num], s[0])
    k=0
    for i in range(num+1, n):
        u=Dist(s[num], s[i])
        v=Angle(s[num-1], s[num], s[i])
        if( (u<d and v==a) or (v<a) ):
            d=u
            a=v
            k=i
    return k

def Autotest():
    s=[[0,0],[0,1],[1,0],[1,1]]
    d=Dist(s[0],s[1])
    if(d!=1):
        print("Autotest failed")
        exit(1)
    d=Angle(s[0],s[1],s[3])
    b=Angle(s[3],s[2],s[0])
    if(d!=b):
        print("Autotest failed")
        exit(2)   
    b=Get_next(s,4,1) 
    if(b!=3):
        print("Autotest failed")
        exit(3)          
    print("Autotest passed")
        


Autotest()  

try:
    file = open("data.txt", "r")
except:
    print("Cannot open file")
    exit()

V = Get_dots(file)
n=V.Get_n()

if(n<3):
    print("Add more dots")
    file.close()
    exit()
    
W = V.Get_dots()

k=2
for i in range(2,n):
    if(Angle(W[0],W[1],W[i])==0):
        k+=1
if(k==n):
    print("All dots lie on the same line")
    file.close()
    exit()  
    
num=1
k=1
f=2
while(k!=0):
    k=Get_next(W, n, num)
    num+=1
    if(num!=k and num<n):
        Q=W[num]
        W[num]=W[k]
        W[k]=Q
    if(k!=0):
        f+=1            
if(f!=n):
    print("Non-convex polygon")
else:
    print("Convex polygon")
file.close()    









