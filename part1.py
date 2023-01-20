n = int(input())
mat_input =[]
for i in range(n):
    a = input().split()
    a = [int(x) for x in a]
    mat_input+=[a]
#print(mat)
#********************************************************
def left_change(mat):
    mat2=[]
    for list1 in mat:
        list1=[int(x) for x in list1]
        for i in range(len(list1)-1):
            if list1[i]==0:
                list1[i+1],list1[i]=list1[i],list1[i+1]
            else:
                if (list1[i]==1 and list1[i+1]==2) or (list1[i]==2 and list1[i+1]==1):
                    list1[i] = 3
                    list1[i+1] = 0
                else:
                    if list1[i] == list1[i+1] and list1[i]!=1 and list1[i]!=2:
                        list1[i]= 2*list1[i]
                        list1[i+1] = 0
        mat2+=[list1]
    return mat2
#print(left_change(mat_input))
#********************************************************
def right_change(mat):
    mat2 =[]
    for list1 in mat:
        list1 = [int(x) for x in list1]
        list1 = list1[::-1]
        for i in range(len(list1)-1):
            if list1[i]==0:
                list1[i+1],list1[i]=list1[i],list1[i+1]
            else:
                if (list1[i]==1 and list1[i+1]==2) or (list1[i]==2 and list1[i+1]==1):
                    list1[i] = 3
                    list1[i+1] = 0
                else:
                    if list1[i] == list1[i+1] and list1[i]!=1 and list1[i]!=2:
                        list1[i]= 2*list1[i]
                        list1[i+1] = 0
        list1 = list1[::-1]
        mat2+=[list1]
    return mat2
#print(right_change(mat_input))
#*********************************************************
def down_change(mat,n1=n):
    mat2 =[]
    j = 0
    while j<n1:
        ls =[]
        for i in range(n1):
            ls+=[mat[i][j]]
            ls = [int(x) for x in ls]
        mat2+=[ls]
        j+=1
    mat3 = right_change(mat2)
    mat4 =[]
    j = 0
    while j<n1:
        ls =[]
        for i in range(n1):
            ls+=[mat3[i][j]]
            ls = [int(x) for x in ls]
        mat4+=[ls]
        j+=1
    return mat4
#print(down_change(mat_input,n))
#*****************************************************
def up_change(mat,n1=n):
    mat2 =[]
    j = 0
    while j<n1:
        ls =[]
        for i in range(n1):
            ls+=[mat[i][j]]
            ls = [int(x) for x in ls]
        mat2+=[ls]
        j+=1
    mat3 = left_change(mat2)
    mat4 =[]
    j = 0
    while j<n1:
        ls =[]
        for i in range(n1):
            ls+=[mat3[i][j]]
            ls = [int(x) for x in ls]
        mat4+=[ls]
        j+=1
    return mat4
#print(up_change(mat_input))
#***************************************************
def count_zero_down(mat,k1,d1):
    count = -1
    count_index = -1
    dc ={}
    for i in mat[0]:
        count_index+=1
        if i==0:
            count+=1
            dc[count] = count_index
    m = count+1
    zero_num = k1%m
    for j in dc.keys():
        if j==zero_num:
            change = dc[j]
    mat[0][change]=d1
    return mat
#print(count_zero_down([[0, 0, 0, 0], [0, 1, 1, 3], [2, 0, 0, 3], [3, 3, 0, 1]]))
def count_zero_up(mat,k1,d1,n1=n-1):
    count = -1
    count_index = -1
    dc ={}
    for i in mat[n1]:
        count_index+=1
        if i==0:
            count+=1
            dc[count] = count_index
    m = count+1
    zero_num = k1%m
    for j in dc.keys():
        if j==zero_num:
            change = dc[j]
    mat[n1][change]=d1
    return mat
#print(count_zero_up([[2, 1, 1, 6], [0, 1, 0, 1], [3, 2, 0, 0], [0, 0, 0, 0]]))

def count_zero_right(mat,k1,d1):
    count = -1
    count_index = -1
    dc = {}
    for i in mat:
        count_index+=1
        a = i[0]
        if a==0:
            count+=1
            dc[count] = count_index
    m = count+1
    zero_num = k1%m
    for j in dc.keys():
        if j==zero_num:
            change = dc[j]
    mat[change][0] = d1
    return mat
#print(count_zero_right([[0, 1, 1, 3], [0, 2, 0, 3], [0, 0, 1, 1], [0, 3, 2, 0]]))

def count_zero_left(mat,k1,d1,n1=n-1):
    count = -1
    count_index = -1
    dc = {}
    for i in mat:
        count_index+=1
        a=i[n1]
        if a==0:
            count+=1
            dc[count] = count_index
    m = count+1
    zero_num = k1%m
    for j in dc.keys():
        if j==zero_num:
            change = dc[j]
    mat[change][n1] = d1
    return mat
#print(count_zero_left([[1, 1, 3, 0], [2, 0, 3, 0], [1, 0, 1, 0], [3, 2, 0, 0]]))
#*********************************************************************************
s = input()
movement = []
for i in s:
    movement+=[i]
#print(movement)
for i in movement:
    inp = input().split()
    k = int(inp[0])
    d = int(inp[1])
    if i=='D':
        new_mat = down_change(mat_input)
        if new_mat == mat_input:
            mat_input = new_mat
        else:
            new_mat_2 = count_zero_down(new_mat,k,d)
            mat_input = new_mat_2
    elif i=='U':
        new_mat = up_change(mat_input)
        if new_mat == mat_input:
            mat_input = new_mat
        else:
            new_mat_2 = count_zero_up(new_mat,k,d)
            mat_input = new_mat_2
    elif i=='R':
        new_mat = right_change(mat_input)
        if new_mat== mat_input:
            mat_input = new_mat
        else:
            new_mat_2 = count_zero_right(new_mat,k,d)
            mat_input = new_mat_2
    elif i=='L':
        new_mat = left_change(mat_input)
        if new_mat== mat_input:
            mat_input = new_mat
        else:
            new_mat_2 = count_zero_left(new_mat,k,d)
            mat_input = new_mat_2
#score
score=0
for i in new_mat_2:
    for j in i:
        count_tavan=-1
        if j==0 or j==1 or j==2:
            continue
        else:
            num=j//3
            while num!=0:
                num=num//2
                count_tavan+=1
        score += 3**(count_tavan+1)
for m in new_mat_2:
    for n in m:
        print(n, end = '\t')
    print()


if (down_change(new_mat_2)==new_mat_2) and (up_change(new_mat_2)==new_mat_2) and (left_change(new_mat_2)==new_mat_2) and (right_change(new_mat_2)==new_mat_2):
    print('The final score is '+str(score))
else:
    print('The partial score is '+str(score))















#
