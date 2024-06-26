row,col=map(int,input().split()) #space seperated input for row and col

mat=[[j for j in input().split()]for i in range(row)] #space seperated input for matrix
 
for i in range(row):
    print()
    for j in range(col):
        if mat[i][j]=="*":
            print("*",end=" ")
        else:
            count=0
            # let take firstly basic condition for center block
            if i-1>=0 and mat[i][j]!=mat[i-1][j]:   #up
                count +=1
            if j+1<col and mat[i][j]!=mat[i][j+1]:   #right
                count +=1
            if i+1<row and mat[i][j]!=mat[i+1][j]:   #down
                count +=1
            if j-1>=0 and mat[i][j]!=mat[i][j-1]:   #left
                count +=1
            if (j+1<col and i-1>=0) and mat[i][j]!=mat[i-1][j+1]:   #up-right
                count +=1
            if (j+1<col and i+1<row) and mat[i][j]!=mat[i+1][j+1]:   #down-right
                count +=1
            if (i+1<row and j-1>=0) and mat[i][j]!=mat[i+1][j-1]:   #down-left
                count +=1
            if (j-1>=0 and i-1>=0) and mat[i][j]!=mat[i-1][j-1]:   #up-left
                count +=1
            # ans.append(count)
            print(count,end=" ")