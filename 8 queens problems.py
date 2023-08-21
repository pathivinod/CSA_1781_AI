num=int(input("enter the no.of queens:\t"))
board=[[0]*num for _ in range(0,num)]
def attack(i,j):
    for k in range(0,num):
        if((board[i][k]==1) or (board[k][j]==1)):
            return True
    for k in range(0,num):
        for l in range(0,num):
            if((k+l==i+j) or (k-l==i-j)):
                if(board[k][l]==1):
                    return True
    return False
def N_Queens(n):
    if(n==0):
        return True
    for i in range(0,num):
        for j in range(0,num):
            if(not(attack(i,j)) and (board[i][j]!=1)):
                board[i][j]=1
                if(N_Queens(n-1)==True):
                    return True
                board[i][j]=0
    return False
N_Queens(num)
for i in board:
    print(i)
