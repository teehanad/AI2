import os

n = 0
G = 0
s = ''
pexercise = [[0.891, 0.009, 0.1], [0.18, 0.72, 0.1], [0, 0, 1]]
rexercise = [[8,8,0],[0,0,0],[0,0,0]]
prelax = [[0.693, 0.297, 0.01], [0, 0.99, 0.01], [0,0,1]]
rrelax = [[10,10,0],[5,5,0],[0,0,0]]





def main():
    global n 
    n = int(raw_input("Enter a value for n >= 0: "))
    while (int(n) < 0):
        n=int(raw_input("Try Again: "))

    global s
    s = str(raw_input("Enter a state: (fit, unfit, dead): "))
    while not ((s == 'fit') or (s == 'unfit') or (s == 'dead')):
        s = str(raw_input("Try Again: "))

    global G
    G = float(raw_input("Enter a value for G where 0<G<1: "))
    while float(G) >= 1 or float(G) <= 0:
        G = float(raw_input("Try Again: "))

    i = 0
    print("------------------------------------------------------------------(Calculating values from 0 to "+str(n)+"...)""-----------------------------------------------------------------")
    while i <= n:
        print ("For n = " +str(i)+ " & G = " +str(G)+ " exercise = "+str(q(i, s, 'exercise'))+" "+"relax = "+  str(q(i, s, 'relax')))
        i+= 1
    print('--------------------------------------------------------------------------------Finished--------------------------------------------------------------------------------')





def p(s,a,sDash):
    global pexercise
    global prelax

    i = j = 0
    if (s == "unfit"):
        i = 1
    elif (s == "dead"):
        i = 2
    
    if (sDash == "unfit"):
        j = 1
    elif (sDash == "dead"):
        j = 2
    
    if(a == "exercise"):
        return pexercise[i][j]
    else:
        return prelax[i][j]
        

def r(s,a,sDash):
    global rexercise
    global rrelax
    i = j = 0
    if (s == "unfit"):
        i = 1
    elif (s == "dead"):
        i = 2
    
    if (sDash == "unfit"):
        j = 1
    elif (sDash == "dead"):
        j = 2
    
    if(a == "exercise"):
        return rexercise[i][j]
    else:
        return rrelax[i][j]

def V(n,s):
    return max(q(n,s, 'exercise'), q(n,s, 'relax'))
        


def q(n,s,a):
    if n == 0:
        return q0(s,a)
    
    else:
        return q0(s,a) + ((G)*(p(s,a,'fit') * V(n-1,'fit') + p(s,a,'unfit') * V(n-1,'unfit')))



def q0(s,a):
   return (p(s,a,'fit') * r(s,a,'fit')) + (p(s,a,'unfit') * r(s,a,'unfit'))


    
if __name__== "__main__":
  main()