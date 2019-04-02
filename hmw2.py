import os

n = 0
G = 0
s = ''
pExercise = [[0.891, 0.009, 0.1], [0.18, 0.77, 0.1], [0, 0, 1]]
rExercise = [[8,8,0],[0,0,0],[0,0,0]]
pRelax = [[0.693, 0.297, 0.01], [0, 0.99, 0.01], [0,0,1]]
rRelax = [[10,10,0],[5,5,0],[0,0,0]]





def main():
    os.system('clear')
    global n 
    n = input("Enter a value for n >= 0: ")
    while (int(n) < 0):
        n=input("Try Again: ")

    global s
    s = input("Enter a state: (Fit, Unfit, Dead): ")
    while not ((s == 'Fit') or (s == 'Unfit') or (s == 'Dead')):
        s = input("Try Again: ")

    global G
    G = input("Enter a value for G where 0<G<1: ")
    while float(G) >= 1 or float(G) <= 0:
        G = input("Try Again: ")

    i = 0
    print("The program isn't frozen its just a little slow as in order to print asnwers in order from 0 to n it calculates all previous answers for each iteration n times")
    print("It will print finished when done")
    while i <= n:
        print ("For n = " +str(i)+ "and G = " +str(G)+ "Exercise = "+str(q(i, s, 'Exercise'))+" "+"Relax = "+  str(q(i, s, 'Relax')))
        i+= 1
    print('Finished')





def p(s,a,sDash):
    global pExercise
    global pRelax

    i = j = 0
    if (s == "Unfit"):
        i = 1
    elif (s == "Dead"):
        i = 2
    
    if (sDash == "Unfit"):
        j = 1
    elif (sDash == "Dead"):
        j = 2
    
    if(a == "Exercise"):
        return pExercise[i][j]
    else:
        return pRelax[i][j]
        

def r(s,a,sDash):
    global rExercise
    global rRelax
    i = j = 0
    if (s == "Unfit"):
        i = 1
    elif (s == "Dead"):
        i = 2
    
    if (sDash == "Unfit"):
        j = 1
    elif (sDash == "Dead"):
        j = 2
    
    if(a == "Relax"):
        return rRelax[i][j]
    else:
        return rExercise[i][j]

def V(n,s):
    return max(q(n,s, 'Exercise'), q(n,s, 'Relax'))
        


def q(n,s,a):
    if n == 0:
        return q0(s,a)
    
    else:
        return q0(s,a) + ((G)*(p(s,a,'Fit') * V(n-1,'Fit') + p(s,a,'Unfit') * V(n-1,'Unfit')))



def q0(s,a):
   return (p(s,a,'Fit') * r(s,a,'Fit')) + (p(s,a,'Unfit') * r(s,a,'Unfit'))


    
if __name__== "__main__":
  main()