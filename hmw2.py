#Adam Teehan - 16318274 - April 2019
n = 0
G = 0
s = ''
pexercise = [[0.891, 0.009, 0.1], [0.18, 0.72, 0.1], [0, 0, 1]]
rexercise = [[8,8,0],[0,0,0],[0,0,0]]
prelax = [[0.693, 0.297, 0.01], [0, 0.99, 0.01], [0,0,1]]
rrelax = [[10,10,0],[5,5,0],[0,0,0]]





def main():
    #Take in n value and repeat until it is is of correct format
    global n 
    n = int(raw_input("Enter a value for n >= 0: "))
    while (int(n) < 0):
        n=int(raw_input("Try Again: "))

    #Take in s value and repeat until it is is of correct format
    global s
    s = str(raw_input("Enter a state: (fit, unfit, dead): "))
    while not ((s == 'fit') or (s == 'unfit') or (s == 'dead')):
        s = str(raw_input("Try Again: "))

    #Take in G value and repeat until it is is of correct format
    global G
    G = float(raw_input("Enter a value for G where 0<G<1: "))
    while float(G) >= 1 or float(G) <= 0:
        G = float(raw_input("Try Again: "))

    #Print a wait message while the loops runs ans calculates answers
    i = 0
    print("------------------------------------------------------------------(Calculating values from 0 to "+str(n)+"...)""-----------------------------------------------------------------")
    while i <= n:
        print ("For n = " +str(i)+ " & G = " +str(G)+ " exercise = "+str(q(i, s, 'exercise'))+" "+"relax = "+  str(q(i, s, 'relax')))
        i+= 1
    print('--------------------------------------------------------------------------------Finished--------------------------------------------------------------------------------')



#Functions below are recusivly called using the n value passed in 
#Probability function, indexes into a 2d array based on the Current state, action and Desired next state (s, a, s')
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


#Reward function, like above indexes into a 2d array based on the Current state, action and Desired next state (s, a, s')
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

#Discounted Gamma value function from assignmemt sheet with n for recusrsion
def V(n,s):
    return max(q(n,s, 'exercise'), q(n,s, 'relax'))
        

#Esentially the qn+1 function from assignemmt sheet with n for recusrsive calls
def q(n,s,a):
    if n == 0:
        return q0(s,a)
    
    else:
        return q0(s,a) + ((G)*(p(s,a,'fit') * V(n-1,'fit') + p(s,a,'unfit') * V(n-1,'unfit')))


#q0 function from assignment sheet
def q0(s,a):
   return (p(s,a,'fit') * r(s,a,'fit')) + (p(s,a,'unfit') * r(s,a,'unfit'))


    
if __name__== "__main__":
  main()