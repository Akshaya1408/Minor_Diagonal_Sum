def minor_diagonal_sum(mat,row,col):

    sum=0
    j=row-1
    for i in range(row):
        sum+=mat[i][j]
        j-=1
    return sum

mat=[]
row=int(input("No of rows : "))
col=int(input("No of columns : "))
for i in range(row):
    mat.append(list(map(int,input().split())))

print(minor_diagonal_sum(mat,row,col))