import os

n = 0
G = 0
s = ''
pExercise = [[0.891, 0.009, 0.1], [0.18, 0.77, 0.1], [0, 0, 1]]
rExercixe = [[8,8,0],[0,0,0],[0,0,0]]
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


def p(s,a,s'):
    i = j = 0
    if (s == "Unfit"):
        i = 1
    elif (s == "Dead"):
        i = 2


        


def r():

def q():


def V():
    return max( q(n,s,'exercise'), q(n,s,'relax') )


def q0(s,a):
    p(s,a,fit)r(s,a,fit)+p(s,a,unfit)r(s,a,unfit)


    
if __name__== "__main__":
  main()